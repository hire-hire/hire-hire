from interview.models import Interview, Question


def create_interview(ser_validated_data):
    question_count = ser_validated_data.pop('question_count')
    instance = Interview.objects.create(**ser_validated_data)
    questions = Question.objects.get_random_questions(
        cnt=question_count,
        user=ser_validated_data['user'],
    )
    instance.questions.add(*questions)
    return instance
