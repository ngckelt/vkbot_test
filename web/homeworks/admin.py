from django.contrib import admin
from .models import Homeworks


@admin.register(Homeworks)
class HomeworksAdmin(admin.ModelAdmin):
    list_display = ['subject', 'group', 'date']
    search_fields = ['subject', 'group']

    class Meta:
        model = Homeworks

