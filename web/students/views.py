from django.shortcuts import render
from django.views import View


class StudentMainPageView(View):
    template_name = "students/student_main_page.html"

    def get(self, request):
        return render(request, self.template_name)



