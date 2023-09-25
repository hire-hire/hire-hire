import pytest

from duel.models import Duel, DuelPlayer, DuelQuestion

QUESTION_COUNT = 10


@pytest.fixture
def duel_instance(moderator_1, all_questions, duel_data):
    duel = Duel.objects.create(owner=moderator_1)

    DuelPlayer.objects.bulk_create(
        DuelPlayer(duel=duel, name=player.get('name'))
        for player in duel_data.get('players')
    )

    DuelQuestion.objects.bulk_create(
        DuelQuestion(duel=duel, question=question, is_answered=False)
        for question in all_questions[:QUESTION_COUNT]
    )

    return duel


@pytest.fixture
def duel_data():
    return {
        'question_count': QUESTION_COUNT,
        'players': [
            {
                'name': 'Ivan',
            },
            {
                'name': 'Anna',
            },
        ],
    }
