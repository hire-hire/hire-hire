from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api_duel.views import DuelViewSet

router_v1_duel = DefaultRouter()

router_v1_duel.register(
    r'duel',
    DuelViewSet,
    basename='duel',
)

urlpatterns = [
    path('', include(router_v1_duel.urls)),
]
