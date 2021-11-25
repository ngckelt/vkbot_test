import asyncio
import inspect
import vk_api
from bot.states import FSMContext
from bot.types import Message
from bot.filters import Filters
from bot.dispatcher import Dispatcher
from vk_api.longpoll import VkLongPoll, VkEventType
from sys import exit
# from logs import logger

from pprint import pprint


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
                await handler.method(*args)
                break

    async def process_event(self, event, dp: Dispatcher):
        message = Message(self, user_id=event.user_id, text=event.text, timestamp=event.timestamp)
        state = FSMContext(message.user_id)
        current_state = await state.get_current()
        filters_set = Filters(text=message.text, regexp=message.text, state=current_state)
        await self.process_handler(dp, message, filters_set)

    async def run(self, dp: Dispatcher):
        for event in self._longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                await self.process_event(event, dp)

    @staticmethod
    def stop_polling(loop):
        loop.close()
        exit()

    def start_polling(self, dp):
        # logger.info("Start polling")
        print("Start polling")
        main_loop = asyncio.new_event_loop()
        try:
            main_loop.run_until_complete(self.run(dp))
        except KeyboardInterrupt:
            print("Stop polling")
            # logger.info("Stop polling")
            self.stop_polling(main_loop)
        except Exception as e:
             # logger.critical(f"CRITICAL {e}")
            print(e)
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

