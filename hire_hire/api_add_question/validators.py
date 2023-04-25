from django.conf import settings
from rest_framework import serializers

from add_question.models import AddQuestion


def questions_per_day_limit_validator(user, user_cookie):
    if (
        AddQuestion.objects.get_24_hours_added_question_count(
            user,
            user_cookie,
        )
        >= settings.LIMIT_ADD_QUESTIONS_PER_DAY
    ):
        raise serializers.ValidationError(
            'Вы исчерпали лимит вопросов на день.'
        )
