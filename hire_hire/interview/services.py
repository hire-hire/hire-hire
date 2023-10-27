import logging

from interview.models import Interview, Question


logger = logging.getLogger('custom')


def create_interview(ser_validated_data):
    question_count = ser_validated_data.pop('question_count')
    logger.debug(f'question_count={question_count}')
    instance = Interview.objects.create(**ser_validated_data)
    logger.debug(
        f'interview created, ID={instance.id}; '
        f'user={ser_validated_data["user"]}'
    )
    questions = Question.objects.get_random_questions(
        cnt=question_count,
        user=ser_validated_data['user'],
    )
    instance.questions.add(*questions)
    return instance
