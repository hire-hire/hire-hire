import pytest

from interview.models import Interview


class TestInterviewApi:
    url_interview = '/api/v1/interview/'
    data = {'question_count': 10}

    @pytest.mark.django_db(transaction=True)
    def test_unavailable_not_auth(self, client, user_client):
        resp_no_auth = client.post(self.url_interview, data=self.data)
        resp_auth = user_client.post(self.url_interview, data=self.data)

        assert resp_no_auth.status_code == 401, (f'Ответ неавторизованному '
                                                 f'от {self.url_interview}'
                                                 f'приходит не со '
                                                 f'статусом 401')
        assert resp_auth.status_code == 201, (f'Ответ авторизованному от '
                                              f'{self.url_interview} '
                                              f'приходит не со '
                                              f'статусом 201')

    @pytest.mark.django_db(transaction=True)
    def test_valid_question_count_only(self, user_client):
        invalid_data = {'question_count': 11}
        response = user_client.post(self.url_interview, data=invalid_data)

        assert response.status_code == 400, (f'Ответ от {self.url_interview} '
                                             f'при некорректно кол-ве вопросов'
                                             f' приходит не со статусом 400')

    @pytest.mark.django_db(transaction=True)
    def test_interview_create_success(self, user_client):
        db_objects = Interview.objects.all().count()
        user_client.post(self.url_interview, data=self.data)
        new_db_count = Interview.objects.all().count()

        assert new_db_count == db_objects + 1, ('Количество интервью '
                                                'не изменилось после '
                                                'создания нового')

    @pytest.mark.django_db(transaction=True)
    def test_valid_question_count_created(
            self, user_client, question_1, question_2,
            question_3, question_4, question_5,
            question_6, question_7, question_8,
            question_9, question_10, question_11
    ):
        response = user_client.post(self.url_interview, data=self.data)
        length = len(response.json().get('questions'))
        setting = self.data['question_count']
        assert length == setting, ('Кол-во вопросов в новом '
                                   'интервью не совпадает с настройкой')
