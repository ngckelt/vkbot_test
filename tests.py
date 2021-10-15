import json


class KeyboardButton:

    def __init__(self, text, color="primary"):
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

    def __repr__(self):
        _keyboard = []
        btns_quantity = len(self.buttons)
        i = 0
        while btns_quantity:
            _buttons = []
            for _ in range(self.row_width):
                try:
                    _buttons.append(self.buttons[i].json)
                    i += 1
                    btns_quantity -= 1
                except IndexError:
                    continue
            _keyboard.append(_buttons)
        reply_keyboard = json.dumps(_keyboard, ensure_ascii=False).encode('utf-8')
        reply_keyboard = str(reply_keyboard.decode('utf-8'))
        return reply_keyboard


b1 = KeyboardButton("btn1")
b2 = KeyboardButton("btn2")


markup = ReplyKeyboardMarkup()


markup.add_buttons(b1, b2)




