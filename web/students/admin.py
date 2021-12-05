from django.contrib import admin
from .models import Students


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['vk_id', 'first_name', 'last_name', 'group']
    search_fields = ['group', 'first_name', 'last_name']
    list_filter = ['group']

    class Meta:
        model = Students


