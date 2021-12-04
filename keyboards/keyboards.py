from bot.keyboards import ReplyKeyboardMarkup, KeyboardButton, ButtonColors
from emoji import emojize


def homework_options_keyboard():
    markup = ReplyKeyboardMarkup(row_width=3)

    markup.add_keyboard({
        "one_time": False,
        "buttons": [
            [KeyboardButton("Сегодня"), KeyboardButton("Завтра")],
            [KeyboardButton("Эта неделя"), KeyboardButton("Следующая неделя")],
            [KeyboardButton("пн"), KeyboardButton("вт"), KeyboardButton("ср")],
            [KeyboardButton("чт"), KeyboardButton("пт"), KeyboardButton("сб")],
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
            [KeyboardButton("Добавить домашку"), KeyboardButton("Добавить дедлайн")],
            [KeyboardButton("Сайт")],
        ]
    })
    return markup



