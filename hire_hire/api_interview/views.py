from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiParameter,
    OpenApiResponse,
    OpenApiTypes,
    extend_schema,
    extend_schema_view,
)
from rest_framework import mixins, permissions, viewsets

from api_interview.serializers import (
    CategoryListSerializer,
    CategoryRetrieveSerializer,
    InterviewCreateSerializer,
    InterviewSerializer,
    LanguageSerializer,
    QuestionsAnswerSerializer,
)
from hire_hire.schema import not_authenticated, not_found
from interview.models import Category, Interview, Language, Question


@extend_schema_view(
    list=extend_schema(
        tags=['Categories & Languages'],
        description='Список всех категорий',
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
    ),
    retrieve=extend_schema(
        tags=['Categories & Languages'],
        description='Информация по конкретной категории '
                    'со вложенными подкатегориями (языками)',
        request=CategoryRetrieveSerializer,
        responses={
            200: OpenApiResponse(
                response=CategoryRetrieveSerializer,
                examples=[
                    OpenApiExample(
                        '200',
                        summary='Валидный ответ',
                        description='Возвращает подробности по конкретной '
                                    'категории со вложенными языками',
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
    ),
)
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CategoryListSerializer
        return CategoryRetrieveSerializer


@extend_schema_view(
    list=extend_schema(
        tags=['Categories & Languages'],
        description='Список всех подкатегорий (языков)',
        request=CategoryListSerializer,
        responses=CategoryListSerializer,
    ),
    retrieve=extend_schema(
        tags=['Categories & Languages'],
        description='Информация по конкретной подкатегории (языку)',
        request=CategoryRetrieveSerializer,
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
    ),
)
class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


@extend_schema_view(
    create=extend_schema(
        tags=['Interview'],
        description='Создание нового интервью. Ждет количество вопросов',
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
    ),
    retrieve=extend_schema(
        parameters=[
            OpenApiParameter('id', OpenApiTypes.INT, OpenApiParameter.PATH),
        ],
        tags=['Interview'],
        description='Информация по конкретному интервью',
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
    ),
)
class InterviewViewset(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        if self.action == 'retrieve':
            return Interview.objects.get_interview_by_user(
                user=self.request.user,
                interview_pk=self.kwargs.get('pk'),
            )
        return Interview.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return InterviewCreateSerializer
        return InterviewSerializer


@extend_schema_view(
    retrieve=extend_schema(
        tags=['Interview'],
        description='Получение ответа на конкретный вопрос',
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
    ),
)
class QuestionAnswerViewset(
    mixins.RetrieveModelMixin, viewsets.GenericViewSet,
):
    serializer_class = QuestionsAnswerSerializer
    queryset = Question.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
