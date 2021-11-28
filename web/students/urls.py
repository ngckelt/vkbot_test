from django.urls import path
from .views import StudentMainPageView

urlpatterns = [
    path('', StudentMainPageView.as_view()),
    # path('', redirect_by_user_post),
    # path('login/', UserLoginView.as_view(), name="login"),
    # path('logout/', UserLogoutView.as_view(), name="logout"),
    # path('manager/', manager, name="manager"),
]

