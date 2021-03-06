

class Message:

    def __init__(self, bot, user_id, text, timestamp):
        self.user_id = user_id
        self.text = text
        self.timestamp = timestamp
        self.bot = bot

    async def answer(self, text, keyboard=None) -> None:
        await self.bot.send_message(self.user_id, text, keyboard)

    async def answer_photo(self, photo_url):
        await self.bot.send_photo(self.user_id, photo_url)

    async def get_user(self):
        return await self.bot.get_user(self.user_id)



