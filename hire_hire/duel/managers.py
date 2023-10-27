import logging

from django.db import models
from django.shortcuts import get_object_or_404

from duel.exceptions import DuelPlayerDoesNotExist
import duel.models


logger = logging.getLogger('custom')


class DuelManager(models.Manager):
    def get_duel_by_user(self, duel_pk, user, do_select_related=True):
        query = self.get_queryset()
        if do_select_related:
            query = query.select_related()
        return get_object_or_404(query.filter(pk=duel_pk, owner=user))

    def filter_duel_by_user(self, duel_pk, user):
        logger.debug(f'trying to find duel by INPUT: duel_pk={duel_pk}, user={user}')
        return (
            self.get_queryset()
            .filter(pk=duel_pk, owner=user)
            .prefetch_related(
                models.Prefetch(
                    self.model.questions.rel.name,
                    queryset=duel.models.DuelQuestion.objects.select_related(),
                ),
                self.model.players.rel.name,
            )
        )


class DuelQuestionManager(models.Manager):
    def get_no_answered(self, get_object=True):
        query = self.get_queryset().filter(is_answered=False)
        if get_object:
            query = query.first()

        return query

    def get_current_question_number(self):
        query = self.get_queryset().filter(is_answered=True)
        return query.count() + 1


class DuelPlayerManager(models.Manager):
    def update_player_and_duel_score(self, winner_pk, duel):
        if winner_pk == -1:
            logger.debug('no winners found')
            duel.wrong_answers_count += 1
            duel.save()
            return

        try:
            winner = self.model.objects.get(
                duel=duel,
                pk=winner_pk,
            )
        except self.model.DoesNotExist:
            raise DuelPlayerDoesNotExist

        winner.good_answers_count += 1
        logger.debug(f'winner found and updated')
        winner.save()
