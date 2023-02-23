from django.conf import settings

from interview.models import Duel, DuelPlayer, DuelQuestion, Question


def create_duel(request):
    count = get_question_count(request.POST, 'duel-questions-count')

    duel = Duel.objects.create(
        owner=request.user if request.user.is_authenticated else None,
    )

    DuelPlayer.objects.bulk_create(
        (DuelPlayer(name=request.POST.get(f'player{pk}'), duel=duel)) for pk in range(1, 3)
    )

    DuelQuestion.objects.bulk_create((
        DuelQuestion(
            duel=duel,
            is_answered=False,
            question=question,
        ) for question in Question.objects.get_random_questions(count)
    ))
    return duel


def get_question_count(post_data, atr_name):
    try:
        return int(post_data.get(atr_name))
    except ValueError:
        return settings.DEFAULT_QUESTIONS_COUNT


def set_duel_question_is_answered(duel_question):
    if duel_question:
        duel_question.is_answered = True
        duel_question.save()
