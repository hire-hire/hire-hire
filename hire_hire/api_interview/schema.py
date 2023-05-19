from drf_spectacular.extensions import OpenApiViewExtension
from drf_spectacular.utils import (
    extend_schema,
    OpenApiExample,
    OpenApiParameter,
    OpenApiResponse,
    OpenApiTypes,
)

from hire_hire.schema_settings import not_authenticated, not_found


class CategoryView(OpenApiViewExtension):
    target_class = 'api_interview.views.CategoryViewSet'

    def view_replacement(self):
        from api_interview.serializers import (
            CategoryListSerializer, CategoryRetrieveSerializer,
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
                                            'category': 1,
                                        },
                                        {
                                            'id': 2,
                                            'title': 'javascript',
                                            'icon': 'какая-то иконка',
                                            'category': 1,
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
                responses=LanguageSerializer,
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
            InterviewCreateSerializer, InterviewSerializer,
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
                                        'допустимых вариантов.',
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
                        OpenApiParameter.PATH,
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
