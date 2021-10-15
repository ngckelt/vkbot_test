from django.db import models


class Students(models.Model):
    vk_id = models.PositiveIntegerField(verbose_name="ВК id")
    first_name = models.CharField(verbose_name="Имя", max_length=255)
    last_name = models.CharField(verbose_name="Фамилия", max_length=255)
    course = models.PositiveIntegerField(verbose_name="Курс")
    group = models.CharField(verbose_name="Группа", max_length=255)
    email = models.CharField(verbose_name="Email", max_length=255)
    phone = models.CharField(verbose_name="Телефон", max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"



