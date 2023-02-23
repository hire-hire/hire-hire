from django.conf import settings
from django.http.request import QueryDict


def get_question_count(post_data: QueryDict) -> int:
    try:
        return int(post_data.get('questions-count'))
    except ValueError:
        return settings.DEFAULT_QUESTIONS_COUNT
