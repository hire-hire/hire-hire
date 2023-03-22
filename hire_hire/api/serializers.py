from django.contrib.auth import get_user_model
from rest_framework import serializers

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


class QuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'text',)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('pk',)


class InterviewCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer
    question_count = serializers.IntegerField(required=True)

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
        fields = ('id', 'questions',)
