from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api_contributors.views import ContributorsListViewSet

router_v1_contributors = DefaultRouter()


router_v1_contributors.register(
    r'contributors',
    ContributorsListViewSet,
    basename='contributors',
)

urlpatterns = [
    path('', include(router_v1_contributors.urls)),
]
