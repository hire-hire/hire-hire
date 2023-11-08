from django.conf import settings
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from add_question.models import AddQuestion
from add_question.serializers import AddQuestionSerializer


class AddQuestionViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = AddQuestionSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AddedQuestionsAndLimitView(
    APIView,
):
    def get(self, request):
        return Response({
            'add_questions_for24_count': (
                AddQuestion.objects.get_24_hours_added_question_count(
                    request.user,
                )
            ),
            'limit_add_questions_per_day': (
                settings.LIMIT_ADD_QUESTIONS_PER_DAY,
            ),
        })
