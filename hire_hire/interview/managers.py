from random import sample

from django.conf import settings
from django.db import models
from django.utils import timezone

import interview.models as int_models


class QuestionManager(models.Manager):
    def filter_by_category(self, category):
        query = self.get_queryset()
        if category is not None:
            query = query.filter(language=category)
        return query

    def get_random_questions(self, cnt, category=None, user=None):
        print('START')
        user_refresh, _ = int_models.LastUserRefreshDate.objects.get_or_create(
            user=user,
        )
        default_range = timezone.now().date() - settings.QUESTION_REFRESH_RANGE
        queryset = self.filter_by_category(category).exclude(
            q_last_date_used__user=user,
            q_last_date_used__date__gt=min(default_range, user_refresh.date),
        )

        ids = list(queryset.values_list('id', flat=True))
        if len(ids) < cnt:
            user_refresh.date = timezone.now()
            user_refresh.save()

            queryset = self.filter_by_category(category)

        ids = list(queryset.values_list('id', flat=True))
        rand_ids = sample(ids, min(cnt, len(ids)))

        selected_questions = self.get_queryset().filter(id__in=rand_ids)

        int_models.QuestionLastDateUsed.objects.create_objects(
            user=user,
            question=selected_questions,
        )
        return selected_questions


class InterviewManager(models.Manager):
    def get_interview_by_user(self, interview_pk, user):
        return self.get_queryset().filter(pk=interview_pk, user=user)


class QuestionLastDateUsedManage(models.Manager):
    def create_objects(self, user, question):
        self.get_queryset().bulk_create(
            int_models.QuestionLastDateUsed(
                user=user,
                question=question,
            )
            for question in question
        )
