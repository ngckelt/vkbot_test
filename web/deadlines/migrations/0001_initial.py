# Generated by Django 3.1.8 on 2021-12-03 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deadlines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('group', models.CharField(max_length=10, verbose_name='Группа')),
                ('date', models.DateField(verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Дедлайн',
                'verbose_name_plural': 'Дедлайны',
            },
        ),
    ]
