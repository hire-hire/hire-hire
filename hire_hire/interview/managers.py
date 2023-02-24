from random import sample

from django.db import models


class QuestionManager(models.Manager):

    def get_random_questions(self, cnt):
        ids = list(self.get_queryset().values_list('id', flat=True))
        rand_ids = sample(ids, min(cnt, len(ids)))
        return self.get_queryset().filter(id__in=rand_ids)


class InterviewManager(models.Manager):
    def get_interview_by_user(self, interview_pk, user):
        return self.get_queryset().filter(pk=interview_pk, user=user)
