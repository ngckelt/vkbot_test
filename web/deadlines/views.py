from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import AddDeadlineForm
from .services import update_deadline, delete_deadline


class AddDeadlineView(View):

    def post(self, request):
        deadline_data = {
            "text": request.POST.get('text'),
            "date": request.POST.get('date'),
            "group":  request.user.userprofile.student.group
        }
        form = AddDeadlineForm(deadline_data)
        if form.is_valid():
            form.save()
            messages.success(request, "Дедлайн успешно добавлен", extra_tags='alert-success')
        else:
            messages.error(request, "Дедлайн не был добавлена из-за некорректных данных", extra_tags="alert-danger")
        return redirect('/')


class UpdateDeadlineView(View):

    def post(self, request):
        deadline_data = {
            "text": request.POST.get('text'),
            "date": request.POST.get('date'),
            "group": request.user.userprofile.student.group
        }
        deadline_id = request.POST.get('deadline_id')
        form = AddDeadlineForm(deadline_data)
        if form.is_valid():
            deadline_data = form.cleaned_data
            update_deadline(deadline_id, request.user.userprofile.student.group, **deadline_data)
            messages.success(request, "Дедлайн успешно изменен", extra_tags='alert-success')
        else:
            messages.error(request, "Дедлайн не был добавлен из-за некорректных данных", extra_tags="alert-danger")
        return redirect('/')


class DeleteDeadlineView(View):

    def post(self, request):
        deadline_id = request.POST.get('deadline_id')
        delete_deadline(deadline_id, request.user.userprofile.student.group)
        messages.success(request, "Дедлайн успешно изменен", extra_tags='alert-success')
        return redirect('/')
