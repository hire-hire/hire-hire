from django.db import models


class DuelQuestionManager(models.Manager):
    def get_no_answered(self, queryset=False):
        query = self.get_queryset().filter(is_answered=False)
        if not queryset:
            query = query.first()

        return query


class DuelPlayerManager(models.Manager):
    def update_player_and_duel_score(self, winner_pk, duel):
        winner = self.get_queryset().filter(
            pk=winner_pk,
        ).first()

        if winner:
            winner.good_answers_count += 1
            winner.save()
        else:
            duel.wrong_answers_count += 1
            duel.save()
