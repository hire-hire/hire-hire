from rest_framework import mixins, permissions, viewsets

from api_interview.serializers import (
    CategoryListSerializer,
    CategoryRetrieveSerializer,
    InterviewCreateSerializer,
    InterviewSerializer,
    LanguageSerializer,
    QuestionsAnswerSerializer,
)
from interview.models import Category, Interview, Language, Question


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
