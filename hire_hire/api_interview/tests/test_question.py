import pytest


class TestQuestionAPI:
    url_question = '/api/v1/question/'

    @pytest.mark.django_db(transaction=True)
    def test_category_not_auth(self, client, question_1):
        url = self.url_question + str(question_1.pk) + '/'
        response = client.get(url)

        assert response.status_code == 401, ('Вопросы доступны '
                                             'неавторизованному юзеру')

    @pytest.mark.django_db(transaction=True)
    def test_category_fields(self, user_client, question_6):
        url = self.url_question + str(question_6.pk) + '/'
        response = user_client.get(url)

        fields = response.json()

        assert type(fields) == dict, 'Отдается не словарь'
        assert len(fields) == 1, 'Отдается что-то кроме ответа'

    @pytest.mark.django_db(transaction=True)
    def test_question_non_exist(self, user_client, question_13):
        response = user_client.get(self.url_question + '3/')

        assert response.status_code == 404, ('Не возвращается 404 ошибка'
                                             ' при несуществующем объекте')
