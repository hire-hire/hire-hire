from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

from users.validators import CustomUsernameValidator


class User(AbstractUser):
    username = models.CharField(
        'имя пользователя',
        max_length=settings.USERNAME_MAX_LENGTH,
        unique=True,
        help_text=f'Обязательное поле. От {settings.USERNAME_MIN_LENGTH} '
                  f'до {settings.USERNAME_MAX_LENGTH} символов. '
                  'Буквы, цифры, @/./+/-/_ допускаются.',
        validators=[
            CustomUsernameValidator(),
            MinLengthValidator(settings.USERNAME_MIN_LENGTH),
        ],
        error_messages={
            'unique': 'Имя пользователя занято',
        },
    )
    is_duel_moderator = models.BooleanField(
        'признак модератора для дуэлей',
        default=False,
    )

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
