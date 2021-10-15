from loader import dp
from bot.types import Message


@dp.message_handler(text="Все дедлайны")
async def show_deadlines(message: Message):
    await message.answer("Тут будет вывод дедлайнов")



