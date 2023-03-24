from django.conf import settings
from rest_framework import serializers

from api_users.serializers import UserSerializer
from interview.models import Category, Interview, Language, Question


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class CategoryRetrieveSerializer(serializers.ModelSerializer):
    languages = LanguageSerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class QuestionsAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('answer',)


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'id',
            'text',
        )


class InterviewCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer
    question_count = serializers.ChoiceField(
        choices=settings.QUESTION_COUNT_CHOICE
    )

    def create(self, validated_data):
        cnt = validated_data.pop('question_count')
        instance = Interview.objects.create(**validated_data)
        questions = Question.objects.get_random_questions(cnt)
        instance.questions.add(*questions)
        return instance

    def to_representation(self, instance):
        serializer = InterviewSerializer(instance)
        return serializer.data

    class Meta:
        model = Interview
        fields = ('user', 'question_count')


class InterviewSerializer(serializers.ModelSerializer):
    questions = QuestionsSerializer(many=True, read_only=True)

    class Meta:
        model = Interview
        fields = (
            'id',
            'questions',
        )
