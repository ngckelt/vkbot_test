from loader import dp
from bot.types import Message
from bot.keyboards import EmptyKeyboard


@dp.message_handler(text="debug")
async def echo(message: Message):
    await message.answer("Неизвестный запрос", keyboard=EmptyKeyboard())


