from rest_framework import serializers

from add_question.models import AddQuestion


class AddQuestionSerializer(serializers.ModelSerializer):
    extra_data = serializers.SerializerMethodField()

    class Meta:
        model = AddQuestion
        fields = '__all__'  # ['text', 'answer']

    def get_extra_data(self, obj):
        print('ser get_extra_data!!!!!!!!!!!!!!!!!!!!')
        return {
            'add_questions_for24_count': self.context.get(
                'add_questions_for24_count'
            ),
            'limit_add_questions_per_day': self.context.get(
                'limit_add_questions_per_day'
            ),
        }

    def validate(self, data):
        print('ser validate!!!!!!!!!!!!!!!!!!!!')
        add_questions_for24_count = self.context.get(
            'add_questions_for24_count')
        limit_add_questions_per_day = self.context.get(
            'limit_add_questions_per_day')
        if add_questions_for24_count >= limit_add_questions_per_day:
            raise serializers.ValidationError(
                'Вы исчерпали лимит вопросов на день.')
        return data
