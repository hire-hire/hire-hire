import logging
from random import sample

from django.conf import settings
from django.db import models
from django.utils import timezone

import interview.models as int_models


logger = logging.getLogger(__name__)


class QuestionManager(models.Manager):
    def filter_by_language(self, language=None):
        query = self.get_queryset()
        if language is not None:
            query = query.filter(language=language)
        return query

    def get_not_used_questions(self, user, user_refresh, language):
        base_refresh_date = timezone.now() - settings.QUESTION_REFRESH_DELTA
        return self.filter_by_language(language).exclude(
            questions_last_date_used__user=user,
            questions_last_date_used__date__gt=max(
                base_refresh_date,
                user_refresh.date,
            ),
        )

    @staticmethod
    def generate_ids_list(queryset):
        return list(
            queryset.values_list(int_models.Question.id.field.name, flat=True),
        )

    def get_random_questions(self, cnt, user, language=None):
        user_refresh, _ = int_models.LastUserRefreshDate.objects.get_or_create(
            user=user,
        )
        logger.debug(f'user_refresh_date={user_refresh.date}')
        queryset = self.get_not_used_questions(user, user_refresh, language)

        ids = self.generate_ids_list(queryset)
        logger.debug(f'not_used_question_LENGTH={len(ids)}')
        if len(ids) < cnt:
            logger.debug('no refresh date found, creating')
            user_refresh.date = timezone.now()
            user_refresh.save()

            queryset = self.filter_by_language(language)
            ids = self.generate_ids_list(queryset)

        rand_ids = sample(ids, min(cnt, len(ids)))
        selected_questions = self.get_queryset().filter(id__in=rand_ids)

        int_models.QuestionLastDateUsed.objects.create_objects(
            user=user,
            questions=selected_questions,
        )
        return selected_questions


class InterviewManager(models.Manager):
    def get_interview_by_user(self, interview_pk, user):
        logger.debug(f'user={user}, interview={interview_pk}')
        return self.get_queryset().filter(pk=interview_pk, user=user)


class QuestionLastDateUsedManage(models.Manager):
    def create_objects(self, user, questions):
        self.get_queryset().bulk_create(
            (
                int_models.QuestionLastDateUsed(
                    user=user,
                    question=question,
                )
                for question in questions
            ),
            update_conflicts=True,
            unique_fields=[
                int_models.QuestionLastDateUsed.user.field.name,
                int_models.QuestionLastDateUsed.question.field.name,
            ],
            update_fields=[int_models.QuestionLastDateUsed.date.field.name],
        )
