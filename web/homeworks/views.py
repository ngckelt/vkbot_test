from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import AddHomeworkForm
from .services import update_homework, delete_homework


class AddHomeworkView(View):

    def post(self, request):
        homework_data = {
            "subject": request.POST.get('subject'),
            "text": request.POST.get('text'),
            "date": request.POST.get('date'),
            "group":  request.user.userprofile.student.group
        }
        form = AddHomeworkForm(homework_data)
        if form.is_valid():
            form.save()
            messages.success(request, "Запись успешно добавлена", extra_tags='alert-success')
        else:
            messages.error(request, "Запись не была добавлена из-за некорректных данных", extra_tags="alert-danger")
        return redirect('/')


class UpdateHomeworkView(View):

    def post(self, request):
        homework_data = {
            "subject": request.POST.get('subject'),
            "text": request.POST.get('text'),
            "date": request.POST.get('date'),
            "group": request.user.userprofile.student.group
        }
        homework_id = request.POST.get('homework_id')
        form = AddHomeworkForm(homework_data)
        if form.is_valid():
            homework_data = form.cleaned_data
            update_homework(homework_id, request.user.userprofile.student.group, **homework_data)
            messages.success(request, "Запись успешно изменена", extra_tags='alert-success')
        else:
            messages.error(request, "Запись не была изменена из-за некорректных данных", extra_tags="alert-danger")
        return redirect('/')


class DeleteHomeworkView(View):

    def post(self, request):
        homework_id = request.POST.get('homework_id')
        delete_homework(homework_id, request.user.userprofile.student.group)
        messages.success(request, "Запись успешно удалена", extra_tags='alert-success')
        return redirect('/')

