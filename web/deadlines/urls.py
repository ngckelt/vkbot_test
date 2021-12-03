from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import AddDeadlineView, UpdateDeadlineView, DeleteDeadlineView


urlpatterns = [
    path('add/', AddDeadlineView.as_view(), name='add_deadline'),
    path('update/', UpdateDeadlineView.as_view(), name='update_deadline'),
    path('delete/', DeleteDeadlineView.as_view(), name='delete_deadline'),
]



