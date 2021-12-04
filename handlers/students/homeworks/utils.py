import re
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


def correct_date(date):
    if re.match(r"^\d\d.\d\d.\d\d\d\d$", date):
        day, months, year = date.split('.')
        if int(day) in range(1, 32) and int(months) in range(1, 13) and int(year) in range(2021, 2023):
            date = datetime.strptime(date, "%d.%m.%Y")
            if date > datetime.now():
                return True
    return False



