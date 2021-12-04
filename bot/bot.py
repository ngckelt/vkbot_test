import asyncio
import inspect
import vk_api
from bot.states import FSMContext
from bot.types import Message
from bot.filters import Filters
from bot.dispatcher import Dispatcher
from vk_api.longpoll import VkLongPoll, VkEventType
from logs import logger
from sys import exit


class Bot:

    def __init__(self, token: str):
        self._token = token
        self._vk_session = vk_api.VkApi(token=self._token)
        self._vk = self._vk_session.get_api()
        self._longpoll = VkLongPoll(self._vk_session)

    @staticmethod
    async def process_handler(dp: Dispatcher, message: Message, filters_set: Filters):
        for handler in dp.handlers:
            if await handler.match_filters(filters_set):
                args = list()
                method_args = inspect.getfullargspec(handler.method).annotations
                if method_args.get('message'):
                    args.append(message)
                if method_args.get('state'):
                    state = FSMContext(message.user_id)
                    args.append(state)
                return await handler.method(*args)

    async def process_event(self, event, dp: Dispatcher):
        message = Message(self, user_id=event.user_id, text=event.text, timestamp=event.timestamp)
        state = FSMContext(message.user_id)
        current_state = await state.get_current()
        filters_set = Filters(text=message.text, regexp=message.text, state=current_state)
        await self.process_handler(dp, message, filters_set)

    async def run(self, dp: Dispatcher):
        for event in self._longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                logger.info(event.text)
                await self.process_event(event, dp)
        await asyncio.sleep(1)

    @staticmethod
    def stop_polling(loop):
        loop.close()
        exit()

    def start_polling(self, dp):
        logger.info("Start polling")
        main_loop = asyncio.get_event_loop()
        main_loop.create_task(self.run(dp))
        try:
            main_loop.run_forever()
        except KeyboardInterrupt:
            logger.info("Stop polling")
            self.stop_polling(main_loop)
        except Exception as e:
            logger.critical(f"CRITICAL {e}")
        self.start_polling(dp)

    async def send_message(self, chat_id, text, keyboard=None):
        random_id = vk_api.utils.get_random_id()
        self._vk_session.method(
            'messages.send',
            {
                'user_id': chat_id,
                'message': text,
                'random_id': random_id,
                'keyboard': keyboard
            }
        )

    async def send_photo(self, chat_id, photo_id):
        random_id = vk_api.utils.get_random_id()
        self._vk_session.method(
            "messages.send",
            {
                "attachment": photo_id,
                "message": "test",
                "user_id": chat_id,
                "random_id": 0
            }
        )

    async def get_user(self, user_vk_id):
        user = self._vk_session.method(
            "users.get",
            {
                "user_id": user_vk_id
            }
        )
        return user[0]


