import pytest

from interview.models import Interview


class TestInterviewApi:

    def setup_class(self):
        self.url_interview = '/api/v1/interview/'
        self.data = {'question_count': 10}

    @pytest.mark.django_db(transaction=True)
    def test_unavailable_not_auth(self, client, user_client):
        resp_no_auth = client.post(self.url_interview, data=self.data)

        assert resp_no_auth.status_code == 401, (f'Ответ неавторизованному '
                                                 f'от {self.url_interview}'
                                                 f'приходит не со '
                                                 f'статусом 401')

    @pytest.mark.django_db(transaction=True)
    def test_unavailable_auth(self, client, user_client):
        resp_auth = user_client.post(self.url_interview, data=self.data)

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
            self, user_client, all_questions,
    ):
        response = user_client.post(self.url_interview, data=self.data)
        length = len(response.json().get('questions'))
        quest_cnt = self.data['question_count']
        assert length == quest_cnt, ('Кол-во вопросов в новом '
                                     'интервью не совпадает с настройкой')

    @pytest.mark.django_db(transaction=True)
    def test_no_extra_fields(self, user_client, all_questions):
        data = {'question_count': 10}
        response = user_client.post('/api/v1/interview/', data=data)
        question = response.json().get('questions')[0]

        assert 'answer' not in question, ('В интервью отдаются '
                                          'вопросы с ответами')
