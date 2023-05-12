from drf_spectacular.extensions import OpenApiViewExtension
from drf_spectacular.utils import (
    extend_schema,
    OpenApiExample,
    OpenApiParameter,
    OpenApiResponse,
    OpenApiTypes,
)

from hire_hire.schema_settings import (
    forbidden_response_example,
    not_authenticated,
    not_found,
    REQUIRED_ERROR_DESCR,
    REQUIRED_ERROR_NAME,
    REQUIRED_ERROR_SUMMARY,
    REQUIRED_FIELD,
)


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
                                    'detail': 'Question is already answered!',
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
