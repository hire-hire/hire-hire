from rest_framework import viewsets
from rest_framework import mixins

from interview.models import Category, Language

from api.serializers import CategorySerializer, LanguageSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()

