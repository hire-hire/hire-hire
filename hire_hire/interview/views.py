from rest_framework import mixins, permissions, viewsets

from interview.models import Category, Interview, Language, Question
from interview.serializers import (
    CategoryListSerializer,
    CategoryRetrieveSerializer,
    InterviewCreateSerializer,
    InterviewSerializer,
    LanguageSerializer,
    QuestionsRetrieveSerializer,
)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CategoryListSerializer
        return CategoryRetrieveSerializer


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


class InterviewViewSet(
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


class QuestionAnswerViewSet(
    mixins.RetrieveModelMixin, viewsets.GenericViewSet,
):
    serializer_class = QuestionsRetrieveSerializer
    queryset = Question.objects.get_question_with_answers_and_author()
    # permission_classes = (permissions.IsAuthenticated,)
