from bot.keyboards import ReplyKeyboardMarkup, KeyboardButton, ButtonColors
from emoji import emojize


def yes_or_no_keyboard():
    markup = ReplyKeyboardMarkup(row_width=2)

    btn_yes = KeyboardButton(f"Да {emojize(':sunglasses:', use_aliases=True)}", ButtonColors.GREEN)
    btn_no = KeyboardButton("Нет", ButtonColors.RED)

    markup.add_buttons(btn_yes, btn_no)
    return markup


def homework_options_keyboard():
    markup = ReplyKeyboardMarkup(row_width=3)

    markup.add_keyboard({
        "one_time": False,
        "buttons": [
            [KeyboardButton("Сегодня"), KeyboardButton("Завтра")],
            [KeyboardButton("Эта неделя"), KeyboardButton("Следующая неделя")],
            [KeyboardButton("ПН"), KeyboardButton("ВТ"), KeyboardButton("СР")],
            [KeyboardButton("ЧТ"), KeyboardButton("ПТ"), KeyboardButton("СБ")],
            [KeyboardButton("Все")],
        ]
    })

    return markup


