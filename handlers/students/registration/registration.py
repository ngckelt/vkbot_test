from pprint import pprint

from loader import dp
from bot.types import Message
from bot.states import FSMContext
from states.students.registration import RegisterUser

from db_api.db import StudentsModel


@dp.message_handler(text="начать")
async def start_registration(message: Message, state: FSMContext):
    student = StudentsModel.get_student_by_vk_id(message.user_id)
    if student is None:
        await state.start()
        await state.set_state(RegisterUser.get_first_name)
        await message.answer("Привет! Как тебя зовту?")
    else:
        await message.answer("Ты уже есть в базе")


@dp.message_handler(state=RegisterUser.get_first_name)
async def get_first_name(message: Message, state: FSMContext):
    first_name = message.text
    await state.update_data(first_name=first_name)
    await state.set_state(RegisterUser.get_last_name)
    await message.answer("Какая у тебя фамилия?")


@dp.message_handler(state=RegisterUser.get_last_name)
async def get_last_name(message: Message, state: FSMContext):
    last_name = message.text
    await state.update_data(last_name=last_name)
    await state.set_state(RegisterUser.get_course)
    await message.answer("На каком курсе ты учишься?")


@dp.message_handler(state=RegisterUser.get_course)
async def get_course(message: Message, state: FSMContext):
    course = message.text
    await state.update_data(course=course)
    await state.set_state(RegisterUser.get_group)
    await message.answer("В какой группе ты учишься?")


@dp.message_handler(state=RegisterUser.get_group)
async def get_group(message: Message, state: FSMContext):
    group = message.text
    await state.update_data(group=group)
    await state.set_state(RegisterUser.get_email)
    await message.answer("Укажи свой email")


@dp.message_handler(state=RegisterUser.get_email)
async def get_email(message: Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await state.set_state(RegisterUser.get_phone)
    await message.answer("Укажи свой номер телефона")


@dp.message_handler(state=RegisterUser.get_phone)
async def get_email(message: Message, state: FSMContext):
    phone = message.text
    await state.update_data(phone=phone)
    await message.answer("Регистрация успешно завершена!")

    state_data = await state.get_data()

    StudentsModel.add_student(
        student_vk_id=message.user_id,
        first_name=state_data.get('first_name').capitalize(),
        last_name=state_data.get('last_name').capitalize(),
        course=state_data.get('course'),
        group=state_data.get('group'),
        email=state_data.get('email'),
        phone=state_data.get('phone'),
    )

    await state.finish()





