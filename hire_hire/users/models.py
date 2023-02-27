from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # email = models.EmailField('электронная почта', unique=True)
    is_duel_moderator = models.BooleanField(
        'признак модератора для дуэлей', default=False
    )

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
