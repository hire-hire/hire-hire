from interview.models import Interview, Question


def create_interview(user, question_count):
    interview = Interview.objects.create(
        user=user,
    )
    interview.questions.add(
        *Question.objects.get_random_questions(question_count, user=user),
    )

    return interview
