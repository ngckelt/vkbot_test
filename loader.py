import asyncio
from os import environ
from django import setup

from bot import Bot
from bot.dispatcher import Dispatcher
from bot.settings import BOT_TOKEN

dp = Dispatcher()
bot = Bot(token=BOT_TOKEN)


def setup_django():
    environ.setdefault(
         'DJANGO_SETTINGS_MODULE',
         'web.web.settings',
    )
    environ.update({'DJANGO_ALLOW_ASYNC_UNSAFE': 'true'})
    setup()


def setup_bot():
    from handlers import dp
    bot.start_polling(dp)


