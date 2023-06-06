from django.conf import settings
from rest_framework import serializers

from add_question.models import AddQuestion
from api_add_question.validators import validate_added_questions_per_day_limit


class AddQuestionSerializer(serializers.ModelSerializer):
    extra_data = serializers.SerializerMethodField()

    class Meta:
        model = AddQuestion
        fields = '__all__'
        read_only_fields = (
            AddQuestion.author.field.name,
            AddQuestion.ip_address.field.name,
            AddQuestion.pub_date.field.name,
            AddQuestion.status.field.name,
            AddQuestion.user_cookie_id.field.name,
        )

    def get_extra_data(self, obj):
        return {
            'add_questions_for24_count': (
                AddQuestion.objects.get_24_hours_added_question_count(
                    self.context.get('request').user,
                    self.context.get('view').user_cookie_id,
                )
            ),
            'limit_add_questions_per_day': (
                settings.LIMIT_ADD_QUESTIONS_PER_DAY
            ),
        }

    def validate(self, attrs):
        validate_added_questions_per_day_limit(
            self.context.get('request').user,
            self.context.get('view').user_cookie_id,
        )
        return attrs
