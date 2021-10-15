from bot.handlers import Handler
from bot.states import State


class Dispatcher:
    handlers = []

    def __init__(self):
        ...

    def message_handler(self, text: str = None, regexp: str = None, state: State = None) -> callable:
        def decorator(method):
            self.register_message_handler(method, text, regexp, state)
            return method
        return decorator

    def register_message_handler(self, handler: callable, text=None, regexp=None, state=None) -> None:
        handler = Handler(handler)
        handler.bind_filters(text, regexp, state)
        self.handlers.append(handler)

