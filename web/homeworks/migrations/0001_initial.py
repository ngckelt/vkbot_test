# Generated by Django 3.1.8 on 2021-11-27 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homeworks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, verbose_name='Предмет')),
                ('text', models.TextField(verbose_name='Текст')),
                ('group', models.CharField(max_length=10, verbose_name='Группа')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Домашка',
                'verbose_name_plural': 'Домашки',
            },
        ),
    ]