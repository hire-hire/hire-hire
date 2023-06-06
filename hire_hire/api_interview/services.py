from interview.models import Interview, Question


def create_interview(ser_validated_data):
    question_count = ser_validated_data.pop('question_count')
    instance = Interview.objects.create(**ser_validated_data)
    questions = Question.objects.get_random_questions(question_count)
    instance.questions.add(*questions)
    return instance
