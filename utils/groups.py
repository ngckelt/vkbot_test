from parser.get_groups import get_groups


def get_short_faculty_name(faculty_long_name):
    return {
        "Факультет автоматики и вычислительной техники": "АВТФ",
        "Факультет летательных аппаратов": "ФЛА",
        "Механико-технологический факультет": "МТФ",
        "Факультет мехатроники и автоматизации": "ФМА",
        "Факультет прикладной математики и информатики": "ФПМИ",
        "Факультет радиотехники и электроники": "РЭФ",
        "Физико-технический факультет": "ФТФ",
        "Факультет энергетики": "ФЭН",
        "Факультет бизнеса": "ФБ",
        "Факультет гуманитарного образования": "ФГО",
        "Заочное отделение института дистанционного обучения": "Заочное отделение института дистанционного обучения",
        "Институт дистанционного  обучения": "Институт дистанционного обучения",
        "Институт социальных технологий": "ИСТ"
    }.get(faculty_long_name)


def get_data_by_group(group):
    groups = get_groups()
    for faculty_name, faculty_data in groups.items():
        for course_number, groups_list in faculty_data.items():
            if group in groups_list:
                return get_short_faculty_name(faculty_name), course_number
