from django.contrib.auth.models import User
from web.custom_admin.models import UserProfile
from django.contrib.auth.hashers import make_password
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

    @staticmethod
    @sync_to_async
    def create_site_account(student, username, password):
        user = User.objects.create(username=username, password=make_password(password), email="",
                                        first_name=student.first_name, last_name=student.last_name)
        UserProfile.objects.create(user=user, student=student)



