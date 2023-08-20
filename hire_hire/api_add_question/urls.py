from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api_add_question.views import (
    AddedQuestionsAndLimitView,
    AddQuestionViewSet,
)

app_name = 'api_add_question'

router_v1_add_question = DefaultRouter()

router_v1_add_question.register(
    r'add_question',
    AddQuestionViewSet,
    basename='add_question',
)

urlpatterns = [
    path('', include(router_v1_add_question.urls)),
    path(
        'added_questions_and_limit/',
        AddedQuestionsAndLimitView.as_view(),
        name='added_questions_and_limit',
    ),
]
