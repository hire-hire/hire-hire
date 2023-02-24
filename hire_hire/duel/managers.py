from django.db import models
from django.shortcuts import get_object_or_404


class DuelManager(models.Manager):
    def get_duel_by_user(self, duel_pk, user, do_select_related=True):
        query = self.get_queryset()
        if do_select_related:
            query = query.select_related()

        return get_object_or_404(query.filter(pk=duel_pk, owner=user))


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
