from api_duel.exceptions import QuestionAlreadyAnswered
from duel.models import Duel, DuelPlayer, DuelQuestion
from duel.services import set_duel_question_is_answered
from interview.models import Question


def create_duel(owner):
    return Duel.objects.create(owner=owner)


def create_duel_players(duel, players):
    DuelPlayer.objects.bulk_create((
        DuelPlayer(
            name=player.get(DuelPlayer.name.field.name),
            duel=duel,
        )
        for player in players
    ))


def create_duel_questions(duel, question_count, subcategory):
    DuelQuestion.objects.bulk_create(
        DuelQuestion(
            duel=duel,
            is_answered=False,
            question=question,
        ) for question in Question.objects.get_random_questions(
            question_count, subcategory,
        )
    )


def update_duel_question_status(duel_question):
    if duel_question.is_answered:
        raise QuestionAlreadyAnswered
    set_duel_question_is_answered(duel_question=duel_question)


def update_duel_player_score(winner_pk, duel):
    DuelPlayer.objects.update_player_and_duel_score(
        winner_pk=winner_pk,
        duel=duel,
    )
