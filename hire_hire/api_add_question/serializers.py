from django.conf import settings
from rest_framework import serializers

from add_question.models import AddQuestion


class AddQuestionSerializer(serializers.ModelSerializer):
    extra_data = serializers.SerializerMethodField()

    class Meta:
        model = AddQuestion
        fields = '__all__'  # пока так ['text', 'answer']

    def validate(self, data):
        if (
            AddQuestion.objects.get_24_hours_added_question(
                self.context.get('request')
            )
            >= settings.LIMIT_ADD_QUESTIONS_PER_DAY
        ):
            raise serializers.ValidationError(
                'Вы исчерпали лимит вопросов на день.'
            )
        return data

    def get_extra_data(self, obj):
        return {
            'add_questions_for24_count': (
                AddQuestion.objects.get_24_hours_added_question(
                    self.context.get('request')
                )
            ),
            'limit_add_questions_per_day': (
                settings.LIMIT_ADD_QUESTIONS_PER_DAY
            ),
        }
