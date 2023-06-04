import pytest

from duel.models import Duel, DuelPlayer, DuelQuestion


@pytest.fixture
def duel_instance(moderator, all_questions):
    duel = Duel.objects.create(owner=moderator)
    DuelPlayer.objects.create(name='Ivan', duel=duel)
    DuelPlayer.objects.create(name='Anna', duel=duel)
    questions = all_questions[:10]

    DuelQuestion.objects.bulk_create(
        DuelQuestion(duel=duel, question=question, is_answered=False)
        for question in questions
    )

    return duel
