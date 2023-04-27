from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from users.validators import username_length_validator


class User(AbstractUser):
    username = models.CharField(
        'имя пользователя',
        max_length=25,
        unique=True,
        help_text='Обязательное поле. От 2 до 25 символов. '
                  'Буквы, цифры, @/./+/-/_ допускаются.',
        validators=[
            UnicodeUsernameValidator(),
            username_length_validator
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
