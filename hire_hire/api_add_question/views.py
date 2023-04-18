import uuid

# from django.conf import settings
from rest_framework import viewsets

from add_question.models import AddQuestion
from api_add_question.serializers import AddQuestionSerializer


class AddQuestionViewSet(viewsets.ModelViewSet):
    queryset = AddQuestion.objects.all()
    serializer_class = AddQuestionSerializer

    def dispatch(self, request, *args, **kwargs):
        print('view dispatch!!!!!!!!!!!!!!!!!!!! здесь суём куки если надо')
        self.user_cookie = request.COOKIES.get('user_cookie')
        response = super().dispatch(request, *args, **kwargs)
        if not self.user_cookie:
            self.user_cookie = uuid.uuid4().hex
            # response = super().dispatch(request, *args, **kwargs)
            response.set_cookie('user_cookie', self.user_cookie)
        # else:
        #     response = super().dispatch(request, *args, **kwargs)
        return response

    # def get_serializer_context(self):
    #     print('view get_serializer_context!!!!!!!!!!!!!!!!!!!! здесь мы уже сунули add_questions_for24_count до создания вопроса в БД')
    #     context = super().get_serializer_context()
    #     print(context)
    #     context['add_questions_for24_count'] = (
    #         AddQuestion.objects.get_24_hours_added_question(self.request)
    #     )
    #     context[
    #         'limit_add_questions_per_day'
    #     ] = settings.LIMIT_ADD_QUESTIONS_PER_DAY
    #     # print(context)
    #     return context

    def perform_create(self, serializer):
        print('view perform_create!!!!!!!!!!!!!!!!!!!!! сохраняем вопрос в БД')
        instance = serializer.save()
        instance.ip_address = self.request.META.get('REMOTE_ADDR')
        if self.request.user.is_authenticated:
            instance.author = self.request.user
        else:
            instance.user_cookie = self.user_cookie
        instance.save()
