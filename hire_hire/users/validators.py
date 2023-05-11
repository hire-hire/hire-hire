from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class PasswordMaxLengthValidator:

    def __init__(self, max_length=settings.PASSWORD_MAX_LENGTH):
        self.max_length = max_length

    def validate(self, password, user=None):
        if len(password) > self.max_length:
            raise ValidationError(f'Пароль слишком длинный, '
                                  f'должно быть не более '
                                  f'{self.max_length} символов',)

    def get_help_text(self):
        return f'Пароль не должен быть длиннее {self.max_length} символов'


class CustomUsernameValidator(RegexValidator):
    regex = r'^[\da-zA-Z.@+-_]+\Z'
    message = ('Введите правильное имя пользователя. Оно может содержать '
               'только латинские буквы, цифры и знаки @/./+/-/_')
