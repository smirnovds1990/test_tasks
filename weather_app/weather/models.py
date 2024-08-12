from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class City(models.Model):
    city_title = models.CharField(
        verbose_name='Название города',
        blank=False,
        null=False,
        max_length=100
    )
    user = models.ManyToManyField(
        User,
        related_name='cities',
        verbose_name='Пользователь',
        blank=False
    )
    request_date = models.DateTimeField(
        verbose_name='Дата запроса',
        auto_now_add=True
    )

    def __str__(self) -> str:
        return self.city_title
