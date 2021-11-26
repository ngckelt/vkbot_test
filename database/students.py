from web.students.models import *
from asgiref.sync import sync_to_async


class StudentsModel:

    @staticmethod
    @sync_to_async
    def add_student(vk_id, **data):
        student = Students.objects.create(vk_id=vk_id, **data)
        return student

    @staticmethod
    @sync_to_async
    def get_student_by_vk_id(student_vk_id):
        return Students.objects.filter(vk_id=student_vk_id).first()




