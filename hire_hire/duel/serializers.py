import logging

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers

from duel.exceptions import DuelQuestionDoesNotExist
from duel.models import Duel, DuelPlayer, DuelQuestion
from duel.services import (
    create_duel,
    create_duel_players,
    create_duel_questions,
    update_duel_player_score,
    update_duel_question_status,
)
from interview.serializers import QuestionsSerializer


logger = logging.getLogger('custom')
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
            Duel.players.rel.name,
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
    language = serializers.IntegerField(required=False)

    class Meta:
        model = Duel
        fields = (
            'question_count',
            Duel.players.rel.name,
            'language',
        )

    def create(self, validated_data):
        request = self.context.get('request')
        duel = create_duel(request.user)
        question_count = validated_data.get('question_count')
        logger.debug(f'question_count={question_count} for duel_ID={duel.id}')
        subcategory = validated_data.get('language')
        logger.debug(f'subcategory={subcategory} for duel_ID={duel.id}')
        create_duel_questions(duel, question_count, subcategory, request.user)
        players = validated_data.get('players')
        logger.debug(f'INPUT: players: {players} for duel_ID={duel.id}')
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
        logger.debug(
            f'INPUT: winner_id={winner_pk}, '
            f'question_id={question_id} '
            f'for duel_ID={instance.id}',
        )
        try:
            duel_question = DuelQuestion.objects.get(
                duel=instance,
                pk=question_id,
            )
        except DuelQuestion.DoesNotExist:
            logger.debug('raising DuelQuestionDoesNotExist')
            raise DuelQuestionDoesNotExist
        with transaction.atomic():
            update_duel_question_status(duel_question=duel_question)
            update_duel_player_score(winner_pk=winner_pk, duel=instance)
        return instance

    def to_representation(self, instance):
        serializer = DuelUpdateSerializer(instance)
        return serializer.data
