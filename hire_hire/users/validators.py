from django.conf import settings
from django.core.exceptions import ValidationError


def username_length_validator(value):
    if len(value) < settings.USERNAME_MIN_LENGTH:
        raise ValidationError(
            'Имя пользователя не должно быть короче 2'
        )


class PasswordMaxLengthValidator:

    def __init__(self, max_length=settings.PASSWORD_MAX_LENGTH):
        self.max_length = max_length

    def validate(self, password, user=None):
        if len(password) > self.max_length:
            raise ValidationError(f'Пароль слишком длинный, '
                                  f'должно быть не более '
                                  f'{self.max_length} символов',)

    def get_help_text(self):
        return 'Пароль не должен быть длиннее 40 символов'
