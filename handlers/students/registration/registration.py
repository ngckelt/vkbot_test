from pprint import pprint

from loader import dp
from bot.types import Message
from bot.states import FSMContext
from states.students.registration import RegisterUser
from utils.groups import get_data_by_group

from database import StudentsModel


@dp.message_handler(text="начать")
async def start_registration(message: Message, state: FSMContext):
    student = await StudentsModel.get_student_by_vk_id(message.user_id)
    if student is None:
        await state.start()
        await state.set_state(RegisterUser.get_group)
        await message.answer("Привет! Укажи свою группу")
    else:
        await message.answer("Ты уже есть в базе")


@dp.message_handler(state=RegisterUser.get_group)
async def get_student_group(message: Message, state: FSMContext):
    group = message.text
    try:
        faculty_name, course_number = get_data_by_group(group)
        user = await message.get_user()
        student = await StudentsModel.add_student(
            vk_id=message.user_id,
            first_name=user.get('first_name'),
            last_name=user.get('last_name'),
            faculty=faculty_name,
            course=course_number,
            group=group
        )
        await message.answer("Отлично! Регистрация завершена")
        user_data = f"Vk id: {student.vk_id}\n" \
                    f"Имя: {student.first_name}\n" \
                    f"Фамилия: {student.last_name}\n" \
                    f"Факультет: {student.faculty}\n" \
                    f"Курс: {student.course}\n" \
                    f"Группа: {student.group}"
        await message.answer(f"Бот знает о тебе следующие данные: \n{user_data}")
        await state.finish()
    except:
        await message.answer("Такой группы не существует")


# @dp.message_handler(state=RegisterUser.get_first_name)
# async def get_first_name(message: Message, state: FSMContext):
#     first_name = message.text
#     await state.update_data(first_name=first_name)
#     await state.set_state(RegisterUser.get_last_name)
#     await message.answer("Какая у тебя фамилия?")
#
#
# @dp.message_handler(state=RegisterUser.get_last_name)
# async def get_last_name(message: Message, state: FSMContext):
#     last_name = message.text
#     await state.update_data(last_name=last_name)
#     await state.set_state(RegisterUser.get_course)
#     await message.answer("На каком курсе ты учишься?")
#
#
# @dp.message_handler(state=RegisterUser.get_course)
# async def get_course(message: Message, state: FSMContext):
#     course = message.text
#     await state.update_data(course=course)
#     await state.set_state(RegisterUser.get_group)
#     await message.answer("В какой группе ты учишься?")
#
#
# @dp.message_handler(state=RegisterUser.get_group)
# async def get_group(message: Message, state: FSMContext):
#     group = message.text
#     await state.update_data(group=group)
#     await state.set_state(RegisterUser.get_email)
#     await message.answer("Укажи свой email")
#
#
# @dp.message_handler(state=RegisterUser.get_email)
# async def get_email(message: Message, state: FSMContext):
#     email = message.text
#     await state.update_data(email=email)
#     await state.set_state(RegisterUser.get_phone)
#     await message.answer("Укажи свой номер телефона")
#
#
# @dp.message_handler(state=RegisterUser.get_phone)
# async def get_email(message: Message, state: FSMContext):
#     phone = message.text
#     await state.update_data(phone=phone)
#     await message.answer("Регистрация успешно завершена!")
#
#     state_data = await state.get_data()
#
#     StudentsModel.add_student(
#         student_vk_id=message.user_id,
#         first_name=state_data.get('first_name').capitalize(),
#         last_name=state_data.get('last_name').capitalize(),
#         course=state_data.get('course'),
#         group=state_data.get('group'),
#         email=state_data.get('email'),
#         phone=state_data.get('phone'),
#     )
#
#     await state.finish()





