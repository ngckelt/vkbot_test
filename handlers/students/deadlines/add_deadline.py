from loader import dp
from bot.types import Message
from bot.states import FSMContext
from states.students.deadlines import AddDeadline
from handlers.students.homeworks.utils import correct_date
from database import StudentsModel, DeadlinesModel
from datetime import datetime
from keyboards.keyboards import main_keyboard, empty_keyboard, home_keyboard


async def home(message, state):
    await message.answer("Основное меню", keyboard=main_keyboard())
    await state.finish()


@dp.message_handler(text="Добавить дедлайн")
async def add_deadline(message: Message, state: FSMContext):
    await state.start()
    await state.set_state(AddDeadline.get_text)
    await message.answer("Введи текст", keyboard=home_keyboard())


@dp.message_handler(state=AddDeadline.get_text)
async def get_deadline_text(message: Message, state: FSMContext):
    if message.text == "Домой":
        return await home(message, state)
    text = message.text
    await state.update_data(text=text)
    await state.set_state(AddDeadline.get_date)
    await message.answer("Введи дату в формате дд.мм.гггг", keyboard=home_keyboard())


@dp.message_handler(state=AddDeadline.get_date)
async def get_deadline_date(message: Message, state: FSMContext):
    if message.text == "Домой":
        return await home(message, state)
    date = message.text
    if correct_date(date):
        student = await StudentsModel.get_student_by_vk_id(message.user_id)
        state_data = await state.get_data()
        text = state_data.get('text')
        await DeadlinesModel.add_deadline(
            text=text,
            group=student.group,
            date=datetime.strptime(date, "%d.%m.%Y")
        )
        await state.finish()
        await message.answer("Дедлайн успешно добавлен", keyboard=main_keyboard())
    else:
        await message.answer("Неверная дата. Попробуй еще раз")
