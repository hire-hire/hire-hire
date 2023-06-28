import pytest


class TestDuelApi:

    def setup_class(self):
        self.url_duel = '/api/v1/duel/'

    @pytest.mark.django_db(transaction=True)
    def test_duel_unavailable_not_auth(
            self,
            client,
            duel_data,
    ):
        resp_no_auth = client.post(self.url_duel, data=duel_data)

        assert resp_no_auth.status_code == 401, (f'Ответ неавторизованному '
                                                 f'от {self.url_duel}'
                                                 f'приходит не со '
                                                 f'статусом 401')

    @pytest.mark.django_db(transaction=True)
    def test_duel_unavailable_auth(
            self,
            user_client,
            duel_data,
    ):
        resp_auth = user_client.post(self.url_duel, data=duel_data)

        assert resp_auth.status_code == 403, ('Ответ немодератору, '
                                              'при создании дуэли '
                                              'приходит не со '
                                              'статусом 403')

    @pytest.mark.django_db(transaction=True)
    def test_duel_valid_data_only(
            self,
            moderator_1_client,
    ):
        invalid_datas = [
            {'question_count': 10},
            {'players': [{'name': 'Juan'}]},
        ]
        for data in invalid_datas:
            response = moderator_1_client.post(self.url_duel, data=data)

            assert response.status_code == 400, (f'Ответ от {self.url_duel} '
                                                 f'при некорректна дата '
                                                 f'приходит не со '
                                                 f'статусом 400')

    @pytest.mark.django_db(transaction=True)
    def test_duel_available_auth_moderator(
            self,
            moderator_1_client,
            all_questions,
            language_1,
            duel_data,
    ):
        data = duel_data
        data.update({'language': language_1.pk})
        resp_auth = moderator_1_client.post(
            self.url_duel,
            data=data,
            format='json',
        )
        assert resp_auth.status_code == 201, (f'Ответ авторизованному, '
                                              f'модератору от '
                                              f'{self.url_duel} '
                                              f'приходит не со '
                                              f'статусом 201')
        assert (
                len(resp_auth.json().get('questions'))
                == duel_data.get('question_count')
        ), 'Количество вопросов не совпадает с переданном количеством'
        assert (
                len(resp_auth.json().get('players'))
                == len(duel_data.get('players'))
        ), 'Количество игроков не совпадает с переданном количеством'

    @pytest.mark.django_db(transaction=True)
    def test_get_duel_not_auth(self, client, duel_instance):
        resp = client.get(f'{self.url_duel}{duel_instance.id}/')
        assert (
                resp.status_code == 401
        ), 'Ответ неавторизованному приходит не со статусом 401'

    @pytest.mark.django_db(transaction=True)
    def test_get_duel_not_moderator(self, user_client, duel_instance):
        resp = user_client.get(f'{self.url_duel}{duel_instance.id}/')
        assert (
                resp.status_code == 403
        ), 'Ответ авторизованному немодератору приходит не со статусом 403'

    @pytest.mark.django_db(transaction=True)
    def test_get_duel_not_owner(
            self,
            moderator_2_client,
            duel_instance,
    ):
        resp = moderator_2_client.get(
            f'{self.url_duel}{duel_instance.pk}/'
        )
        assert (
                resp.status_code == 404
        ), 'Ответ невладелцу дуэли приходит не со статусом 404'

    @pytest.mark.django_db(transaction=True)
    def test_get_invalid_duel(self, moderator_1_client, duel_instance):
        invalid_duel_pk = 99999999999
        resp = moderator_1_client.get(f'{self.url_duel}{invalid_duel_pk}/')
        assert (
                resp.status_code == 404
        ), 'Ответ при несуществующем объекте приходит не со статусом 404'

    @pytest.mark.django_db(transaction=True)
    def test_get_duel_owner(self, moderator_1_client, duel_instance):
        resp = moderator_1_client.get(f'{self.url_duel}{duel_instance.id}/')
        assert (
                resp.status_code == 200
        ), 'Ответ владелецу дуэли приходит не со статусом 200'

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
    def test_patch_duel_not_moderator(self, user_client, duel_instance):
        resp = user_client.patch(f'{self.url_duel}{duel_instance.id}/')
        assert (
                resp.status_code == 403
        ), 'Ответ немодератору дуэли приходит не со статусом 403'

    @pytest.mark.django_db(transaction=True)
    def test_patch_duel_not_owner(
            self,
            moderator_2_client,
            duel_instance,
    ):
        resp = moderator_2_client.patch(
            f'{self.url_duel}{duel_instance.pk}/'
        )
        assert (
                resp.status_code == 404
        ), 'Ответ невладелцу дуэли приходит не со статусом 404'

    @pytest.mark.django_db(transaction=True)
    def test_duel_update(self, moderator_1_client, duel_instance):
        player_ids = duel_instance.players.values_list('id', flat=True)
        question_ids = duel_instance.questions.values_list('id', flat=True)

        data = {
            'winner_id': player_ids[0],
            'question_id': question_ids[0],
        }

        resp = moderator_1_client.patch(
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
    def test_duel_update_invalid_winner(
            self,
            moderator_1_client,
            duel_instance,
    ):
        question_ids = duel_instance.questions.values_list('id', flat=True)

        invalid_data = {
            'winner_id': 123456789,
            'question_id': question_ids[0],
        }

        resp = moderator_1_client.patch(
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
            moderator_1_client,
            duel_instance,
    ):
        player_ids = duel_instance.players.values_list(
            'id',
            flat=True,
        )

        invalid_data = {
            'winner_id': player_ids[0],
            'question_id': 123456789,
        }

        resp = moderator_1_client.patch(
            f'{self.url_duel}{duel_instance.id}/',
            data=invalid_data,
            format='json',
        )
        assert (
                resp.status_code == 404
        ), ('Ответ при указании несуществующего '
            'вопроса не приходит со статусом 404')

    @pytest.mark.django_db(transaction=True)
    def test_duel_update_no_winner(self, moderator_1_client, duel_instance):
        question_ids = duel_instance.questions.values_list('id', flat=True)
        wrong_answers_count_initial = duel_instance.wrong_answers_count

        data = {
            'winner_id': -1,
            'question_id': question_ids[0],
        }

        resp = moderator_1_client.patch(
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
            moderator_1_client,
            duel_instance,
    ):
        player_ids = duel_instance.players.values_list('id', flat=True)
        question_ids = duel_instance.questions.values_list('id', flat=True)

        # First update - should be successful
        data = {
            'winner_id': player_ids[0],
            'question_id': question_ids[0],
        }

        resp = moderator_1_client.patch(
            f'{self.url_duel}{duel_instance.id}/',
            data=data,
            format='json',
        )
        assert (
                resp.status_code == 200
        ), 'Ответ после обновления приходит не со статусом 200'

        # Second update - should fail because the question was already answered
        resp = moderator_1_client.patch(
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
