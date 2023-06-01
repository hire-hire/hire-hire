import datetime

from django.conf import settings
from django.urls import reverse
import pytest

from add_question.models import AddQuestion


class TestApiAddQuestion:
    def setup_class(self):
        self.url = reverse('api:api_add_question:add_question-list')

    def _test_add_question(self, client, author, language):
        assert not AddQuestion.objects.exists(), 'В базе уже есть вопросы!!!'

        for i in range(1, settings.LIMIT_ADD_QUESTIONS_PER_DAY + 1):
            data = {
                'text': f'Вопрос номер {i}?',
                'answer': f'Ответ номер {i}',
                'language': language.id,
            }
            response = client.post(
                path=self.url,
                data=data,
            )
            assert (
                response.status_code == 201
            ), 'Статус код не верный при добавлении вопроса!!!'
            assert AddQuestion.objects.count() == i, 'Вопрос не добавился!!!'

            last_added_question = AddQuestion.objects.get(id=i)
            assert (
                last_added_question.text == data['text']
            ), 'Текст вопроса не совпадает!!!'
            assert (
                last_added_question.answer == data['answer']
            ), 'Ответ не совпадает!!!'
            assert (
                last_added_question.language == language
            ), 'Субкатегория не совпадает!!!'
            assert (
                last_added_question.status == AddQuestion.StatusChoice.PROPOSED
            ), 'Статус не совпадает!!!'
            assert (
                last_added_question.author == author
            ), 'Автор не совпадает!!!'
            assert (
                last_added_question.user_cookie_id is None
                if author
                else not None
            ), 'user_cookie_id не совпадает!!!'

        assert (
            AddQuestion.objects.count() == settings.LIMIT_ADD_QUESTIONS_PER_DAY
        ), 'В базе неверное количество вопросов!!!'

        data = {
            'text': 'Вопрос на котором лимит исчерпан?',
            'answer': 'Ответ на котором лимит исчерпан',
            'language': language.id,
        }
        response = client.post(
            path=self.url,
            data=data,
        )
        assert (
            response.status_code == 400
        ), 'Статус код не верный, лимит не сработал!!!'
        assert not AddQuestion.objects.filter(
            text=data.get('text'),
            answer=data.get('answer'),
            language=language,
        ).exists(), 'Вопрос на котором лимит исчерпан добавился в базу!!!'
        assert (
            AddQuestion.objects.count() == settings.LIMIT_ADD_QUESTIONS_PER_DAY
        ), 'В базе неверное количество вопросов!!!'

    @pytest.mark.django_db
    def test_add_question_unauthorized_user(
        self,
        client,
        api_add_question_language_1,
        api_add_question_language_2,
        api_add_question_language_3,
    ):
        self._test_add_question(
            client,
            None,
            api_add_question_language_2,
        )

    @pytest.mark.django_db
    def test_add_question_authorized_user(
        self,
        api_add_question_user_1,
        api_client_auth_user,
        api_add_question_language_1,
        api_add_question_language_2,
        api_add_question_language_3,
    ):
        self._test_add_question(
            api_client_auth_user,
            api_add_question_user_1,
            api_add_question_language_2,
        )

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
        assert AddQuestion.objects.count() == 0, 'В базе уже есть вопросы!!!'

        some_datatime = datetime.datetime(2020, 1, 1, 1, 1, 1, 1)

        data = {
            'text': 'Вопрос номер 1?',
            'answer': 'Ответ номер 1',
            'language': api_add_question_language_2.id,
            # below not allowed field
            'author': api_add_question_user_2,
            'ip_address': '8:8:8:8',
            'pub_date': some_datatime,
            'status': AddQuestion.StatusChoice.APPROVED,
            'user_cookie_id': 'some_fake_user_cookie_id',
        }
        response = api_client_auth_user.post(
            path=self.url,
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
            added_question_with_wrong_data.ip_address != data['ip_address']
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
            != data['user_cookie_id']
        ), 'Подмена user_cookie_id!!!'