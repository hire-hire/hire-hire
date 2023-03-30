from duel.models import Duel, DuelPlayer, DuelQuestion
from interview.models import Question


def create_duel(ser_validated_data):
    question_count = ser_validated_data.pop('question_count')
    owner = ser_validated_data.pop('user')
    instance = Duel.objects.create(owner=owner)
    DuelPlayer.objects.bulk_create((
        DuelPlayer(
            name=player.get('name'),
            duel=instance,
        )
        for player in ser_validated_data.values()
    ))
    DuelQuestion.objects.bulk_create((
        DuelQuestion(
            duel=instance,
            is_answered=False,
            question=question,
        ) for question in Question.objects.get_random_questions(question_count)
    ))
    return instance
