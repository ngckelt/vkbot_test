from pprint import pprint

from bot.types import Message
from loader import dp

from keyboards.keyboards import yes_or_no_keyboard


@dp.message_handler(text="test")
async def test(message: Message):
    await message.answer(
        text="Тест с клавиатурой",
        keyboard=yes_or_no_keyboard()
    )





