from random import sample

from django.db import models


class QuestionManager(models.Manager):
    """
    Кастомный менеджер для добавления метода
    выборки данного кол-ва случайных вопросов.
    """

    def random(self, cnt):
        ids = list(self.get_queryset().values_list('id', flat=True))
        rand_ids = sample(ids, min(cnt, len(ids)))
        return self.get_queryset().filter(id__in=rand_ids)
