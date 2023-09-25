import pytest

from interview.models import Question


class TestQuestionRandom:
    @pytest.mark.django_db(transaction=True)
    def test_questions_gives_and_dont_end(self, user, all_questions):
        cnt = len(all_questions)

        first_questions = Question.objects.get_random_questions(cnt, user=user)
        assert (
                len(first_questions) == cnt
        ), 'Не верное кол-во вопросов при первом запросе'

        sec_questions = Question.objects.get_random_questions(cnt, user=user)
        assert (
                len(sec_questions) == cnt
        ), 'Не верное кол-во вопросов при повторном запросе'

    @pytest.mark.django_db(transaction=True)
    def test_questions_uniq(self, user, all_questions):
        cnt = len(all_questions) // 2
        first_questions = Question.objects.get_random_questions(cnt, user=user)
        sec_questions = Question.objects.get_random_questions(cnt, user=user)

        assert len(
            set(first_questions) | set(sec_questions)
        ) == cnt + cnt, 'Вопросы не уникальны'

    @pytest.mark.django_db(transaction=True)
    def test_get_questions(self, user, all_questions):
        cnt = len(all_questions)
        questions = Question.objects.get_random_questions(cnt, user=user)
        assert list(questions) == list(all_questions)
