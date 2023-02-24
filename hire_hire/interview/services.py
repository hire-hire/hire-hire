from django.conf import settings

from interview.models import Question, Interview


def create_interview(request):
    count = get_question_count(request.POST, 'questions-count')

    interview = Interview.objects.create(
        user=request.user,
    )
    interview.questions.add(
        *Question.objects.get_random_questions(count),
    )

    return interview


def get_question_count(post_data, atr_name):
    try:
        return min(
            int(post_data.get(atr_name)),
            settings.MAX_QUESTIONS_COUNT_BY_ONE_SESSION,
        )
    except ValueError:
        return settings.DEFAULT_QUESTIONS_COUNT
