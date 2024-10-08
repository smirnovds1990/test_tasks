# Generated by Django 5.0.7 on 2024-07-24 10:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_title', models.CharField(max_length=100, verbose_name='Название города')),
                ('request_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата запроса')),
                ('user', models.ManyToManyField(related_name='cities', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
