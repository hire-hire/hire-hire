from drf_spectacular.extensions import OpenApiViewExtension
from drf_spectacular.utils import (
    extend_schema,
    inline_serializer,
    OpenApiExample,
    OpenApiResponse,
    OpenApiParameter,
    OpenApiTypes,
)
from rest_framework.fields import CharField

INVALID_FIELD = 'Невалидное поле'
INVALID_FIELD_DESCR = 'Возвращает список ошибок валидации'
USERS_TAG = 'Users'
JWT_TAG = 'JWT'
VALIDATION_ERROR_NAME = 'validation'
REQUIRED_ERROR_NAME = 'required'
REQUIRED_ERROR_SUMMARY = 'Обязательные поля'
REQUIRED_ERROR_DESCR = 'Возвращает список незаполненных обязательных полей'
REQUIRED_FIELD = 'Обязательное поле.'
INVALID_EMAIL_VALUE = {
                          'email': [
                              'Введите правильный адрес электронной почты.'
                          ]
                      },
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
        'detail': 'Учетные данные не были предоставлены.'
    },
    response_only=False,
)

not_found = OpenApiExample(
    'not found',
    summary='Объект не найден',
    description='Возвращает ошибку если объект не существует',
    value={
        'detail': 'Страница не найдена.'
    },
    response_only=False,
)

forbidden_response_example = OpenApiExample(
    'forbidden',
    summary='Недостаточно прав',
    description='Возвращает ошибку если недостаточно прав',
    value={
        'detail': 'У вас недостаточно прав '
        'для выполнения данного действия.'
    },
    response_only=False,
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
                                        'цифры и знаки @/./+/-/_.'
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
                                    'username': ['Имя пользователя занято']
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
                                        REQUIRED_FIELD
                                    ],
                                    'new_username': [
                                        REQUIRED_FIELD
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
                                        REQUIRED_FIELD
                                    ],
                                    'new_password': [
                                        REQUIRED_FIELD
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
                                        REQUIRED_FIELD
                                    ],
                                    'password': [
                                        REQUIRED_FIELD
                                    ],
                                },
                                response_only=False,
                            ),
                        ],
                    ),
                    404: OpenApiResponse(
                        response=inline_serializer(
                            'Obtain404Serializer',
                            FAKE_SERIALIZER_FIELDS
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
                                    'refresh': [REQUIRED_FIELD]
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


class CategoryView(OpenApiViewExtension):
    target_class = 'api_interview.views.CategoryViewSet'

    def view_replacement(self):
        from api_interview.serializers import (
            CategoryListSerializer, CategoryRetrieveSerializer
        )

        class Extended(self.target_class):

            @extend_schema(
                description='Список всех категорий',
                tags=['Categories & Languages'],
                request=CategoryListSerializer,
                responses={
                    200: OpenApiResponse(
                        response=CategoryListSerializer,
                        examples=[
                            OpenApiExample(
                                '200',
                                summary='Валидный ответ',
                                description='Возвращает список категорий',
                                value={
                                    'id': 1,
                                    'title': 'Программирование',
                                    'icon': 'какой-то урл',
                                },
                            ),
                        ],
                    ),
                },
            )
            def list(self):
                pass

            @extend_schema(
                description='Информация по конкретной категории '
                            'со вложенными подкатегориями (языками)',
                tags=['Categories & Languages'],
                request=CategoryRetrieveSerializer,
                responses={
                    200: OpenApiResponse(
                        response=CategoryRetrieveSerializer,
                        examples=[
                            OpenApiExample(
                                '200',
                                summary='Валидный ответ',
                                description='Возвращает подробности '
                                            'по конкретной категории '
                                            'со вложенными языками',
                                value={
                                    'id': 1,
                                    'title': 'Программирование',
                                    'icon': 'какой-то урл',
                                    'lanuages': [
                                        {
                                            'id': 1,
                                            'title': 'python',
                                            'icon': 'какая-то иконка',
                                            'category': 1
                                        },
                                        {
                                            'id': 2,
                                            'title': 'javascript',
                                            'icon': 'какая-то иконка',
                                            'category': 1
                                        },
                                    ],
                                },
                                response_only=False,
                            ),
                        ]
                    ),
                    401: OpenApiResponse(
                        response=CategoryRetrieveSerializer,
                        examples=[not_authenticated],
                    ),
                    404: OpenApiResponse(
                        response=CategoryRetrieveSerializer,
                        examples=[not_found],
                    ),
                },
            )
            def retrieve(self):
                pass

        return Extended


class LanguageView(OpenApiViewExtension):
    target_class = 'api_interview.views.LanguageViewSet'

    def view_replacement(self):
        from api_interview.serializers import LanguageSerializer

        class Extended(self.target_class):

            @extend_schema(
                description='Список всех подкатегорий (языков)',
                tags=['Categories & Languages'],
                request=LanguageSerializer,
                responses=LanguageSerializer
            )
            def list(self):
                pass

            @extend_schema(
                description='Информация по конкретной подкатегории (языку)',
                tags=['Categories & Languages'],
                request=LanguageSerializer,
                responses={
                    200: OpenApiResponse(response=LanguageSerializer),
                    401: OpenApiResponse(
                        response=LanguageSerializer,
                        examples=[not_authenticated],
                    ),
                    404: OpenApiResponse(
                        response=LanguageSerializer,
                        examples=[not_found],
                    ),
                },
            )
            def retrieve(self):
                pass

        return Extended


class InterviewView(OpenApiViewExtension):
    target_class = 'api_interview.views.InterviewViewset'

    def view_replacement(self):
        from api_interview.serializers import (
            InterviewCreateSerializer, InterviewSerializer
        )

        class Extended(self.target_class):

            @extend_schema(
                description='Создание нового интервью. '
                            'Ждет количество вопросов',
                tags=['Interview'],
                request=InterviewCreateSerializer,
                responses={
                    201: OpenApiResponse(response=InterviewSerializer),
                    400: OpenApiResponse(
                        response=InterviewSerializer,
                        examples=[
                            OpenApiExample(
                                'invalid_question_count',
                                summary='Некорректное число вопросов',
                                description='Возвращает ошибку '
                                            'о несоответствии кол-ва '
                                            'вопросов допустимому',
                                value={
                                    'question_count': [
                                        'Значения N нет среди '
                                        'допустимых вариантов.'
                                    ],
                                },
                                response_only=False,
                            ),
                        ],
                    ),
                    401: OpenApiResponse(
                        response=InterviewSerializer,
                        examples=[not_authenticated],
                    ),
                },
            )
            def create(self):
                pass

            @extend_schema(
                parameters=[
                    OpenApiParameter(
                        'id',
                        OpenApiTypes.INT,
                        OpenApiParameter.PATH
                    ),
                ],
                description='Информация по конкретному интервью',
                tags=['Interview'],
                request=InterviewSerializer,
                responses={
                    200: OpenApiResponse(response=InterviewSerializer),
                    401: OpenApiResponse(
                        response=InterviewSerializer,
                        examples=[not_authenticated],
                    ),
                    404: OpenApiResponse(
                        response=InterviewSerializer,
                        examples=[not_found],
                    ),
                },
            )
            def retrieve(self):
                pass

        return Extended


class QuestionAnswerView(OpenApiViewExtension):
    target_class = 'api_interview.views.QuestionAnswerViewset'

    def view_replacement(self):
        from api_interview.serializers import QuestionsAnswerSerializer

        class Extended(self.target_class):

            @extend_schema(
                description='Получение ответа на конкретный вопрос',
                tags=['Interview'],
                request=QuestionsAnswerSerializer,
                responses={
                    200: OpenApiResponse(response=QuestionsAnswerSerializer),
                    401: OpenApiResponse(
                        response=QuestionsAnswerSerializer,
                        examples=[not_authenticated],
                    ),
                    404: OpenApiResponse(
                        response=QuestionsAnswerSerializer,
                        examples=[not_found],
                    ),
                },
            )
            def retrieve(self):
                pass

        return Extended


class ContributorsView(OpenApiViewExtension):
    target_class = 'api_contributors.views.ContributorsListViewSet'

    def view_replacement(self):
        from api_contributors.serializers import ContributorSerializer

        class Extended(self.target_class):

            @extend_schema(
                description='Список участников команды с ролями',
                tags=['Contributors'],
                request=ContributorSerializer,
                responses={
                    200: OpenApiResponse(
                        response=ContributorSerializer,
                        examples=[
                            OpenApiExample(
                                'valid_result',
                                summary='Валидный результат',
                                description='Возвращает ошибку '
                                            'о несоответствии кол-ва '
                                            'вопросов допустимому',
                                value={
                                    'first_name': 'кукла',
                                    'last_name': 'колдуна',
                                    'middle_name': 'кишовна',
                                    'photo': 'урл какой-то фотки',
                                    'role': 'мужик',
                                    'contacts': [
                                        {
                                            'social_network': 'сеть1',
                                            'contact': 'http://ya.ru'
                                        }
                                    ]
                                },
                                response_only=False,
                            ),
                        ],
                    ),
                },
            )
            def list(self):
                pass

            @extend_schema(
                description='Информация по конкретному интервью',
                tags=['Contributors'],
                request=ContributorSerializer,
                responses={
                    200: OpenApiResponse(response=ContributorSerializer),
                    404: OpenApiResponse(
                        response=ContributorSerializer,
                        examples=[not_found],
                    ),
                },
            )
            def retrieve(self):
                pass

        return Extended


class DuelView(OpenApiViewExtension):
    target_class = 'api_duel.views.DuelViewSet'

    def view_replacement(self):
        from api_duel.serializers import (
            DuelCreateSerializer, DuelPartialUpdateSerializer, DuelSerializer
        )

        class Extended(self.target_class):

            @extend_schema(
                description='Создание дуэли',
                tags=['Duels'],
                request=DuelCreateSerializer,
                responses={
                    201: OpenApiResponse(
                        response=DuelCreateSerializer,
                        examples=[
                            OpenApiExample(
                                '201',
                                summary='Валидный ответ',
                                description='Возвращает созданную дуэль',
                                value={
                                    'question_count': 10,
                                    'players': [
                                        {
                                            'name': 'player1',
                                            'good_answers_count': 0,
                                        },
                                        {
                                            'name': 'player2',
                                            'good_answers_count': 0,
                                        },
                                    ],
                                },
                            ),
                        ],
                    ),
                    400: OpenApiResponse(
                        response=DuelCreateSerializer,
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
                        response=DuelCreateSerializer,
                        examples=[not_authenticated],
                    ),
                    403: OpenApiResponse(
                        response=DuelCreateSerializer,
                        examples=[forbidden_response_example],
                    ),
                },
            )
            def create(self):
                pass

            @extend_schema(
                parameters=[
                    OpenApiParameter(
                        'id',
                        OpenApiTypes.INT,
                        OpenApiParameter.PATH
                    ),
                ],
                description='Получение конкретной дуэли',
                tags=['Duels'],
                request=DuelSerializer,
                responses={
                    200: OpenApiResponse(
                        response=DuelSerializer,
                        examples=[
                            OpenApiExample(
                                '200',
                                summary='Валидный ответ',
                                description='Возвращает созданную дуэль',
                                value={
                                    'id': 0,
                                    'questions': [
                                        {
                                            'id': 0,
                                            'question': {
                                                'id': 0,
                                                'text': 'string',
                                            },
                                        },
                                    ],
                                    'players': [
                                        {
                                            'id': 0,
                                            'name': 'string',
                                            'good_answers_count': 0,
                                        },
                                    ],
                                    'owner': {
                                        'id': 0,
                                        'username': '0lBKAybKeS',
                                    },
                                    'wrong_answers_count': 0,
                                },
                            ),
                        ],
                    ),
                    401: OpenApiResponse(
                        response=DuelSerializer,
                        examples=[not_authenticated],
                    ),
                    403: OpenApiResponse(
                        response=DuelSerializer,
                        examples=[forbidden_response_example],
                    ),
                }
            )
            def retrieve(self):
                pass

            @extend_schema(
                description='Получение конкретной дуэли',
                tags=['Duels'],
                request=DuelPartialUpdateSerializer,
                responses={
                    200: OpenApiResponse(
                        response=DuelPartialUpdateSerializer,
                        examples=[
                            OpenApiExample(
                                '200',
                                summary='Валидный ответ',
                                description='Возвращает созданную дуэль',
                                value={
                                    'wrong_answers_count': 0,
                                    'players': [
                                        {
                                            'id': 1,
                                            'name': 'player1',
                                            'good_answers_count': 2,
                                        },
                                        {
                                            'id': 2,
                                            'name': 'player2',
                                            'good_answers_count': 0,
                                        },
                                    ],
                                },
                            ),
                        ],
                    ),
                    400: OpenApiResponse(
                        response=DuelPartialUpdateSerializer,
                        examples=[
                            OpenApiExample(
                                'question_answered',
                                summary='Уже отвеченный вопрос',
                                description='Возвращает ошибку о том, '
                                            'что ответ на вопрос уже был дан',
                                value={
                                    'detail': 'Question is already answered!'
                                },
                            ),
                        ],
                    ),
                    401: OpenApiResponse(
                        response=DuelPartialUpdateSerializer,
                        examples=[not_authenticated],
                    ),
                    403: OpenApiResponse(
                        response=DuelPartialUpdateSerializer,
                        examples=[forbidden_response_example],
                    ),
                    404: OpenApiResponse(
                        response=DuelPartialUpdateSerializer,
                        examples=[
                            not_found,
                            OpenApiExample(
                                'question not found',
                                summary='Вопроса нет в дуэли',
                                description='Возвращает ошибку если совершена '
                                            'попытка отправить ответ '
                                            'на вопрос не из этой дуэли',
                                value=not_found.value,
                                response_only=False,
                            ),
                            OpenApiExample(
                                'player not found',
                                summary='Игрока нет в дуэли',
                                description='Возвращает ошибку если совершена '
                                            'попытка отправить ответ от имени '
                                            'игрока не из этой дуэли',
                                value=not_found.value,
                                response_only=False,
                            ),
                        ],
                    ),
                },
            )
            def partial_update(self):
                pass

        return Extended
