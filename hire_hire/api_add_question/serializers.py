from django.conf import settings
from rest_framework import serializers

from add_question.models import AddQuestion
from api_add_question.validators import questions_per_day_limit_validator


class AddQuestionSerializer(serializers.ModelSerializer):
    extra_data = serializers.SerializerMethodField()

    class Meta:
        model = AddQuestion
        fields = '__all__'
        read_only_fields = (
            'author',
            'ip_address',
            'pub_date',
            'status',
            'user_cookie',
        )

    def get_extra_data(self, obj):
        return {
            'add_questions_for24_count': (
                AddQuestion.objects.get_24_hours_added_question(
                    author=self.context.get('request').user,
                    user_cookie=self.context.get('view').user_cookie,
                    # user_cookie=self.context.get('request').COOKIES.get('user_cookie'),
                )
            ),
            'limit_add_questions_per_day': (
                settings.LIMIT_ADD_QUESTIONS_PER_DAY
            ),
        }

    def validate(self, attrs):
        # if (
        #     AddQuestion.objects.get_24_hours_added_question(
        #         author=self.context.get('request').user,
        #         user_cookie=self.context.get('view').user_cookie,
        #         # user_cookie=self.context.get('request').COOKIES.get('user_cookie'),
        #     )
        #     >= settings.LIMIT_ADD_QUESTIONS_PER_DAY
        # ):
        #     raise serializers.ValidationError(
        #         'Вы исчерпали лимит вопросов на день.'
        #     )
        questions_per_day_limit_validator(self)
        return attrs
