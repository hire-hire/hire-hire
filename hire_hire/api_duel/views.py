from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiParameter,
    OpenApiResponse,
    OpenApiTypes,
    extend_schema,
    extend_schema_view,
)
from rest_framework import mixins, permissions, viewsets

from api_duel.permissions import IsDuelModerator
from api_duel.serializers import (
    DuelCreateSerializer,
    DuelPartialUpdateSerializer,
    DuelSerializer,
)
from duel.models import Duel
from hire_hire import schema


@extend_schema_view(
    create=extend_schema(
        tags=['Duels'],
        description='Создание дуэли',
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
                        schema.REQUIRED_ERROR_NAME,
                        summary=schema.REQUIRED_ERROR_SUMMARY,
                        description=schema.REQUIRED_ERROR_DESCR,
                        value={
                            'current_password': [schema.REQUIRED_FIELD],
                        },
                        response_only=False,
                    ),
                ],
            ),
            401: OpenApiResponse(
                response=DuelCreateSerializer,
                examples=[schema.not_authenticated],
            ),
            403: OpenApiResponse(
                response=DuelCreateSerializer,
                examples=[schema.forbidden_response_example],
            ),
        },
    ),
    retrieve=extend_schema(
        parameters=[
            OpenApiParameter('id', OpenApiTypes.INT, OpenApiParameter.PATH),
        ],
        tags=['Duels'],
        description='Получение конкретной дуэли',
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
                                'username': 'HdcIeCw.qnL-54L0lBKAybKeS',
                            },
                            'wrong_answers_count': 0,
                        },
                    ),
                ],
            ),
            401: OpenApiResponse(
                response=DuelSerializer,
                examples=[schema.not_authenticated],
            ),
            403: OpenApiResponse(
                response=DuelSerializer,
                examples=[schema.forbidden_response_example],
            ),
        }
    ),
    partial_update=extend_schema(
        tags=['Duels'],
        description='Получение конкретной дуэли',
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
                examples=[schema.not_authenticated],
            ),
            403: OpenApiResponse(
                response=DuelPartialUpdateSerializer,
                examples=[schema.forbidden_response_example],
            ),
            404: OpenApiResponse(
                response=DuelPartialUpdateSerializer,
                examples=[
                    schema.not_found,
                    OpenApiExample(
                        'question not found',
                        summary='Вопроса нет в дуэли',
                        description='Возвращает ошибку если совершена '
                                    'попытка отправить ответ на вопрос '
                                    'не из этой дуэли',
                        value=schema.not_found.value,
                        response_only=False,
                    ),
                    OpenApiExample(
                        'player not found',
                        summary='Игрока нет в дуэли',
                        description='Возвращает ошибку если совершена '
                                    'попытка отправить ответ от имени '
                                    'игрока не из этой дуэли',
                        value=schema.not_found.value,
                        response_only=False,
                    ),
                ],
            ),
        },
    ),
)
class DuelViewSet(
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (
        permissions.IsAuthenticated,
        IsDuelModerator,
    )
    http_method_names = ['get', 'post', 'patch']

    def get_queryset(self):
        if self.action == 'retrieve':
            return Duel.objects.filter_duel_by_user(
                duel_pk=self.kwargs.get('pk'),
                user=self.request.user,
            )
        return Duel.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return DuelCreateSerializer
        elif self.action == 'partial_update':
            return DuelPartialUpdateSerializer
        return DuelSerializer
