import datetime

from django.conf import settings
from django.urls import reverse
import pytest

from add_question.models import AddQuestion

# from interview.models import Language


class TestApiAddQuestion:
    # @pytest.mark.django_db
    # def test_get_languages(
    #     self,
    #     client,
    #     api_add_question_language_1,
    #     api_add_question_language_2,
    #     api_add_question_language_3,
    # ):
    #     url = '/api/v1/language/'
    #     response = client.get(url)
    #     assert (
    #         response.status_code == 200
    #     ), 'Статус код не верный при запросе языков!!! Проблемы с фикстурами.'
    #     assert Language.objects.count() == 3, 'Проблемы с фикстурами языков!!!'
    #     assert (
    #         response.data[1]['title'] == api_add_question_language_2.title
    #     ), 'Субкатегория не совпадает!!! Фикстуры языков не верны.'

    @pytest.mark.django_db
    def test_add_question_unauthorized_user(
        self,
        client,
        api_add_question_language_1,
        api_add_question_language_2,
        api_add_question_language_3,
    ):
        url = reverse('api:api_add_question:add_question-list')

        assert not AddQuestion.objects.exists(), 'В базе уже есть вопросы!!!'

        for i in range(1, settings.LIMIT_ADD_QUESTIONS_PER_DAY + 1):
            data = {
                'text': f'Вопрос номер {i}?',
                'answer': f'Ответ номер {i}',
                'language': api_add_question_language_2.id,
            }
            response = client.post(
                path=url,
                data=data,
            )
            assert (
                response.status_code == 201
            ), 'Статус код не верный при добавлении вопроса!!!'
            assert AddQuestion.objects.count() == i, 'Вопрос не добавился!!!'

            last_added_question = AddQuestion.objects.get(id=i)
            assert (
                last_added_question.text == f'Вопрос номер {i}?'
            ), 'Текст вопроса не совпадает!!!'
            assert (
                last_added_question.answer == f'Ответ номер {i}'
            ), 'Ответ не совпадает!!!'
            assert (
                last_added_question.language == api_add_question_language_2
            ), 'Субкатегория не совпадает!!!'
            assert (
                last_added_question.status == AddQuestion.StatusChoice.PROPOSED
            ), 'Статус не совпадает!!!'
            assert (
                last_added_question.author is None
            ), 'У анонима автор не None!!!'
            assert (
                last_added_question.user_cookie_id is not None
            ), 'У анонима user_cookie_id None!!!'

        assert (
            AddQuestion.objects.count() == settings.LIMIT_ADD_QUESTIONS_PER_DAY
        ), 'В базе странное количество вопросов!!!'

        data = {
            'text': 'Вопрос на котором лимит исчерпан?',
            'answer': 'Ответ на котором лимит исчерпан',
            'language': api_add_question_language_2.id,
        }
        response = client.post(
            path=url,
            data=data,
        )
        assert (
            response.status_code == 400
        ), 'Статус код не верный, лимит не сработал!!!'
        # AddQuestion.objects.create(
        #     text='Вопрос на котором лимит исчерпан?',
        #     answer='Ответ на котором лимит исчерпан',
        #     language=api_add_question_language_2,
        # )
        assert not AddQuestion.objects.filter(
            text=data.get('text'),
            answer=data.get('answer'),
            language=api_add_question_language_2,
        ).exists(), 'Вопрос на котором лимит исчерпан добавился в базу!!!'
        assert (
            AddQuestion.objects.count() == 10
        ), 'Странное количество вопросов в базе!!!'

    @pytest.mark.django_db
    def test_add_question_authorized_user(
        self,
        api_add_question_user_1,
        api_client_auth_user,
        api_add_question_language_1,
        api_add_question_language_2,
        api_add_question_language_3,
    ):
        url = reverse('api:api_add_question:add_question-list')

        assert not AddQuestion.objects.exists(), 'В базе уже есть вопросы!!!'

        for i in range(1, settings.LIMIT_ADD_QUESTIONS_PER_DAY + 1):
            data = {
                'text': f'Вопрос номер {i}?',
                'answer': f'Ответ номер {i}',
                'language': api_add_question_language_2.id,
            }
            response = api_client_auth_user.post(
                path=url,
                data=data,
            )
            assert (
                response.status_code == 201
            ), 'Статус код не верный при добавлении вопроса!!!'
            assert AddQuestion.objects.count() == i, 'Вопрос не добавился!!!'

            last_question = AddQuestion.objects.get(id=i)
            assert (
                last_question.text == f'Вопрос номер {i}?'
            ), 'Текст вопроса не совпадает!!!'
            assert (
                last_question.answer == f'Ответ номер {i}'
            ), 'Ответ не совпадает!!!'
            assert (
                last_question.language == api_add_question_language_2
            ), 'Субкатегория не совпадает!!!'
            assert (
                last_question.status == AddQuestion.StatusChoice.PROPOSED
            ), 'Статус не совпадает!!!'
            assert (
                last_question.author == api_add_question_user_1
            ), 'У автоизированного пользователя автор не совпадает!!!'
            assert (
                last_question.user_cookie_id is None
            ), 'У автоизированного пользователя user_cookie_id не None!!!'

        assert (
            AddQuestion.objects.count() == settings.LIMIT_ADD_QUESTIONS_PER_DAY
        ), 'В базе странное количество вопросов!!!'

        data = {
            'text': 'Вопрос на котором лимит исчерпан?',
            'answer': 'Ответ на котором лимит исчерпан',
            'language': api_add_question_language_2.id,
        }
        response = api_client_auth_user.post(
            path=url,
            data=data,
        )
        assert (
            response.status_code == 400
        ), 'Статус код не верный, лимит не сработал!!!'
        assert not AddQuestion.objects.filter(
            text=data.get('text'),
            answer=data.get('answer'),
            language=api_add_question_language_2,
        ).exists(), 'Вопрос на котором лимит исчерпан добавился в базу!!!'
        assert (
            AddQuestion.objects.count() == 10
        ), 'Странное количество вопросов в базе!!!'

    @pytest.mark.django_db
    def test_add_question_with_not_allowed_fields(
        self,
        api_add_question_user_1,
        api_add_question_user_2,
        api_client_auth_user,
        api_add_question_language_1,
        api_add_question_language_2,
        api_add_question_language_3,
    ):
        url = reverse('api:api_add_question:add_question-list')

        assert AddQuestion.objects.count() == 0, 'В базе уже есть вопросы!!!'

        some_datatime = datetime.datetime(2020, 1, 1, 1, 1, 1, 1)

        data = {
            'text': 'Вопрос номер 1?',
            'answer': 'Ответ номер 1',
            'language': api_add_question_language_2.id,
            # not_allowed_field
            'author': api_add_question_user_2,
            'ip_address': '8:8:8:8',
            'pub_date': some_datatime,
            'status': AddQuestion.StatusChoice.APPROVED,
            'user_cookie_id': 'some_fake_user_cookie_id',
        }
        response = api_client_auth_user.post(
            path=url,
            data=data,
        )
        assert (
            response.status_code == 201
        ), 'Статус код не верный при добавлении вопроса!!!'
        assert AddQuestion.objects.count() == 1, 'Вопрос не добавился!!!'

        added_question_with_wrong_data = AddQuestion.objects.get(id=1)
        assert (
            added_question_with_wrong_data.author == api_add_question_user_1
        ), 'Подмена автора!!!'
        assert (
            added_question_with_wrong_data.ip_address == '127.0.0.1'
        ), 'Подмена IP!!!'
        assert (
            added_question_with_wrong_data.pub_date != some_datatime
        ), 'Подмена даты публикации!!!'
        assert (
            added_question_with_wrong_data.status
            == AddQuestion.StatusChoice.PROPOSED
        ), 'Подмена статуса!!!'
        assert (
            added_question_with_wrong_data.user_cookie_id
            != 'some_fake_user_cookie_id'
        ), 'Подмена user_cookie_id!!!'
