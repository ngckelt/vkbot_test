from loader import dp
from bot.types import Message
from keyboards.keyboards import homework_options_keyboard
from datetime import datetime, timedelta


def translate_week_day(week_day):
    return {
        "пн": "Mon",
        "вт": "Tue",
        "ср": "Wed",
        "чт": "Thu",
        "пт": "Fri",
        "сб": "Sat",
        "вс": "Sun",
    }.get(week_day)


@dp.message_handler(text="test")
async def echo(message: Message):
    week_day = 'чт'
    # current_date = datetime.now()
    days = 1
    date = datetime.now() + timedelta(days=days)
    while translate_week_day(week_day) != date.strftime("%a"):
        days += 1
        date =  datetime.now() + timedelta(days=days)
        print(date.strftime("%a"))
        if days == 7:
            break
    print(date)
    await message.answer("test")
    # await message.answer("debug", keyboard=homework_options_keyboard())
    # await message.answer_photo("photo218384941_457240419")
    # await message.answer_photo("photo-457240419")
    # await message.answer_photo("457240419")


