import uuid

from rest_framework import mixins, viewsets

from add_question.models import AddQuestion
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
        self.user_cookie = request.COOKIES.get('user_cookie')
        response = super().dispatch(request, *args, **kwargs)
        if not self.user_cookie:
            self.user_cookie = uuid.uuid4().hex
            response.set_cookie('user_cookie', self.user_cookie)
        return response

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.ip_address = self.request.META.get('REMOTE_ADDR')
        if self.request.user.is_authenticated:
            instance.author = self.request.user
        else:
            instance.user_cookie = self.user_cookie
        instance.save()
