from loader import dp
from bot.types import Message
from .utils import delete_deadlines
from bot.settings import ADMIN_VK_ID


@dp.message_handler(text="delete_deadlines")
async def _delete_deadlines(message: Message):
    if ADMIN_VK_ID == message.user_id:
        await message.answer("Удаление дедлайнов началась")
        await delete_deadlines()
        await message.answer("Удаление дедлайнов закончилась")
    else:
        await message.answer("Неизвестный запрос")

