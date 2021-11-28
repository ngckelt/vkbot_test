from pprint import pprint
from dataclasses import dataclass
from web.homeworks.models import Homeworks
from datetime import datetime


@dataclass
class HomeworksObject:
    date: datetime


def get_homeworks_by_group(group):
    homeworks = dict()
    homework_objects = Homeworks.objects.filter(group=group).order_by('date')

    for homework in homework_objects:
        if homework.date not in homeworks.keys():
            homeworks[homework.date] = list()
        homeworks[homework.date].append(homework)

    data = list()
    for date, homework_objects in homeworks.items():
        homework_object = HomeworksObject(date)
        setattr(homework_object, "homeworks", homework_objects)
        setattr(homework_object, 'str_date', date.strftime(f"%d.%m.%Y %A, неделя: {date.isocalendar().week - 34}"))
        setattr(homework_object, 'str_date_input_format',  date.strftime("%Y-%m-%d"))
        data.append(homework_object)

    return data





