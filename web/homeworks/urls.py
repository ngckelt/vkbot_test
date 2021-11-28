from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import AddHomeworkView, UpdateHomeworkView, DeleteHomeworkView


urlpatterns = [
    path('add/', AddHomeworkView.as_view(), name='add_homework'),
    path('update/', UpdateHomeworkView.as_view(), name='update_homework'),
    path('delete/', DeleteHomeworkView.as_view(), name='delete_homework'),
]

