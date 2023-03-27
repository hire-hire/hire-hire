from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from api_interview.views import (
    CategoryViewSet,
    InterviewViewset,
    LanguageViewSet,
    QuestionAnswerViewset,
)

router_v1 = DefaultRouter()

router_v1.register(r'category', CategoryViewSet)
router_v1.register(r'language', LanguageViewSet)
router_v1.register(r'interview', InterviewViewset, basename='interview')
router_v1.register(r'question', QuestionAnswerViewset)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    re_path(r'^v1/auth/', include('djoser.urls')),
    re_path(r'^v1/auth/', include('djoser.urls.jwt')),
]
