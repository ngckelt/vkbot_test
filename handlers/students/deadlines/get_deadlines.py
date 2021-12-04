from loader import dp
from bot.types import Message
from database import StudentsModel, DeadlinesModel
from datetime import datetime
from .utils import get_delta_days


@dp.message_handler(text="Дедлайны")
async def show_deadlines(message: Message):
    student = await StudentsModel.get_student_by_vk_id(message.user_id)
    deadlines = await DeadlinesModel.get_deadlines_by_student_group(student.group)
    if deadlines:
        text = ""
        for deadline in deadlines:
            text += f"{deadline.text}\nДата: {deadline.date.strftime('%d.%m.%Y')}\n" \
                    f"Осталось дней: {get_delta_days(deadline.date, datetime.now().date())}\n\n"
        await message.answer(text)
    else:
        await message.answer("Дедлайнов нет")



