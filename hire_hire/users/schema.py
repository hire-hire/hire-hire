from drf_spectacular.extensions import OpenApiViewExtension
from drf_spectacular.utils import (
    extend_schema,
    inline_serializer,
    OpenApiExample,
    OpenApiResponse,
)
from rest_framework.fields import CharField

from hire_hire.schema_settings import (
    FAKE_SERIALIZER_FIELDS,
    forbidden_response_example,
    INVALID_EMAIL_VALUE,
    INVALID_FIELD,
    INVALID_FIELD_DESCR,
    INVALID_TOKEN_EXAMPLE,
    JWT_TAG,
    not_authenticated,
    not_found,
    REQUIRED_ERROR_DESCR,
    REQUIRED_ERROR_NAME,
    REQUIRED_ERROR_SUMMARY,
    REQUIRED_FIELD,
    USERS_TAG,
    VALIDATION_ERROR_NAME,
)


class DjoserUsersView(OpenApiViewExtension):
    target_class = 'djoser.views.UserViewSet'

    def view_replacement(self):
        from djoser.serializers import UserSerializer

        class Extended(self.target_class):

            @extend_schema(exclude=True)
            def activation(self, request, *args, **kwargs):
                pass

            @extend_schema(exclude=True)
            def resend_activation(self, request, *args, **kwargs):
                pass

            @extend_schema(exclude=True)
            def reset_username(self, request, *args, **kwargs):
                pass

            @extend_schema(exclude=True)
            def reset_username_confirm(self, request, *args, **kwargs):
                pass

            @extend_schema(exclude=True)
            def reset_password(self, request, *args, **kwargs):
                pass

            @extend_schema(exclude=True)
            def reset_password_confirm(self, request, *args, **kwargs):
                pass

            @extend_schema(tags=['Users'])
            def me(self, request, *args, **kwargs):
                pass

            @extend_schema(
                description='Получение информации о пользователе',
                tags=[USERS_TAG],
                responses={
                    200: OpenApiResponse(response=UserSerializer),
                    401: OpenApiResponse(
                        response=UserSerializer,
                        examples=[not_authenticated],
                    ),
                    404: OpenApiResponse(
                        response=UserSerializer,
                        examples=[not_found],
                    ),
                },
            )
            def retrieve(self, request, *args, **kwargs):
                pass

            @extend_schema(
                description='Обновление конкретного пользователя',
                tags=[USERS_TAG],
                responses={
                    200: OpenApiResponse(response=UserSerializer),
                    400: OpenApiResponse(
                        response=UserSerializer,
                        examples=[
                            OpenApiExample(
                                VALIDATION_ERROR_NAME,
                                summary=INVALID_FIELD,
                                description=INVALID_FIELD_DESCR,
                                value=INVALID_EMAIL_VALUE,
                                response_only=False,
                            ),
                        ],
                    ),
                    401: OpenApiResponse(
                        response=UserSerializer,
                        examples=[not_authenticated],
                    ),
                    404: OpenApiResponse(
                        response=UserSerializer,
                        examples=[not_found],
                    ),
                },
            )
            def update(self, request, *args, **kwargs):
                pass

            @extend_schema(
                description='Обновление конкретного пользователя',
                tags=[USERS_TAG],
                responses={
                    200: OpenApiResponse(response=UserSerializer),
                    400: OpenApiResponse(
                        response=UserSerializer,
                        examples=[
                            OpenApiExample(
                                VALIDATION_ERROR_NAME,
                                summary=INVALID_FIELD,
                                description=INVALID_FIELD_DESCR,
                                value=INVALID_EMAIL_VALUE,
                                response_only=False,
                            ),
                        ],
                    ),
                    401: OpenApiResponse(
                        response=UserSerializer,
                        examples=[not_authenticated],
                    ),
                    404: OpenApiResponse(
                        response=UserSerializer,
                        examples=[not_found],
                    ),
                },
            )
            def partial_update(self, request, *args, **kwargs):
                pass

            @extend_schema(
                description='Получение списка пользователей',
                tags=[USERS_TAG],
                responses={
                    200: OpenApiResponse(response=UserSerializer),
                    401: OpenApiResponse(
                        response=UserSerializer,
                        examples=[not_authenticated],
                    )
                }
            )
            def list(self, request, *args, **kwargs):
                pass

            @extend_schema(
                description='Создание пользователя',
                tags=[USERS_TAG],
                responses={
                    201: OpenApiResponse(response=UserSerializer),
                    400: OpenApiResponse(
                        response=UserSerializer,
                        examples=[
                            OpenApiExample(
                                REQUIRED_ERROR_NAME,
                                summary=REQUIRED_ERROR_SUMMARY,
                                description=REQUIRED_ERROR_DESCR,
                                value={
                                    'username': [REQUIRED_FIELD],
                                    'password': [REQUIRED_FIELD],
                                },
                                response_only=False,
                            ),
                            OpenApiExample(
                                VALIDATION_ERROR_NAME,
                                summary=INVALID_FIELD,
                                description=INVALID_FIELD_DESCR,
                                value={
                                    'username': [
                                        'Введите правильное имя пользователя. '
                                        'Оно может содержать '
                                        'только латинские буквы, '
                                        'цифры и знаки @/./+/-/_.',
                                    ],
                                },
                                response_only=False,
                            ),
                            OpenApiExample(
                                'unique',
                                summary='Реквизит занят',
                                description='Возвращает список '
                                            'ошибок unique constraint',
                                value={
                                    'username': ['Имя пользователя занято'],
                                },
                                response_only=False,
                            ),
                        ],
                    ),
                    401: OpenApiResponse(
                        response=UserSerializer,
                        examples=[not_authenticated],
                    ),
                },
            )
            def create(self):
                pass

            @extend_schema(
                description='Удаление конкретного пользователя',
                tags=[USERS_TAG],
                responses={
                    204: OpenApiResponse(response=UserSerializer),
                    400: OpenApiResponse(
                        response=UserSerializer,
                        examples=[
                            OpenApiExample(
                                REQUIRED_ERROR_NAME,
                                summary=REQUIRED_ERROR_SUMMARY,
                                description=REQUIRED_ERROR_DESCR,
                                value={
                                    'current_password': [REQUIRED_FIELD],
                                },
                                response_only=False,
                            ),
                        ],
                    ),
                    401: OpenApiResponse(
                        response=UserSerializer,
                        examples=[not_authenticated],
                    ),
                    403: OpenApiResponse(
                        response=UserSerializer,
                        examples=[forbidden_response_example],
                    ),
                    404: OpenApiResponse(
                        response=UserSerializer,
                        examples=[not_found],
                    ),
                },
            )
            def destroy(self, request, *args, **kwargs):
                pass

            @extend_schema(
                description='Смена имени пользователя',
                tags=[USERS_TAG],
                responses={
                    204: OpenApiResponse(),
                    400: OpenApiResponse(
                        response=UserSerializer,
                        examples=[
                            OpenApiExample(
                                REQUIRED_ERROR_NAME,
                                summary=REQUIRED_ERROR_SUMMARY,
                                description=REQUIRED_ERROR_DESCR,
                                value={
                                    'current_password': [
                                        REQUIRED_FIELD,
                                    ],
                                    'new_username': [
                                        REQUIRED_FIELD,
                                    ]
                                },
                                response_only=False,
                            ),
                        ],
                    ),
                    401: OpenApiResponse(
                        response=UserSerializer,
                        examples=[not_authenticated],
                    ),
                    403: OpenApiResponse(
                        response=UserSerializer,
                        examples=[forbidden_response_example],
                    ),
                    404: OpenApiResponse(
                        response=UserSerializer,
                        examples=[not_found],
                    ),
                },
            )
            def set_username(self, request, *args, **kwargs):
                pass

            @extend_schema(
                description='Смена пароля',
                tags=[USERS_TAG],
                responses={
                    204: OpenApiResponse(),
                    400: OpenApiResponse(
                        response=UserSerializer,
                        examples=[
                            OpenApiExample(
                                REQUIRED_ERROR_NAME,
                                summary=REQUIRED_ERROR_SUMMARY,
                                description=REQUIRED_ERROR_DESCR,
                                value={
                                    'current_password': [
                                        REQUIRED_FIELD,
                                    ],
                                    'new_password': [
                                        REQUIRED_FIELD,
                                    ],
                                },
                                response_only=False,
                            ),
                        ],
                    ),
                    401: OpenApiResponse(
                        response=UserSerializer,
                        examples=[not_authenticated],
                    ),
                    403: OpenApiResponse(
                        response=UserSerializer,
                        examples=[forbidden_response_example],
                    ),
                    404: OpenApiResponse(
                        response=UserSerializer,
                        examples=[not_found],
                    ),
                },
            )
            def set_password(self, request, *args, **kwargs):
                pass

        return Extended


class JWTTokenObtainPairView(OpenApiViewExtension):
    target_class = 'rest_framework_simplejwt.views.TokenObtainPairView'

    def view_replacement(self):

        class Extended(self.target_class):
            @extend_schema(
                description='Получение токена',
                tags=[JWT_TAG],
                responses={
                    200: OpenApiResponse(
                        response=inline_serializer(
                            'ObtainSerializer',
                            {
                                'refresh': CharField(),
                                'access': CharField(),
                            },
                        ),
                    ),
                    400: OpenApiResponse(
                        response=inline_serializer(
                            'ObtainFakeSerializer',
                            FAKE_SERIALIZER_FIELDS),
                        examples=[
                            OpenApiExample(
                                REQUIRED_ERROR_NAME,
                                summary=REQUIRED_ERROR_SUMMARY,
                                description=REQUIRED_ERROR_DESCR,
                                value={
                                    'username': [
                                        REQUIRED_FIELD,
                                    ],
                                    'password': [
                                        REQUIRED_FIELD,
                                    ],
                                },
                                response_only=False,
                            ),
                        ],
                    ),
                    404: OpenApiResponse(
                        response=inline_serializer(
                            'Obtain404Serializer',
                            FAKE_SERIALIZER_FIELDS,
                        ),
                        examples=[not_found],
                    ),
                },
            )
            def post(self, request, *args, **kwargs):
                pass
        return Extended


class JWTTokenRefreshView(OpenApiViewExtension):
    target_class = 'rest_framework_simplejwt.views.TokenRefreshView'

    def view_replacement(self):

        class Extended(self.target_class):
            @extend_schema(
                description='Обновление токена',
                tags=[JWT_TAG],
                responses={
                    200: OpenApiResponse(
                        response=inline_serializer(
                            'RefreshSerializer',
                            {'access': CharField()}),
                    ),
                    400: OpenApiResponse(
                        response=inline_serializer(
                            'RefreshFakeSerializer',
                            FAKE_SERIALIZER_FIELDS,
                        ),
                        examples=[
                            OpenApiExample(
                                REQUIRED_ERROR_NAME,
                                summary=REQUIRED_ERROR_SUMMARY,
                                description=REQUIRED_ERROR_DESCR,
                                value={
                                    'refresh': [REQUIRED_FIELD],
                                },
                                response_only=False,
                            ),
                        ],
                    ),
                    401: OpenApiResponse(
                        response=inline_serializer(
                            'Refresh401Serializer',
                            FAKE_SERIALIZER_FIELDS
                        ),
                        examples=[
                            OpenApiExample(
                                'not_valid',
                                summary='Невалидный токен',
                                description='Возвращает ошибку '
                                            'о невалидности refresh-token',
                                value={
                                    'detail': 'Token is invalid or expired',
                                    'code': 'token_not_valid',
                                },
                                response_only=False,
                            ),
                        ],
                    ),
                },
            )
            def post(self, request, *args, **kwargs):
                pass
        return Extended


class JWTTokenVerifyView(OpenApiViewExtension):
    target_class = 'rest_framework_simplejwt.views.TokenVerifyView'

    def view_replacement(self):

        class Extended(self.target_class):
            @extend_schema(
                description='Обновление токена',
                tags=[JWT_TAG],
                responses={
                    200: OpenApiResponse(response={}),
                    400: OpenApiResponse(
                        response=inline_serializer(
                            'VerifyFakeSerializer',
                            FAKE_SERIALIZER_FIELDS),
                        examples=[INVALID_TOKEN_EXAMPLE],
                    ),
                    401: OpenApiResponse(
                        response=inline_serializer(
                            'Verify401Serializer',
                            FAKE_SERIALIZER_FIELDS,
                        ),
                        examples=[INVALID_TOKEN_EXAMPLE],
                    ),
                },
            )
            def post(self, request, *args, **kwargs):
                pass
        return Extended
