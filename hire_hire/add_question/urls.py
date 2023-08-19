from django.urls import include, path
from rest_framework.routers import DefaultRouter

from add_question.views import (
    AddedQestionsAndLimitView,
    AddQuestionViewSet,
)

app_name = 'add_question'

router_v1_add_question = DefaultRouter()

router_v1_add_question.register(
    r'add_question',
    AddQuestionViewSet,
    basename='add_question',
)

urlpatterns = [
    path('', include(router_v1_add_question.urls)),
    path(
        'added_qestions_and_limit/',
        AddedQestionsAndLimitView.as_view(),
        name='added_qestions_and_limit',
    ),
]
