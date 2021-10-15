from loader import bot, setup_django


if __name__ == '__main__':
    setup_django()
    from handlers import dp
    bot.start_polling(dp)

