from loader import dp
from bot.types import Message
from keyboards.keyboards import homework_options_keyboard


@dp.message_handler(text="debug")
async def echo(message: Message):
    await message.answer("debug", keyboard=homework_options_keyboard())
    # await message.answer_photo("photo218384941_457240419")
    # await message.answer_photo("photo-457240419")
    # await message.answer_photo("457240419")


