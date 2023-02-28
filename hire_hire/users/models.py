from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_duel_moderator = models.BooleanField(
        'признак модератора для дуэлей',
        default=False,
    )

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
