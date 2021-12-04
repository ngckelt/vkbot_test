import requests
import json
import re
import os
from bs4 import BeautifulSoup


def get_group_subjects(group):
    if os.path.exists(f"parser/schedule_{group}.json"):
        with open(f"parser/schedule_{group}.json", 'r') as f:
            data = json.loads(f.read())
            return data

    subjects = set()
    content = requests.get(f"https://www.nstu.ru/studies/schedule/schedule_classes/schedule?group={group}").text
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('div', class_='schedule__table-body')
    week_days = table.find_all('div', class_='schedule__table-row')
    for week_day in week_days:
        week_day_data = week_day.find_all('div', class_='schedule__table-row')
        for data in week_day_data:
            item = data.find('div', class_='schedule__table-item')
            data = item.text.replace('\t', '').replace('\xa0', '').split('\n')
            for i in data:
                if '·' in i:
                    subject = i.split('·')[0].strip()
                    if ';' in subject:
                        subject = subject.split(';')[0].strip()
                    subjects.add(subject.strip())
                elif not re.findall("[0-9]", i) and "," not in i and i.strip() not in (
                        "Лекция", "Практика", "Лабораторная",
                        "лыжная база", "спорткомплекс", "по нечётным",
                        "по чётным", ""):
                    subjects.add(i.strip())

    subjects = list(subjects)
    with open(f"parser/schedule_{group}.json", 'w') as f:
        f.write(json.dumps(list(subjects)))
    return subjects


