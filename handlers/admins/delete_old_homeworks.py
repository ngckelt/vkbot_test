from loader import dp
from bot.types import Message
from .utils import delete_homeworks
from bot.settings import ADMIN_VK_ID


@dp.message_handler(text="delete_homeworks")
async def _delete_homeworks(message: Message):
    if ADMIN_VK_ID == message.user_id:
        await message.answer("Удаление домашек началась")
        await delete_homeworks()
        await message.answer("Удаление домашек закончилась")
    else:
        await message.answer("Неизвестный запрос")

