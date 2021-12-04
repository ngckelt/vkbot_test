from loader import dp
from bot.states import FSMContext
from bot.types import Message
from keyboards.keyboards import homework_options_keyboard, main_keyboard
from states.students.homework import Homework
from database import HomeworksModel, StudentsModel
from .utils import correct_week_day, get_closest_week_day_date, get_future_date, get_today_date


async def collect_homeworks(student_vk_id, date=None):
    student = await StudentsModel.get_student_by_vk_id(student_vk_id)
    if date:
        homeworks = await HomeworksModel.get_homeworks_by_filters(group=student.group, date=date)
    else:
        homeworks = await HomeworksModel.get_homeworks_by_filters(group=student.group)
    text = ""
    if homeworks:
        for homework in homeworks:
            text += f"Предмет: {homework.subject}\nЗадание: {homework.text}\n\n"
    else:
        text = "Записей нет"
    return text


@dp.message_handler(text="Домашка")
async def send_homework_options(message: Message, state: FSMContext):
    await message.answer("Выбери нужный пункт", keyboard=homework_options_keyboard())
    await state.start()
    await state.set_state(Homework.get_option)


@dp.message_handler(state=Homework.get_option, regexp="^[а-яА-Яё -]{2}$")
async def get_homework_by_week_day(message: Message, state: FSMContext):
    week_day = message.text
    if correct_week_day(week_day):
        date = get_closest_week_day_date(week_day)
        homeworks = await collect_homeworks(message.user_id, date.date())
        await message.answer(homeworks, keyboard=main_keyboard())
        await state.finish()
    else:
        await message.answer("Написано же, выбери один из пунктов")


@dp.message_handler(state=Homework.get_option, text="Сегодня")
async def send_today_homework(message: Message, state: FSMContext):
    date = get_today_date()
    homeworks = await collect_homeworks(message.user_id, date.date())
    await message.answer(homeworks, keyboard=main_keyboard())
    await state.finish()


@dp.message_handler(state=Homework.get_option, text="Завтра")
async def send_next_day_homework(message: Message, state: FSMContext):
    date = get_future_date(1)
    homeworks = await collect_homeworks(message.user_id, date.date())
    await message.answer(homeworks, keyboard=main_keyboard())
    await state.finish()


@dp.message_handler(state=Homework.get_option, text="Эта неделя")
async def send_this_week_homework(message: Message, state: FSMContext):
    await message.answer("Эта неделя", keyboard=main_keyboard())
    await state.finish()


@dp.message_handler(state=Homework.get_option, text="Следующая неделя")
async def send_next_week_homework(message: Message, state: FSMContext):
    await message.answer("Следующая неделя", keyboard=main_keyboard())
    await state.finish()


@dp.message_handler(state=Homework.get_option, text="Все")
async def send_all_homework(message: Message, state: FSMContext):
    homeworks = await collect_homeworks(message.user_id)
    await message.answer(homeworks, keyboard=main_keyboard())
    await state.finish()


@dp.message_handler(state=Homework.get_option, regexp=".*")
async def homework_option_error(message: Message):
    await message.answer("Написано же, выбери один из пунктов")

