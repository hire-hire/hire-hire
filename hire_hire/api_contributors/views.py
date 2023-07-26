from rest_framework import viewsets
from rest_framework.response import Response

from api_contributors.serializers import ContributorSerializer
from contributors.models import Contributor


class ContributorsListViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = (Contributor.objects.
                    get_contributors_with_contacts_and_roles())
        serializer = ContributorSerializer(queryset, many=True)
        return Response(serializer.data)
