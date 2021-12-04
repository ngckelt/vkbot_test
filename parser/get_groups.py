import json
import requests
from bs4 import BeautifulSoup


def get_groups():
    with open('parser/groups_data.json', 'r') as f:
        data = json.loads(f.read())
    return data


def parse_groups():
    """
    :return:
    {
        "Факультет": {
            "Номер курса": [список групп],
            "Номер курса": [список групп]
        },
        "Факультет": {
            "Номер курса": [список групп],
            "Номер курса": [список групп]
        },
    }
    """
    groups = dict()
    content = requests.get('https://www.nstu.ru/studies/schedule/schedule_classes').text

    soup = BeautifulSoup(content, 'lxml')

    content = soup.find('div', class_='schedule__faculties-result')

    faculties = content.find_all('div', class_='schedule__faculty')

    for faculty in faculties:
        faculty_name = faculty.find('a', class_='schedule__faculty-title').text.replace('\n', '').replace('\t', '')
        groups[faculty_name] = dict()
        faculty_courses = faculty.find_all('div', class_='schedule__faculty-course')
        for course in faculty_courses:
            course_number = course.find('label', class_='schedule__faculty-course__title').find('span').text[0]
            if course_number not in groups[faculty_name].keys():
                groups[faculty_name][course_number] = list()
            course_groups = course.find_all('a', class_='schedule__faculty-groups__item')
            for group in course_groups:
                groups[faculty_name][course_number].append(group.text)

    with open('groups_data.json', 'w') as f:
        f.write(json.dumps(groups))
    return groups


if __name__ == '__main__':
    parse_groups()
