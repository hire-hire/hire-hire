from rest_framework import mixins, viewsets

from add_question.models import AddQuestion
from add_question.services import get_or_set_user_cookie
from api_add_question.serializers import AddQuestionSerializer


class AddQuestionViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = AddQuestion.objects.all()
    serializer_class = AddQuestionSerializer

    def dispatch(self, request, *args, **kwargs):
        response = get_or_set_user_cookie(
            self, request, super().dispatch, *args, **kwargs
        )
        return response

    def perform_create(self, serializer):
        ip_address = self.request.META.get('REMOTE_ADDR')
        if self.request.user.is_authenticated:
            author = self.request.user
            user_cookie = None
        else:
            author = None
            user_cookie = self.user_cookie
        serializer.save(
            ip_address=ip_address,
            author=author,
            user_cookie=user_cookie,
        )
