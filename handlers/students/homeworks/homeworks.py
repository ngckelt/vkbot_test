from loader import dp
from bot.states import FSMContext
from bot.types import Message
from keyboards.keyboards import homework_options_keyboard, main_keyboard
from states.students.homework import Homework
from .utils import correct_week_day


@dp.message_handler(text="Домашка")
async def send_homework_options(message: Message, state: FSMContext):
    await message.answer("Выбери нужный пункт", keyboard=homework_options_keyboard())
    await state.start()
    await state.set_state(Homework.get_option)


@dp.message_handler(state=Homework.get_option, regexp="^[а-яА-Яё -]{2}$")
async def get_homework_by_week_day(message: Message, state: FSMContext):
    week_day = message.text
    print(week_day)
    if correct_week_day(week_day):
        await message.answer("Проверка пройдена", keyboard=main_keyboard())
        await state.finish()
    else:
        await message.answer("Написано же, выбери один из пунктов")


@dp.message_handler(state=Homework.get_option, text="Сегодня")
async def send_today_homework(message: Message, state: FSMContext):
    await message.answer("Проверка пройдена", keyboard=main_keyboard())
    await state.finish()


@dp.message_handler(state=Homework.get_option, text="Завтра")
async def send_next_day_homework(message: Message, state: FSMContext):
    await message.answer("Проверка пройдена", keyboard=main_keyboard())
    await state.finish()


@dp.message_handler(state=Homework.get_option, text="Эта неделя")
async def send_this_week_homework(message: Message, state: FSMContext):
    await message.answer("Проверка пройдена", keyboard=main_keyboard())
    await state.finish()


@dp.message_handler(state=Homework.get_option, text="Следующая неделя")
async def send_next_week_homework(message: Message, state: FSMContext):
    await message.answer("Следующая неделя", keyboard=main_keyboard())
    await state.finish()


@dp.message_handler(state=Homework.get_option, text="Все")
async def send_all_homework(message: Message, state: FSMContext):
    await message.answer("Все", keyboard=main_keyboard())
    await state.finish()


@dp.message_handler(state=Homework.get_option, regexp=".*")
async def homework_option_error(message: Message, state: FSMContext):
    await message.answer("Написано же, выбери один из пунктов")

