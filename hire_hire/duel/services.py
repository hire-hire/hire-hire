from duel.models import Duel, DuelQuestion, DuelPlayer
from interview.models import Question
from interview.services import get_question_count


def set_duel_question_is_answered(duel_question):
    if duel_question:
        duel_question.is_answered = True
        duel_question.save()


def create_duel(request):
    count = get_question_count(request.POST, 'duel-questions-count')

    duel = Duel.objects.create(
        owner=request.user,
    )
    duel_players = []
    for pk in range(1, 3):
        name = request.POST.get(f'player{pk}')
        if not name:
            name = f'Игрок {pk}'
        duel_players.append(DuelPlayer(name=name, duel=duel))

    DuelPlayer.objects.bulk_create(duel_players)

    DuelQuestion.objects.bulk_create((
        DuelQuestion(
            duel=duel,
            is_answered=False,
            question=question,
        ) for question in Question.objects.get_random_questions(count)
    ))
    return duel
