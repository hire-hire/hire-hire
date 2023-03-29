from rest_framework import viewsets

from api.serializers import ContributorSerializer
from contributors.models import Contributor


class ContributorsListViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ContributorSerializer
    queryset = Contributor.objects.get_contributors_with_contacts_and_roles()
