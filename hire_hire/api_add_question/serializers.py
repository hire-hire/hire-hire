from rest_framework import serializers

from add_question.models import AddQuestion
from api_add_question.validators import validate_added_questions_per_day_limit


class AddQuestionSerializer(serializers.ModelSerializer):
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

    def validate(self, attrs):
        validate_added_questions_per_day_limit(
            self.context.get('request').user,
            self.context.get('view').user_cookie_id,
        )
        return attrs
