from loader import dp
from bot.types import Message
from bot.states import FSMContext
from states.students.homework import AddHomework
from handlers.students.homeworks.utils import correct_date
from database import StudentsModel, HomeworksModel
from datetime import datetime
from parser.get_group_subjects import get_group_subjects
from keyboards.keyboards import main_keyboard, empty_keyboard, subject_keyboard, week_days_keyboard, home_keyboard
from .utils import correct_date, correct_week_day, get_closest_week_day_date


async def home(message, state):
    await message.answer("Основное меню", keyboard=main_keyboard())
    await state.finish()


@dp.message_handler(text="Добавить домашку")
async def start_add_homework(message: Message, state: FSMContext):
    student = await StudentsModel.get_student_by_vk_id(message.user_id)
    subjects = get_group_subjects(student.group)
    await state.start()
    await state.set_state(AddHomework.get_homework_subject)
    await state.update_data(subjects=subjects)
    await message.answer("Выбери предмет", keyboard=subject_keyboard(subjects))


@dp.message_handler(state=AddHomework.get_homework_subject)
async def get_subject(message: Message, state: FSMContext):
    if message.text == "Домой":
        return await home(message, state)
    subject_name = message.text
    s = None
    state_data = await state.get_data()
    subjects = state_data.get('subjects')
    for subject in subjects:
        if len(subject_name) == 40:  # max button str length
            if subject[:37] + '...' == subject_name:
                s = subject
                break
        else:
            if subject_name == subject:
                s = subject
                break
    if s is not None:
        await state.update_data(subject=s)
        await message.answer("Введи текст задания", keyboard=home_keyboard())
        await state.set_state(AddHomework.get_homework_text)
    else:
        await message.answer("Такого предмета не существует. Попробуй еще раз")


@dp.message_handler(state=AddHomework.get_homework_text)
async def get_homework_text(message: Message, state: FSMContext):
    if message.text == "Домой":
        return await home(message, state)
    text = message.text
    await state.update_data(text=text)
    await state.set_state(AddHomework.get_homework_date)
    await message.answer("Введи дату в формате дд.мм.гггг, либо выбери нужный день недели",
                         keyboard=week_days_keyboard())


async def add_homework(student_group, state: FSMContext):
    state_data = await state.get_data()
    subject = state_data.get('subject')
    text = state_data.get('text')
    date = state_data.get('date')
    date = datetime.strptime(date, "%d.%m.%Y")
    await HomeworksModel.add_homework(
        subject=subject,
        text=text,
        group=student_group,
        date=date.date()
    )


@dp.message_handler(state=AddHomework.get_homework_date, regexp="^[а-яА-Яё -]{2}$")
async def get_homework_date_by_week_day(message: Message, state: FSMContext):
    if message.text == "Домой":
        return await home(message, state)
    week_day = message.text
    if correct_week_day(week_day):
        student = await StudentsModel.get_student_by_vk_id(message.user_id)
        date = get_closest_week_day_date(week_day)
        await state.update_data(date=date.strftime("%d.%m.%Y"))
        await add_homework(student.group, state)
        await message.answer("Запись успешно добавлена", keyboard=main_keyboard())
        await state.finish()
    else:
        await message.answer("День недели указан неверно. Попробуй еще раз")


@dp.message_handler(state=AddHomework.get_homework_date)
async def get_homework_date(message: Message, state: FSMContext):
    if message.text == "Домой":
        return await home(message, state)
    str_date = message.text
    if correct_date(str_date):
        student = await StudentsModel.get_student_by_vk_id(message.user_id)
        await state.update_data(date=str_date)
        await add_homework(student.group, state)
        await message.answer("Запись успешно добавлена", keyboard=main_keyboard())
        await state.finish()
    else:
        await message.answer("Дата указана неверно. Попробуй еще раз")


