from loader import dp
from bot.types import Message
from .utils import send_deadlines
from bot.settings import ADMIN_VK_ID


@dp.message_handler(text="send_deadlines")
async def _send_deadlines(message: Message):
    if ADMIN_VK_ID == message.user_id:
        await message.answer("Отправка дедлайнов началась")
        await send_deadlines()
        await message.answer("Отправка дедлайнов закончилась")
    else:
        await message.answer("Неизвестный запрос")

