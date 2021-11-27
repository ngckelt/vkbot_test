from bot.keyboards import ReplyKeyboardMarkup, KeyboardButton, ButtonColors
from emoji import emojize


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


def main_keyboard():
    markup = ReplyKeyboardMarkup(row_width=2)
    markup.add_keyboard({
        "one_time": False,
        "buttons": [
            [KeyboardButton("Домашка"), KeyboardButton("Дедлайны")],
            [KeyboardButton("Сайт"), KeyboardButton("Расписание")],
        ]
    })
    return markup



