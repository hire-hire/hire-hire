from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api_contributors.serializers import ContributorSerializer
from contributors.models import Contributor


class ContributorsListViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = (Contributor.objects.
                get_contributors_with_contacts_and_roles())
    serializer_class = ContributorSerializer
