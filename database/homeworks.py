from web.homeworks.models import Homeworks
from asgiref.sync import sync_to_async


class HomeworksModel:

    @staticmethod
    @sync_to_async
    def get_homeworks_by_student_group(student_group):
        return Homeworks.objects.filter(group=student_group).order_by('date')

    @staticmethod
    @sync_to_async
    def add_homework(subject, text, group, date):
        Homeworks.objects.create(subject=subject, text=text, group=group, date=date)

    @staticmethod
    @sync_to_async
    def get_homeworks_by_filters(**filters):
        return Homeworks.objects.filter(**filters).order_by('date')

    @staticmethod
    @sync_to_async
    def get_homeworks():
        return Homeworks.objects.all()
