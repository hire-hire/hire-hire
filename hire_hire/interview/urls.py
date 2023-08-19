from django.urls import include, path
from rest_framework.routers import DefaultRouter

from interview.views import (
    CategoryViewSet,
    InterviewViewSet,
    LanguageViewSet,
    QuestionAnswerViewSet,
)

router_v1_interview = DefaultRouter()

router_v1_interview.register(
    r'category',
    CategoryViewSet,
    basename='category',
)
router_v1_interview.register(
    r'language',
    LanguageViewSet,
    basename='language',
)
router_v1_interview.register(
    r'interview',
    InterviewViewSet,
    basename='interview',
)
router_v1_interview.register(
    r'question',
    QuestionAnswerViewSet,
    basename='question',
)

urlpatterns = [
    path('', include(router_v1_interview.urls)),
]
