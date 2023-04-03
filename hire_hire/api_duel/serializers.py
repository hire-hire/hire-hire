from rest_framework import serializers
from django.conf import settings

from api_interview.serializers import QuestionsSerializer
from api_duel.services import create_duel
from duel.models import Duel, DuelPlayer, DuelQuestion
from duel.services import set_duel_question_is_answered
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
            'id',
            'username',
        )


class DuelPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DuelPlayer
        fields = (
            'id',
            'name',
            'good_answers_count',
        )


class DuelUpdateSerializer(serializers.ModelSerializer):
    players = DuelPlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Duel
        fields = (
            'wrong_answers_count',
            'players',
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
    winner_id = serializers.IntegerField()
    question_id = serializers.IntegerField()

    class Meta:
        model = Duel
        fields = (
            'winner_id',
            'question_id',
        )

    def update(self, instance, validated_data):
        winner_pk = validated_data.get('winner_id')
        question_id = validated_data.get('question_id')
        duel = instance
        DuelPlayer.objects.update_player_and_duel_score(winner_pk=winner_pk, duel=duel)
        duel_question = duel.questions.get(pk=question_id)
        set_duel_question_is_answered(duel_question=duel_question)
        return duel

    def to_representation(self, instance):
        serializer = DuelUpdateSerializer(instance)
        return serializer.data
