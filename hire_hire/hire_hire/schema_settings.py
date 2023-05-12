from drf_spectacular.utils import OpenApiExample
from rest_framework.fields import CharField

INVALID_FIELD = 'Невалидное поле'
INVALID_FIELD_DESCR = 'Возвращает список ошибок валидации'
USERS_TAG = 'Users'
JWT_TAG = 'JWT'
VALIDATION_ERROR_NAME = 'validation'
REQUIRED_ERROR_NAME = 'required'
REQUIRED_ERROR_SUMMARY = 'Обязательные поля'
REQUIRED_ERROR_DESCR = 'Возвращает список незаполненных обязательных полей'
REQUIRED_FIELD = 'Обязательное поле'
INVALID_EMAIL_VALUE = {'email': [
    'Введите правильный адрес электронной почты.',
]},
INVALID_TOKEN_EXAMPLE = OpenApiExample(
    'not_valid',
    summary='Невалидный токен',
    description='Возвращает ошибку о невалидности refresh-token',
    value={
        'detail': 'Token is invalid or expired',
        'code': 'token_not_valid',
    },
    response_only=False,
)
FAKE_SERIALIZER_FIELDS = {'somefield': CharField()}


not_authenticated = OpenApiExample(
    '401',
    summary='Не авторизован',
    description='Возвращает ошибку аутентификации',
    value={
        'detail': 'Учетные данные не были предоставлены.',
    },
    response_only=False,
)

not_found = OpenApiExample(
    'not found',
    summary='Объект не найден',
    description='Возвращает ошибку если объект не существует',
    value={
        'detail': 'Страница не найдена.',
    },
    response_only=False,
)

forbidden_response_example = OpenApiExample(
    'forbidden',
    summary='Недостаточно прав',
    description='Возвращает ошибку если недостаточно прав',
    value={
        'detail': 'У вас недостаточно прав '
        'для выполнения данного действия.',
    },
    response_only=False,
)
