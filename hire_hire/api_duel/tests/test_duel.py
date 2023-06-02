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

    @pytest.mark.django_db(transaction=True)
    def test_duel_valid_players_count(
            self,
            client,
            user_client,
            moderator_client,
            language_1,
            all_questions,
    ):
        resp_auth = moderator_client.post(
            self.url_duel,
            data=self.data,
            format='json',
        )
        assert (
                len(resp_auth.json().get('players'))
                == len(self.data.get('players'))
        ), 'Количество игроков не совпадает с переданном количеством'

    @pytest.mark.django_db(transaction=True)
    def test_get_duel_not_auth(self, client, duel_instance):
        resp = client.get(f'{self.url_duel}{duel_instance.id}/')
        assert (
                resp.status_code == 401
        ), 'Ответ неавторизованному приходит не со статусом 401'

    @pytest.mark.django_db(transaction=True)
    def test_get_duel_not_owner(self, user_client, duel_instance):
        resp = user_client.get(f'{self.url_duel}{duel_instance.id}/')
        assert (
                resp.status_code == 403
        ), 'Ответ авторизованному невладелецу приходит не со статусом 403'

    @pytest.mark.django_db(transaction=True)
    def test_get_invalid_duel(self, moderator_client, duel_instance):
        invalid_duel_pk = 99999999999  # This duel does not exist
        resp = moderator_client.get(f'{self.url_duel}{invalid_duel_pk}/')
        assert (
                resp.status_code == 404
        ), 'Ответ при несуществующем объекте приходит не со статусом 404'

    @pytest.mark.django_db(transaction=True)
    def test_get_duel_owner(self, moderator_client, duel_instance):
        resp = moderator_client.get(f'{self.url_duel}{duel_instance.id}/')
        assert (
                resp.status_code == 200
        ), 'Ответ авторизованному владелецу приходит не со статусом 200'

        assert (
                len(resp.json().get('questions'))
                == duel_instance.questions.count()
        ), 'Кол-во вопросов не совпадает с кол-вом в базе'

        assert (
                len(resp.json().get('players'))
                == duel_instance.players.count()
        ), 'Кол-во игроков не совпадает с кол-вом в базе'

    @pytest.mark.django_db(transaction=True)
    def test_patch_duel_not_auth(self, client, duel_instance):
        resp = client.patch(f'{self.url_duel}{duel_instance.id}/')
        assert (
                resp.status_code == 401
        ), 'Ответ неавторизованному приходит не со статусом 401'

    @pytest.mark.django_db(transaction=True)
    def test_patch_duel_not_owner(self, user_client, duel_instance):
        resp = user_client.patch(f'{self.url_duel}{duel_instance.id}/')
        assert (
                resp.status_code == 403
        ), 'Ответ авторизованному невладелецу приходит не со статусом 403'

    @pytest.mark.django_db(transaction=True)
    def test_duel_update(self, moderator_client, duel_instance):
        player_ids = duel_instance.players.values_list('id', flat=True)
        question_ids = duel_instance.questions.values_list('id', flat=True)

        data = {
            'winner_id': player_ids[0],
            'question_id': question_ids[0],
        }

        resp = moderator_client.patch(
            f'{self.url_duel}{duel_instance.id}/',
            data=data,
            format='json',
        )
        assert (
                resp.status_code == 200
        ), 'Ответ после обновления приходит не со статусом 200'

        # Check that the duel instance was correctly updated
        assert (
                duel_instance.players.get(
                    id=data['winner_id']).good_answers_count == 1
        ), 'Счет победителя не был увеличен'
        assert (
            duel_instance.questions.get(id=data['question_id']).is_answered
        ), 'Поле is_answered вопроса не установлено в True'

    @pytest.mark.django_db(transaction=True)
    def test_duel_update_invalid_winner(self, moderator_client, duel_instance):
        question_ids = duel_instance.questions.values_list('id', flat=True)

        invalid_data = {
            'winner_id': 123456789,  # This player does not exist
            'question_id': question_ids[0],
        }

        resp = moderator_client.patch(
            f'{self.url_duel}{duel_instance.id}/',
            data=invalid_data,
            format='json',
        )
        assert (
                resp.status_code == 404
        ), ('Ответ при указании несуществующего игрока '
            'не приходит со статусом 404')

    @pytest.mark.django_db(transaction=True)
    def test_duel_update_invalid_question(
            self,
            moderator_client,
            duel_instance,
    ):
        player_ids = duel_instance.players.values_list(
            'id',
            flat=True,
        )

        invalid_data = {
            'winner_id': player_ids[0],
            'question_id': 123456789,  # This question does not exist
        }

        resp = moderator_client.patch(
            f'{self.url_duel}{duel_instance.id}/',
            data=invalid_data,
            format='json',
        )
        assert (
                resp.status_code == 404
        ), ('Ответ при указании несуществующего '
            'вопроса не приходит со статусом 404')

    @pytest.mark.django_db(transaction=True)
    def test_duel_update_no_winner(self, moderator_client, duel_instance):
        question_ids = duel_instance.questions.values_list('id', flat=True)
        wrong_answers_count_initial = duel_instance.wrong_answers_count

        data = {
            'winner_id': -1,  # No winner
            'question_id': question_ids[0],
        }

        resp = moderator_client.patch(
            f'{self.url_duel}{duel_instance.id}/',
            data=data,
            format='json',
        )
        assert (
                resp.status_code == 200
        ), 'Ответ после обновления приходит не со статусом 200'

        duel_instance.refresh_from_db()

        assert (
                duel_instance.wrong_answers_count
                == wrong_answers_count_initial + 1
        ), 'Счетчик неправильных ответов не увеличен'

    @pytest.mark.django_db(transaction=True)
    def test_duel_update_question_already_answered(
            self,
            moderator_client,
            duel_instance,
    ):
        player_ids = duel_instance.players.values_list('id', flat=True)
        question_ids = duel_instance.questions.values_list('id', flat=True)

        # First update - should be successful
        data = {
            'winner_id': player_ids[0],
            'question_id': question_ids[0],
        }

        resp = moderator_client.patch(
            f'{self.url_duel}{duel_instance.id}/',
            data=data,
            format='json',
        )
        assert (
                resp.status_code == 200
        ), 'Ответ после обновления приходит не со статусом 200'

        # Second update - should fail because the question was already answered
        resp = moderator_client.patch(
            f'{self.url_duel}{duel_instance.id}/',
            data=data,
            format='json',
        )
        assert (
                resp.status_code == 400
        ), ('Ответ на обновление уже ответившего вопроса '
            'не имел кода статуса 400')
        assert (
                resp.json().get('detail') == 'Question is already answered!'
        ), ('Сообщение об ошибке при обновлении '
            'уже ответившего вопроса неверно')
