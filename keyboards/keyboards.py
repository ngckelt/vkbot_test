from bot.keyboards import ReplyKeyboardMarkup, KeyboardButton, ButtonColors
from emoji import emojize


def yes_or_no_keyboard():
    markup = ReplyKeyboardMarkup(row_width=2)

    btn_yes = KeyboardButton(f"Да {emojize(':sunglasses:', use_aliases=True)}", ButtonColors.GREEN)
    btn_no = KeyboardButton("Нет", ButtonColors.RED)

    markup.add_buttons(btn_yes, btn_no)
    return markup

