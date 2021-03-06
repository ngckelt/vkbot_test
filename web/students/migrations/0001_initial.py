# Generated by Django 3.1.8 on 2021-11-26 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vk_id', models.CharField(max_length=12, verbose_name='Вк ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('faculty', models.CharField(max_length=10, verbose_name='Факультет')),
                ('course', models.PositiveIntegerField(default=1, verbose_name='Курс')),
                ('group', models.CharField(max_length=10, verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
        ),
    ]
