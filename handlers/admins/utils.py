from loader import bot
from database import DeadlinesModel, StudentsModel, HomeworksModel
from handlers.students.deadlines.utils import get_delta_days
from datetime import datetime


async def send_deadline_to_group(deadline, delta_days):
    students = await StudentsModel.get_students_by_filters(group=deadline.group)
    student_ids = [student.vk_id for student in students]
    text = f"Напоминаю! Скоро дедлайн: {deadline.text}\nОсталось дней: {delta_days}"
    await bot.send_message(
        chat_id=student_ids,
        text=text
    )


async def send_deadlines():
    deadlines = await DeadlinesModel.get_deadlines()
    for deadline in deadlines:
        delta_days = get_delta_days(deadline.date, datetime.now().date())
        if delta_days in (7, 3, 1):
            await send_deadline_to_group(deadline, delta_days)


async def delete_homeworks():
    homeworks = await HomeworksModel.get_homeworks()
    for homework in homeworks:
        if homework.date < datetime.now().date():
            homework.delete()


async def delete_deadlines():
    deadlines = await DeadlinesModel.get_deadlines()
    for deadline in deadlines:
        if deadline.date < datetime.now().date():
            deadline.delete()






