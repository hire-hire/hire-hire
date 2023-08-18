import pytest

from interview.models import Question


class TestQuestionRandom:

    @pytest.mark.django_db(transaction=True)
    def test_questions_uniq(self, user, all_questions):
        cnt = 10
        first_questions = Question.objects.get_random_questions(cnt, user=user)
        assert len(first_questions) == cnt, 'Вопросы не отдаются'
        sec_questions = Question.objects.get_random_questions(cnt, user=user)
        assert len(sec_questions) == cnt, 'Вопросы не отдаются'
        assert len(
            set(first_questions) | set(sec_questions)
        ) == cnt + cnt, 'Вопросы не уникальны'

    @pytest.mark.django_db(transaction=True)
    def test_questions_dont_end(self, user, all_questions):
        cnt = len(all_questions)
        q1 = Question.objects.get_random_questions(cnt, user=user)
        q2 = Question.objects.get_random_questions(cnt, user=user)
        assert len(q1) == len(q2) == cnt, 'Отдает меньше вопросов чем нужно'

    @pytest.mark.django_db(transaction=True)
    def test_get_questions(self, user, all_questions):
        cnt = len(all_questions)
        questions = Question.objects.get_random_questions(cnt, user=user)
        for question, correct_question in zip(questions, all_questions):
            assert question == correct_question
