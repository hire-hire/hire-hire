import pytest

from interview.models import Question, QuestionAnswer


class TestQuestionAPI:
    url_question = '/api/v1/question/'

    @pytest.mark.django_db(transaction=True)
    def test_category_not_auth(self, client, all_questions):
        url = self.url_question + str(all_questions[0].pk) + '/'
        response = client.get(url)

        assert response.status_code == 401, ('Вопросы доступны '
                                             'неавторизованному юзеру')

    @pytest.mark.django_db(transaction=True)
    def test_category_fields(self, user_client, all_questions):
        url = self.url_question + str(all_questions[5].pk) + '/'
        response = user_client.get(url)

        fields = response.json()

        assert isinstance(fields, dict), 'Отдается не словарь'

        assert len(fields) == 3, 'Должны отдаваться: язык, текст, ответы'
        assert Question.text.field.name in fields
        assert Question.language.field.name in fields

        assert Question.answers.rel.name in fields
        answers = fields[Question.answers.rel.name]
        assert isinstance(answers, list)
        assert len(answers) > 0
        assert isinstance(answers[0], dict)
        assert QuestionAnswer.is_correct.field.name in answers[0]

    @pytest.mark.django_db(transaction=True)
    def test_question_non_exist(self, user_client, all_questions):
        response = user_client.get(self.url_question + '50/')

        assert response.status_code == 404, ('Не возвращается 404 ошибка'
                                             ' при несуществующем объекте')
