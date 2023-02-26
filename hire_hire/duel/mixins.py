from duel.models import Duel


class DuelFlowGetDuelMixin:
    duel = None
    duel_players = None

    def configurate_duel(self):
        self.duel = Duel.objects.get_duel_by_user(
            duel_pk=self.kwargs.get('duel_id'),
            user=self.request.user,
        )
        self.duel_players = self.duel.players.all()
