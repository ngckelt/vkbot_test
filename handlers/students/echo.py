from loader import dp
from bot.types.message import Message


@dp.message_handler(regexp=".*")
async def echo(message: Message):
    await message.answer("Неизвестный запрос")
