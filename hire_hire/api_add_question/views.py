from rest_framework import mixins, viewsets

from add_question.mixins import GetOrSetUserCookieIdMixin
from add_question.models import AddQuestion
from add_question.services import get_user_data_dict
from api_add_question.serializers import AddQuestionSerializer


class AddQuestionViewSet(
    GetOrSetUserCookieIdMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = AddQuestion.objects.all()
    serializer_class = AddQuestionSerializer

    def dispatch(self, request, *args, **kwargs):
        response = self.get_or_set_user_cookie_id(
            request,
            super().dispatch,
            *args,
            **kwargs,
        )
        return response

    def perform_create(self, serializer):
        serializer.save(
            ip_address=self.request.META.get('REMOTE_ADDR'),
            **get_user_data_dict(self.request.user, self.user_cookie_id),
        )
