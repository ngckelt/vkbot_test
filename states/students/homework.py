from bot.states import State


class Homework:
    get_option = State()


class AddHomework:
    get_homework_subject = State()
    get_homework_text = State()
    get_homework_date = State()


