from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from api.views import CategoryViewSet, LanguageViewSet

router = DefaultRouter()

router.register(r'category', CategoryViewSet)
router.register(r'language', LanguageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
]