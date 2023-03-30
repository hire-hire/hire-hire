from rest_framework import mixins, permissions, viewsets

from api_duel.serializers import DuelSerializer, DuelCreateSerializer
from duel.models import Duel


class DuelViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        if self.action == 'retrieve':
            return Duel.objects.get_duel_by_user(
                duel_pk=self.kwargs.get('pk'),
                user=self.request.user,
            )
        return Duel.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return DuelCreateSerializer
        return DuelSerializer
