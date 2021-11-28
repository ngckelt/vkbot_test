from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return '/'


class UserLogoutView(LogoutView):
    next_page = "accounts/login/"



