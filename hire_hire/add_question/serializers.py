from rest_framework import serializers

from add_question.models import AddQuestion


class AddQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddQuestion
        fields = '__all__'
        read_only_fields = (
            AddQuestion.author.field.name,
            AddQuestion.pub_date.field.name,
            AddQuestion.status.field.name,
        )
