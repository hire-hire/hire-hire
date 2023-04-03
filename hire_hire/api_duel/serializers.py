from rest_framework import serializers
from django.conf import settings

from api_interview.serializers import QuestionsSerializer
from api_duel.services import create_duel
from duel.models import Duel, DuelPlayer, DuelQuestion
from django.contrib.auth import get_user_model

User = get_user_model()


class DuelQuestionsSerializer(serializers.ModelSerializer):
    question = QuestionsSerializer()

    class Meta:
        model = DuelQuestion
        fields = (
            'id',
            'question',
        )


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
        )


class DuelPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DuelPlayer
        fields = (
            "id",
            "name",
        )


class DuelSerializer(serializers.ModelSerializer):
    questions = DuelQuestionsSerializer(many=True, read_only=True)
    players = DuelPlayerSerializer(many=True, read_only=True)
    owner = OwnerSerializer()

    class Meta:
        model = Duel
        fields = '__all__'


class DuelCreateSerializer(serializers.ModelSerializer):
    question_count = serializers.ChoiceField(
        choices=settings.QUESTION_COUNT_CHOICE,
    )
    player_1 = DuelPlayerSerializer()
    player_2 = DuelPlayerSerializer()

    class Meta:
        model = Duel
        fields = (

            'question_count',
            'player_1',
            'player_2',
        )

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return create_duel(validated_data)

    def to_representation(self, instance):
        serializer = DuelSerializer(instance)
        return serializer.data


class DuelPartialUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Duel
        fields = (
            'wrong_answers_count',
        )
