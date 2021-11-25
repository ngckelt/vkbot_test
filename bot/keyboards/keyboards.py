import json
from dataclasses import dataclass


@dataclass
class ButtonColors:
    BLUE = "primary"
    RED = "negative"
    GREEN = "positive"


class KeyboardButton:

    def __init__(self, text, color=ButtonColors.BLUE):
        self.text = text
        self.color = color

    def to_json(self):
        return {
            "action": {
                "type": "text",
                "label": self.text
            },
            "color": self.color
        }

    @property
    def json(self):
        return self.to_json()


class ReplyKeyboardMarkup:

    def __init__(self, row_width=1, one_time=False):
        self.row_width = row_width
        self.one_time = one_time
        self.buttons = []
        self.keyboard = None

    def add_keyboard(self, keyboard):
        self.keyboard = keyboard

    def add_button(self, btn: KeyboardButton):
        self.buttons.append(btn)

    def add_buttons(self, *buttons):
        for btn in buttons:
            self.add_button(btn)

    def format_buttons(self):
        grid = []
        buttons_quantity = len(self.buttons)
        i = 0
        while buttons_quantity:
            buttons = []
            for _ in range(self.row_width):
                try:
                    buttons.append(self.buttons[i].json)
                    i += 1
                    buttons_quantity -= 1
                except IndexError:
                    continue
            grid.append(buttons)
        return grid

    def format_keyboard(self):
        for buttons in self.keyboard['buttons']:
            for i in range(len(buttons)):
                buttons[i] = buttons[i].json

    @staticmethod
    def decode_markup(markup):
        return str(markup.decode('utf-8'))

    @staticmethod
    def encode_markup(markup):
        return json.dumps(markup, ensure_ascii=False).encode('utf-8')

    def __reply_keyboard(self):
        reply_keyboard = {
            "one_time": self.one_time,
            "buttons": self.format_buttons()
        }
        reply_keyboard = self.encode_markup(reply_keyboard)
        return self.decode_markup(reply_keyboard)

    def __repr__(self):
        if self.keyboard:
            self.encode_markup(self.format_keyboard())
            return self.decode_markup(self.encode_markup(self.keyboard))
        return self.__reply_keyboard()


class EmptyKeyboard(ReplyKeyboardMarkup):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



