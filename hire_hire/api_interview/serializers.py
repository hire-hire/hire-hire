from django.conf import settings
from drf_spectacular.utils import OpenApiExample, extend_schema_serializer
from rest_framework import serializers

from api_interview.services import create_interview
from interview.models import Category, Interview, Language, Question


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            '200',
            summary='Валидный ответ',
            description='Возвращает список категорий',
            value={
                    'id': 1,
                    'title': 'Программирование',
                    'icon': 'какой-то урл'
            },
        ),
    ],
)
class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            '200',
            summary='Валидный ответ',
            description='Возвращает подробности по конкретной '
                        'категории со влолженными языками',
            value={
                    'id': 1,
                    'title': 'Программирование',
                    'icon': 'какой-то урл',
                    'lanuages': [
                        {
                            'id': 1,
                            'title': 'python',
                            'icon': 'какая-то иконка',
                            'category': 1
                        },
                        {
                            'id': 2,
                            'title': 'javascript',
                            'icon': 'какая-то иконка',
                            'category': 1
                        }
                    ]
            },
            response_only=False,
        ),
    ]
)
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
