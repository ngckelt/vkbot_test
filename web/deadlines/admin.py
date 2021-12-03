from django.contrib import admin
from .models import Deadlines


@admin.register(Deadlines)
class DeadlinesAdmin(admin.ModelAdmin):
    list_display = ['group', 'date']
    search_fields = ['group', 'date']

    class Meta:
        model = Deadlines


