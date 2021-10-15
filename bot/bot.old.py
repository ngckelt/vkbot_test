import asyncio
import vk_api

from bot.storage.storage import StateStorage
from sys import exit
from bot.types import Message
from bot.types import Handler
from bot.filters import Filters
from vk_api.longpoll import VkLongPoll, VkEventType


class Bot:
    handlers = []

    def __init__(self, token):
        self._token = token
        self._vk_session = vk_api.VkApi(token=self._token)
        self._vk = self._vk_session.get_api()
        self._longpoll = VkLongPoll(self._vk_session)

    @staticmethod
    async def set_state(user_vk_id, state_name):
        if not StateStorage.exists(user_vk_id):
            StateStorage.alloc(user_vk_id)
        StateStorage.set_state(user_vk_id, state_name)

    @staticmethod
    async def get_state_data(user_vk_id):
        return StateStorage.get_data(user_vk_id)

    @staticmethod
    async def update_state_data(user_vk_id, **data):
        StateStorage.update_data(user_vk_id, **data)

    @staticmethod
    async def finish_state(user_vk_id):
        StateStorage.free(user_vk_id)

    @staticmethod
    async def get_current_state(user_vk_id):
        return StateStorage.get_current_state(user_vk_id)

    def message_handler(self, text: str = None, regexp: str = None, state: str = None):
        def decorator(method):
            self.register_message_handler(method, text, regexp, state)
            return method

        return decorator

    def register_message_handler(self, handler: callable, text=None, regexp=None, state=None):
        handler = Handler(handler)
        handler.bind_filters(text, regexp, state)
        self.handlers.append(handler)

    async def run(self):
        for event in self._longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                message = Message(user_id=event.user_id, text=event.text, timestamp=event.timestamp)
                current_user_state = StateStorage.get_current_state(message.user_id)
                filters_set = Filters(text=event.text, regexp=event.text, state=current_user_state)

                for handler in self.handlers:
                    if await handler.match_filters(filters_set):
                        await handler.method(message)
                        break

    def start_polling(self):
        print("Start polling")
        print(self.handlers)
        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.run())
        except KeyboardInterrupt:
            loop.close()
            exit()
        self.start_polling()

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



