from web.deadlines.models import Deadlines
from asgiref.sync import sync_to_async


class DeadlinesModel:

    @staticmethod
    @sync_to_async
    def get_deadlines_by_student_group(student_group):
        return Deadlines.objects.filter(group=student_group).order_by('date')

    @staticmethod
    @sync_to_async
    def add_deadline(text, group, date):
        Deadlines.objects.create(text=text, group=group, date=date)


