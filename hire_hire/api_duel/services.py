from duel.models import Duel, DuelPlayer, DuelQuestion
from interview.models import Question


def create_duel(owner):
    return Duel.objects.create(owner=owner)


def create_duel_players(duel, players):
    DuelPlayer.objects.bulk_create((
        DuelPlayer(
            name=player.get('name'),
            duel=duel,
        )
        for player in players
    ))


def create_duel_questions(duel, question_count):
    DuelQuestion.objects.bulk_create((
        DuelQuestion(
            duel=duel,
            is_answered=False,
            question=question,
        ) for question in Question.objects.get_random_questions(question_count)
    ))
