import pytest


class TestDuelApi:

    def setup_class(self):
        self.url_duel = '/api/v1/duel/'
        self.data = {
            'question_count': 10,
            'players': [
                {
                    'name': 'Ivan',
                },
                {
                    'name': 'Anna',
                },
            ],
        }

    @pytest.mark.django_db(transaction=True)
    def test_duel_unavailable_not_auth(
            self,
            client,
            user_client,
            moderator_client,
    ):
        resp_no_auth = client.post(self.url_duel, data=self.data)

        assert resp_no_auth.status_code == 401, (f'Ответ неавторизованному '
                                                 f'от {self.url_duel}'
                                                 f'приходит не со '
                                                 f'статусом 401')

    @pytest.mark.django_db(transaction=True)
    def test_duel_unavailable_auth(
            self,
            client,
            user_client,
            moderator_client,
    ):
        resp_auth = user_client.post(self.url_duel, data=self.data)

        assert resp_auth.status_code == 403, (f'Ответ авторизованному, '
                                              f'немодератору от '
                                              f'{self.url_duel} '
                                              f'приходит не со '
                                              f'статусом 403')

    @pytest.mark.django_db(transaction=True)
    def test_duel_valid_data_only(
            self,
            client,
            user_client,
            moderator_client,
    ):
        invalid_data_1 = {'question_count': 10}
        response = moderator_client.post(self.url_duel, data=invalid_data_1)

        assert response.status_code == 400, (f'Ответ от {self.url_duel} '
                                             f'при некорректна дата без '
                                             f'игроков приходит не со '
                                             f'статусом 400')
        invalid_data_2 = {'players': [{'name': 'Juan'}]}
        response = moderator_client.post(self.url_duel, data=invalid_data_2)

        assert response.status_code == 400, (f'Ответ от {self.url_duel} '
                                             f'при некорректна дата без '
                                             f'кол-во вопросов '
                                             f'приходит не со '
                                             f'статусом 400')

    @pytest.mark.django_db(transaction=True)
    def test_duel_available_auth_moderator(
            self,
            client,
            user_client,
            moderator_client,
            language_1,
            all_questions,
    ):
        data = self.data
        data.update({'language': language_1.pk})
        resp_auth = moderator_client.post(
            self.url_duel,
            data=data,
            format='json',
        )
        assert resp_auth.status_code == 201, (f'Ответ авторизованному, '
                                              f'модератору от '
                                              f'{self.url_duel} '
                                              f'приходит не со '
                                              f'статусом 201')

    @pytest.mark.django_db(transaction=True)
    def test_duel_valid_question_count(
            self,
            client,
            user_client,
            moderator_client,
            language_1,
            all_questions,
    ):
        data = self.data
        data.update({'language': language_1.pk})
        resp_auth = moderator_client.post(
            self.url_duel,
            data=data,
            format='json',
        )
        assert (
                len(resp_auth.json().get('questions'))
                == self.data.get('question_count')
        ), 'Количество вопросов не совпадает с переданном количеством'
