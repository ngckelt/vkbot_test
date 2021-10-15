from django.contrib import admin
from . import models


@admin.register(models.Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'course', 'group']
    list_filter = ['course', 'group']

    class Meta:
        model = models.Students



