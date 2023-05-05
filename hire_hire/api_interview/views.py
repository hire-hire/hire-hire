from drf_spectacular.utils import OpenApiExample, OpenApiResponse, extend_schema, extend_schema_view
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
        description='',
        request=CategoryListSerializer,
        responses=CategoryListSerializer
    ),
    retrieve=extend_schema(
        tags=['Categories & Languages'],
        description='',
        request=CategoryRetrieveSerializer,
        responses={
            200: OpenApiResponse(response=CategoryRetrieveSerializer),
            400: OpenApiResponse(
                response=CategoryRetrieveSerializer,
                examples=[not_authenticated]
            ),
            404: OpenApiResponse(
                response=CategoryRetrieveSerializer,
                examples=[not_found]
            )
        }
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
        description='',
        request=CategoryListSerializer,
        responses=CategoryListSerializer
    ),
    retrieve=extend_schema(
        tags=['Categories & Languages'],
        description='',
        request=CategoryRetrieveSerializer,
        responses={
            200: OpenApiResponse(response=LanguageSerializer),
            400: OpenApiResponse(
                response=LanguageSerializer,
                examples=[not_authenticated]
            ),
            404: OpenApiResponse(
                response=LanguageSerializer,
                examples=[not_found]
            )
        }
    ),
)
class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


@extend_schema_view(
    create=extend_schema(
        tags=['Interview'],
        description='',
        request=InterviewCreateSerializer,
        responses={
            201: OpenApiResponse(response=InterviewSerializer),
            400: OpenApiResponse(
                response=InterviewSerializer,
                examples=[
                    not_authenticated,
                    OpenApiExample(
                        'invalid_question_count',
                        summary='Некорректное число вопросов',
                        description='Возвращает ошибку '
                                    'о несоответствии кол-ва вопросов допустимому',
                        value={
                            'question_count': [
                                'Значения N нет среди '
                                'допустимых вариантов.'
                            ]
                        },
                        response_only=False,
                    )
                ]
            ),
        }
    ),
    retrieve=extend_schema(
        tags=['Interview'],
        description='',
        request=InterviewSerializer,
        responses={
            200: OpenApiResponse(response=InterviewSerializer),
            400: OpenApiResponse(
                response=InterviewSerializer,
                examples=[not_authenticated]
            ),
            404: OpenApiResponse(
                response=InterviewSerializer,
                examples=[not_found]
            )
        }
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


class QuestionAnswerViewset(
    mixins.RetrieveModelMixin, viewsets.GenericViewSet,
):
    serializer_class = QuestionsAnswerSerializer
    queryset = Question.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
