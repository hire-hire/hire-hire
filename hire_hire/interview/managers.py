from random import sample

from django.db import models


class QuestionManager(models.Manager):
    """
    Кастомный менеджер для добавления метода
    выборки данного кол-ва случайных вопросов.
    """

    def get_random_questions(self, cnt):
        ids = list(self.get_queryset().values_list('id', flat=True))
        rand_ids = sample(ids, min(cnt, len(ids)))
        return self.get_queryset().filter(id__in=rand_ids)


class DuelQuestionManager(models.Manager):
    def get_no_answered(self, queryset=False):
        query = self.get_queryset().filter(is_answered=False)
        if not queryset:
            query = query.first()

        return query


class DuelPlayer(models.Manager):
    def update_score(self, winner_pk, duel):
        winner = self.get_queryset().filter(
            pk=winner_pk,
        ).first()

        if winner:
            winner.good_answers_count += 1
            winner.save()
        else:
            duel.wrong_answers_count += 1
            duel.save()
