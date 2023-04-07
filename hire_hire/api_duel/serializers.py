from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from api_duel.services import (
    create_duel,
    create_duel_players,
    create_duel_questions,
)
from api_interview.serializers import QuestionsSerializer
from duel.models import Duel, DuelPlayer, DuelQuestion
from duel.services import set_duel_question_is_answered

User = get_user_model()


class DuelQuestionsSerializer(serializers.ModelSerializer):
    question = QuestionsSerializer()

    class Meta:
        model = DuelQuestion
        fields = (
            DuelQuestion.id.field.name,
            DuelQuestion.question.field.name,
        )


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            User.id.field.name,
            User.username.field.name,
        )


class DuelPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DuelPlayer
        fields = (
            DuelPlayer.id.field.name,
            DuelPlayer.name.field.name,
            DuelPlayer.good_answers_count.field.name,
        )


class DuelUpdateSerializer(serializers.ModelSerializer):
    players = DuelPlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Duel
        fields = (
            Duel.wrong_answers_count.field.name,
            Duel.players.field._related_name,
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
    players = DuelPlayerSerializer(many=True)

    class Meta:
        model = Duel
        fields = (
            'question_count',
            Duel.players.field._related_name,
        )

    def create(self, validated_data):
        request = self.context.get('request')
        duel = create_duel(request.user)
        question_count = validated_data.get('question_count')
        create_duel_questions(duel, question_count)
        players = validated_data.get('players')
        create_duel_players(duel, players)
        return duel

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
        duel_question = get_object_or_404(instance.questions, pk=question_id)
        set_duel_question_is_answered(duel_question=duel_question)
        DuelPlayer.objects.update_player_and_duel_score(
            winner_pk=winner_pk,
            duel=instance,
        )
        return instance

    def to_representation(self, instance):
        serializer = DuelUpdateSerializer(instance)
        return serializer.data
