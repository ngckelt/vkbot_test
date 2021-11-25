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

    def __json_btn(self):
        return {
            "action": {
                "type": "text",
                "label": self.text
            },
            "color": self.color
        }

    @property
    def json(self):
        return self.__json_btn()


class ReplyKeyboardMarkup:

    def __init__(self, row_width=1, one_time=False):
        self.row_width = row_width
        self.one_time = one_time
        self.buttons = []

    def add_button(self, btn: KeyboardButton):
        self.buttons.append(btn)

    def add_buttons(self, *buttons):
        for btn in buttons:
            self.add_button(btn)

    def __format_buttons(self):
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

    def __reply_keyboard(self):
        reply_keyboard = {
            "one_time": self.one_time,
            "buttons": self.__format_buttons()
        }
        reply_keyboard = json.dumps(reply_keyboard, ensure_ascii=False).encode('utf-8')
        return str(reply_keyboard.decode('utf-8'))

    def __repr__(self):
        return self.__reply_keyboard()


class EmptyKeyboard(ReplyKeyboardMarkup):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



