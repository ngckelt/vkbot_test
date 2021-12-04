from datetime import datetime, timedelta
from bot.settings import WEEK_DAYS


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


def correct_week_day(week_day):
    return week_day in WEEK_DAYS


def get_future_date(days):
    return datetime.now() + timedelta(days=days)


def get_today_date():
    return datetime.now()


def get_date_range():
    ...


def get_closest_week_day_date(week_day):
    days = 1
    date = datetime.now() + timedelta(days=days)
    while translate_week_day(week_day) != date.strftime("%a"):
        days += 1
        date = datetime.now() + timedelta(days=days)
    return date



