from web.deadlines.models import Deadlines


def update_deadline(deadline_id, student_group, **data):
    Deadlines.objects.filter(pk=deadline_id, group=student_group).update(**data)


def delete_deadline(deadline_id, student_group):
    Deadlines.objects.filter(pk=deadline_id, group=student_group).delete()

