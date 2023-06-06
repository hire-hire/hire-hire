from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api_add_question.views import AddQuestionViewSet

router_v1_add_question = DefaultRouter()

router_v1_add_question.register(
    r'add_question',
    AddQuestionViewSet,
    basename='add_question',
)

urlpatterns = [
    path('', include(router_v1_add_question.urls)),
]
