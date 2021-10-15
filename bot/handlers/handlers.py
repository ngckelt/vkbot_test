from bot.filters.filters import Filters
from re import match
from dataclasses import dataclass

from bot.states import State


class Handler:

    def __init__(self, method: callable):
        self.method = method
        self.filters = list()

    def get_data(self):
        return self.HandlerObject(self.method, self.filters)

    def bind_filters(self, text: str, regexp: str, state: State) -> None:
        filters = Filters(text, regexp, state)
        self.filters.append(filters)

    @staticmethod
    def __match_text(method_text: str, filter_text: str) -> bool:
        if isinstance(method_text, str) and isinstance(filter_text, str):
            return method_text == filter_text
        return True

    @staticmethod
    def __match_regexp(method_regexp: str, filter_regexp: str) -> bool:
        if isinstance(method_regexp, str) and isinstance(filter_regexp, str):
            return bool(match(method_regexp, filter_regexp))
        return True

    @staticmethod
    def __match_state(method_state: State, filter_state: str) -> bool:
        if method_state is None and filter_state is None:
            return True
        if method_state is not None and filter_state is not None:
            return method_state.get_state() == filter_state
        return False

    async def match_filters(self, filters_set: Filters) -> bool:
        for method_filter in self.filters:
            if self.__match_state(method_filter.state, filters_set.state):
                if not self.__match_text(method_filter.text, filters_set.text):
                    return False
                if not self.__match_regexp(method_filter.regexp, filters_set.regexp):
                    return False
                return True
            return False

    @dataclass
    class HandlerObject:
        method: callable
        filters: list

