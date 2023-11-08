from django.conf import settings
from rest_framework import serializers

from add_question.models import AddQuestion


def validate_added_questions_per_day_limit(user):
    count = AddQuestion.objects.get_24_hours_added_question_count(user)

    if count >= settings.LIMIT_ADD_QUESTIONS_PER_DAY:
        raise serializers.ValidationError(
            'Вы исчерпали лимит вопросов на день.',
        )
