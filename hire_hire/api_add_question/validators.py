from django.conf import settings
from rest_framework import serializers

from add_question.models import AddQuestion


def questions_per_day_limit_validator(self):
    if (
        AddQuestion.objects.get_24_hours_added_question(
            author=self.context.get('request').user,
            user_cookie=self.context.get('view').user_cookie,
            # user_cookie=self.context.get('request').COOKIES.get('user_cookie'),
        )
        >= settings.LIMIT_ADD_QUESTIONS_PER_DAY
    ):
        raise serializers.ValidationError(
            'Вы исчерпали лимит вопросов на день.'
        )
