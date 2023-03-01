from duel.models import Duel, DuelPlayer, DuelQuestion
from interview.models import Question


def set_duel_question_is_answered(duel_question):
    if duel_question:
        duel_question.is_answered = True
        duel_question.save()


def create_duel(user, question_count, players_names):
    duel = Duel.objects.create(
        owner=user,
    )

    DuelPlayer.objects.bulk_create((
        DuelPlayer(
            name=name,
            duel=duel,
        )
        for name in players_names
    ))

    DuelQuestion.objects.bulk_create((
        DuelQuestion(
            duel=duel,
            is_answered=False,
            question=question,
        ) for question in Question.objects.get_random_questions(question_count)
    ))
    return duel
