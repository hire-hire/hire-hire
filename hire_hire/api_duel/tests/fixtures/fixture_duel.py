import pytest

from duel.models import Duel, DuelPlayer, DuelQuestion

QUESTION_COUNT = 10


@pytest.fixture
def duel_instance(moderator, all_questions):
    duel = Duel.objects.create(owner=moderator)
    DuelPlayer.objects.create(name='Ivan', duel=duel)
    DuelPlayer.objects.create(name='Anna', duel=duel)
    questions = all_questions[:QUESTION_COUNT]

    DuelQuestion.objects.bulk_create(
        DuelQuestion(duel=duel, question=question, is_answered=False)
        for question in questions
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
