from django.conf import settings
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from add_question.mixins import GetOrSetUserCookieIdMixin
from add_question.models import AddQuestion
from add_question.services import get_user_data_dict
from api_add_question.serializers import AddQuestionSerializer


class AddQuestionViewSet(
    GetOrSetUserCookieIdMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = AddQuestion.objects.all()
    serializer_class = AddQuestionSerializer

    def perform_create(self, serializer):
        serializer.save(
            ip_address=self.request.META.get('REMOTE_ADDR'),
            **get_user_data_dict(self.request.user, self.user_cookie_id),
        )

    def create(self, request, *args, **kwargs):
        remaining_question_limit = (
            settings.LIMIT_ADD_QUESTIONS_PER_DAY
            - AddQuestion.objects.get_24_hours_added_question_count(
                request.user,
                self.user_cookie_id,
            )
        )
        serializer = self.get_serializer(
            data=request.data,
            many=True,
            max_length=remaining_question_limit,
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )


class AddedQestionsAndLimitView(
    GetOrSetUserCookieIdMixin,
    APIView,
):
    def get(self, request):
        data = {
            'add_questions_for24_count': (
                AddQuestion.objects.get_24_hours_added_question_count(
                    request.user,
                    self.user_cookie_id,
                )
            ),
            'limit_add_questions_per_day': (
                settings.LIMIT_ADD_QUESTIONS_PER_DAY
            ),
        }
        return Response(data)
