from loader import dp
from bot.types.message import Message


@dp.message_handler(text="Дз на завтра")
async def start_registration(message: Message):
    await message.answer("Тут будет вывод дз")



