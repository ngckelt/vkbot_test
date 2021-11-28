from django.shortcuts import render
from django.views import View
from .srvices import get_homeworks_by_group


class StudentMainPageView(View):
    template_name = "students/student_main_page.html"

    def get(self, request):
        student = request.user.userprofile.student
        homeworks = get_homeworks_by_group(student.group)
        context = {
            "homework_objects": homeworks,
        }
        return render(request, self.template_name, context=context)



