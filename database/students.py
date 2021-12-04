from web.students.models import Students
from asgiref.sync import sync_to_async


class StudentsModel:

    @staticmethod
    @sync_to_async
    def add_student(vk_id, **data):
        return Students.objects.create(vk_id=vk_id, **data)

    @staticmethod
    @sync_to_async
    def get_student_by_vk_id(vk_id):
        return Students.objects.filter(vk_id=vk_id).first()




