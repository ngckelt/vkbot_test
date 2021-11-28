from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import StudentMainPageView


urlpatterns = [
    path('', login_required(StudentMainPageView.as_view()), name='student_main_page'),
]

