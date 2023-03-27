from django.conf import settings
from rest_framework import serializers

from api_interview.services import create_interview
from interview.models import Category, Interview, Language, Question


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryRetrieveSerializer(CategoryListSerializer):
    languages = LanguageSerializer(many=True)


class QuestionsAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (Question.answer.field.name,)


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            Question.id.field.name,
            Question.text.field.name,
        )


class InterviewCreateSerializer(serializers.ModelSerializer):
    question_count = serializers.ChoiceField(
        choices=settings.QUESTION_COUNT_CHOICE,
    )

    class Meta:
        model = Interview
        fields = ('question_count',)

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return create_interview(validated_data)

    def to_representation(self, instance):
        serializer = InterviewSerializer(instance)
        return serializer.data


class InterviewSerializer(serializers.ModelSerializer):
    questions = QuestionsSerializer(many=True, read_only=True)

    class Meta:
        model = Interview
        fields = (
            Interview.id.field.name,
            Interview.questions.field.name,
        )
