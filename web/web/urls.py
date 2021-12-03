from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('web.accounts.urls')),
    path('homeworks/', include('web.homeworks.urls')),
    path('deadlines/', include('web.deadlines.urls')),
    path('', include('web.students.urls')),
]



