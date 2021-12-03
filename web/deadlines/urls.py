from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import AddDeadlineView


urlpatterns = [
    path('add_deadline/', AddDeadlineView.as_view(), name='add_deadline'),
]



