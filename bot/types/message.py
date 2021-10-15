

class Message:

    def __init__(self, bot, user_id, text, timestamp):
        self.user_id = user_id
        self.text = text
        self.timestamp = timestamp
        self.bot = bot

    async def answer(self, text, keyboard=None) -> None:
        await self.bot.send_message(self.user_id, text, keyboard)


