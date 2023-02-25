from duel.models import Duel, DuelQuestion, DuelPlayer
from interview.models import Question
from interview.services import get_question_count


def set_duel_question_is_answered(duel_question):
    if duel_question:
        duel_question.is_answered = True
        duel_question.save()


def create_duel(user, post_data):
    count = get_question_count(post_data, 'duel-questions-count')

    duel = Duel.objects.create(
        owner=user,
    )

    DuelPlayer.objects.bulk_create((
        DuelPlayer(
            name=post_data.get(f'player{pk}') or f'Игрок {pk}',
            duel=duel,
        )
        for pk in range(1, 3)
    ))

    DuelQuestion.objects.bulk_create((
        DuelQuestion(
            duel=duel,
            is_answered=False,
            question=question,
        ) for question in Question.objects.get_random_questions(count)
    ))
    return duel
