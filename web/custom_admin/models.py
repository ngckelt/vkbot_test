from django.db import models
from django.contrib.auth.models import User
from web.students.models import Students


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student = models.ForeignKey(Students, verbose_name="Студент", on_delete=models.CASCADE)

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

