from web.homeworks.models import Homeworks


def update_homework(homework_id, student_group, **data):
    Homeworks.objects.filter(pk=homework_id, group=student_group).update(**data)


def delete_homework(homework_id, student_group):
    Homeworks.objects.filter(pk=homework_id, group=student_group).delete()



