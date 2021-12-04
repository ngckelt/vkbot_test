from loader import dp
from bot.types import Message
from bot.states import FSMContext
from states.students.registration import RegisterUser
from utils.groups import get_data_by_group
from keyboards.keyboards import main_keyboard
from database import StudentsModel


@dp.message_handler(text="Начать")
async def start_registration(message: Message, state: FSMContext):
    student = await StudentsModel.get_student_by_vk_id(message.user_id)
    if student is None:
        await state.start()
        await state.set_state(RegisterUser.get_group)
        await message.answer("Привет! Укажи свою группу")
    else:
        await message.answer("Ты уже есть в базе", keyboard=main_keyboard())


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
        await message.answer(f"Бот знает о тебе следующие данные: \n{user_data}", keyboard=main_keyboard())
        await state.finish()
    except:
        await message.answer("Такой группы не существует")





