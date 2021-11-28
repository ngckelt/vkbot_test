from django.db import models


class Homeworks(models.Model):
    subject = models.CharField("Предмет", max_length=255)
    text = models.TextField("Текст")
    group = models.CharField("Группа", max_length=10)
    date = models.DateField("Дата", null=True, blank=True)

    def __str__(self):
        return f"{self.subject}|{self.date}"

    class Meta:
        verbose_name = "Домашнее задание"
        verbose_name_plural = "Домашние задания"
