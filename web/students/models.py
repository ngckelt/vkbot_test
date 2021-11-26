from django.db import models


class Students(models.Model):
    vk_id = models.CharField("Вк ID", max_length=12)
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    faculty = models.CharField("Факультет", max_length=10)
    course = models.PositiveIntegerField("Курс", default=1)
    group = models.CharField("Группа", max_length=10)

    def __str__(self):
        return f"{self.faculty} | {self.course} | {self.group}"

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"




