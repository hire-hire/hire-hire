from rest_framework import mixins, viewsets

from add_question.mixins import GetOrSetUserCookieMixin
from add_question.models import AddQuestion
from api_add_question.serializers import AddQuestionSerializer


class AddQuestionViewSet(
    GetOrSetUserCookieMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = AddQuestion.objects.all()
    serializer_class = AddQuestionSerializer

    def dispatch(self, request, *args, **kwargs):
        response = self.get_or_set_user_cookie(
            request,
            super().dispatch,
            *args,
            **kwargs,
        )
        return response

    def perform_create(self, serializer):
        user_data_dict = (
            dict(author=self.request.user)
            if self.request.user.is_authenticated
            else dict(user_cookie=self.user_cookie)
        )
        serializer.save(
            ip_address=self.request.META.get('REMOTE_ADDR'),
            **user_data_dict,
        )
