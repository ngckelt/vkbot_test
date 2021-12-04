from loader import dp
from bot.types import Message
from bot.settings import SITE_URL


@dp.message_handler(text="Сайт")
async def start_add_homework(message: Message):
    await message.answer(f"Вот ссылка на сайт:\n{SITE_URL}")


