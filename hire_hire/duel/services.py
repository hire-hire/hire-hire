import logging

from duel.exceptions import QuestionAlreadyAnswered
from duel.models import Duel, DuelPlayer, DuelQuestion
from interview.models import Question


logger = logging.getLogger('custom')


def create_duel(owner):
    logger.debug(f'creating duel for user={owner}')
    return Duel.objects.create(owner=owner)


def create_duel_players(duel, players):
    DuelPlayer.objects.bulk_create((
        DuelPlayer(
            name=player.get(DuelPlayer.name.field.name),
            duel=duel,
        )
        for player in players
    ))


def create_duel_questions(duel, question_count, subcategory, user):
    DuelQuestion.objects.bulk_create(
        DuelQuestion(
            duel=duel,
            is_answered=False,
            question=question,
        ) for question in Question.objects.get_random_questions(
            cnt=question_count,
            language=subcategory,
            user=user,
        )
    )


def update_duel_question_status(duel_question):
    if duel_question.is_answered:
        logger.debug('duel_question is already answered')
        raise QuestionAlreadyAnswered
    if duel_question:
        logger.debug('changing duel_question status')
        duel_question.is_answered = True
        duel_question.save()


def update_duel_player_score(winner_pk, duel):
    DuelPlayer.objects.update_player_and_duel_score(
        winner_pk=winner_pk,
        duel=duel,
    )
