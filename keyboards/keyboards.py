from bot.keyboards import ReplyKeyboardMarkup, KeyboardButton, ButtonColors, EmptyKeyboard
from bot.settings import WEEK_DAYS


def homework_options_keyboard():
    markup = ReplyKeyboardMarkup(row_width=3)

    markup.add_keyboard({
        "one_time": False,
        "buttons": [
            [KeyboardButton("Сегодня"), KeyboardButton("Завтра")],
            # [KeyboardButton("Эта неделя"), KeyboardButton("Следующая неделя")],
            [KeyboardButton("пн"), KeyboardButton("вт"), KeyboardButton("ср")],
            [KeyboardButton("чт"), KeyboardButton("пт"), KeyboardButton("сб")],
            [KeyboardButton("Все что есть")],
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


def subject_keyboard(subjects):
    markup = ReplyKeyboardMarkup()
    for subject in subjects:
        if len(subject) > 40:
            subject = subject[:37] + "..."
        markup.add_button(KeyboardButton(subject[:40]))
    return markup


def week_days_keyboard():
    markup = ReplyKeyboardMarkup(row_width=3)
    for week_day in WEEK_DAYS:
        markup.add_button(KeyboardButton(week_day))
    return markup


def empty_keyboard():
    return EmptyKeyboard()



