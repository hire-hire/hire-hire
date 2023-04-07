from rest_framework import mixins, permissions, viewsets

from api_duel.permissions import IsDuelModerator
from api_duel.serializers import (
    DuelCreateSerializer,
    DuelPartialUpdateSerializer,
    DuelSerializer,
)
from duel.models import Duel


class DuelViewSet(
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (
        permissions.IsAuthenticated,
        IsDuelModerator,
    )

    def get_queryset(self):
        if self.action == 'retrieve':
            return Duel.objects.filter(
                id=self.kwargs.get('pk'),
                owner=self.request.user,
            )
        return Duel.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return DuelCreateSerializer
        elif self.action == 'partial_update':
            return DuelPartialUpdateSerializer
        return DuelSerializer
