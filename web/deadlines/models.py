from django.db import models


class Deadlines(models.Model):
    text = models.TextField("Текст")
    group = models.CharField("Группа", max_length=10)
    date = models.DateField("Дата")

    def __str__(self):
        return f"{self.group}|{self.date}"

    class Meta:
        verbose_name = "Дедлайн"
        verbose_name_plural = "Дедлайны"

