from web.adminbot.models import *


class StudentsModel:

    @staticmethod
    def add_student(student_vk_id, **data):
        Students.objects.create(vk_id=student_vk_id, **data)

    @staticmethod
    def get_student_by_vk_id(student_vk_id):
        return Students.objects.filter(vk_id=student_vk_id).first()




