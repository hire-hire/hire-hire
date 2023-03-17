from rest_framework import viewsets
from rest_framework import mixins

from interview.models import Category, Language
from contributors.models import Contributor

from api.serializers import (CategorySerializer, LanguageSerializer,
                             ContributorSerializer)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


class ContributorsListViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ContributorSerializer
    queryset = Contributor.objects.all()
