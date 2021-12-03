from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import AddDeadlineForm


class AddDeadlineView(View):

    def post(self, request):
        homework_data = {
            "text": request.POST.get('text'),
            "date": request.POST.get('date'),
            "group":  request.user.userprofile.student.group
        }
        form = AddDeadlineForm(homework_data)
        if form.is_valid():
            form.save()
            messages.success(request, "Дедлайн успешно добавлен", extra_tags='alert-success')
        else:
            messages.error(request, "Дедлайн не был добавлена из-за некорректных данных", extra_tags="alert-danger")
        return redirect('/')

#
# class UpdateHomeworkView(View):
#
#     def post(self, request):
#         homework_data = {
#             "subject": request.POST.get('subject'),
#             "text": request.POST.get('text'),
#             "date": request.POST.get('date'),
#             "group": request.user.userprofile.student.group
#         }
#         homework_id = request.POST.get('homework_id')
#         form = AddHomeworkForm(homework_data)
#         if form.is_valid():
#             homework_data = form.cleaned_data
#             update_homework(homework_id, request.user.userprofile.student.group, **homework_data)
#             messages.success(request, "Запись успешно изменена", extra_tags='alert-success')
#         else:
#             messages.error(request, "Запись не была изменена из-за некорректных данных", extra_tags="alert-danger")
#         return redirect('/')
#
#
# class DeleteHomeworkView(View):
#
#     def post(self, request):
#         homework_id = request.POST.get('homework_id')
#         delete_homework(homework_id, request.user.userprofile.student.group)
#         messages.success(request, "Запись успешно удалена", extra_tags='alert-success')
#         return redirect('/')
