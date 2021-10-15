from bot.states import State


class RegisterUser:
    get_first_name = State()
    get_last_name = State()
    get_course = State()
    get_group = State()
    get_email = State()
    get_phone = State()
