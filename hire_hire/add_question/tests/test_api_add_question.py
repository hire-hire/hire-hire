import json

from django.conf import settings
from django.urls import reverse
import pytest

from add_question.models import AddQuestion


class TestApiAddQuestion:
    def setup_class(self):
        self.url = reverse('api:add_question:add_question-list')

    @pytest.mark.django_db
    def test_add_question_unauthorized_user(
            self,
            client,
            add_question_language_1,
    ):
        assert AddQuestion.objects.count() == 0, 'В базе уже есть вопросы'
        data = [{
            'text': 'Super vopros?',
            'answer': 'Super otvet',
            'language': add_question_language_1.id,
        }]
        response = client.post(
            path=self.url,
            data=json.dumps(data),
            content_type='application/json',
        )
        assert (
                response.status_code == 401
        ), 'Неверный статус код, для неавторизованного юзера'
        assert (
                AddQuestion.objects.count() == 0
        ), 'В базу добавился вопрос от неавторизованного пользователя'

    @pytest.mark.django_db
    def test_add_question_authorized_user(
            self,
            add_question_user_1,
            api_client_auth_user,
            add_question_language_1,
    ):
        assert AddQuestion.objects.count() == 0, 'В базе уже есть вопросы'

        data = [
            {
                'text': f'Вопрос номер {i}?',
                'answer': f'Ответ номер {i}',
                'language': add_question_language_1.id,
            }
            for i in range(1, settings.LIMIT_ADD_QUESTIONS_PER_DAY + 1)
        ]
        response = api_client_auth_user.post(
            path=self.url,
            data=json.dumps(data),
            content_type='application/json',
        )

        assert (
                response.status_code == 201
        ), 'Статус код не верный при добавлении вопроса'

        assert AddQuestion.objects.count() == len(
            data,
        ), 'Вопрос не добавился'

        for i in range(1, settings.LIMIT_ADD_QUESTIONS_PER_DAY + 1):
            added_question = AddQuestion.objects.get(id=i)
            current_data = data[i - 1]
            assert (
                    added_question.text == current_data['text']
            ), 'Текст вопроса не совпадает'
            assert (
                    added_question.answer == current_data['answer']
            ), 'Ответ не совпадает'
            assert (
                    added_question.language == add_question_language_1
            ), 'Субкатегория не совпадает'
            assert (
                    added_question.status == AddQuestion.StatusChoice.PROPOSED
            ), 'Статус не совпадает'
            assert (
                    added_question.author == add_question_user_1
            ), 'Автор не совпадает'

        assert (
                AddQuestion.objects.count() ==
                settings.LIMIT_ADD_QUESTIONS_PER_DAY
        ), 'В базе неверное количество вопросов'

        data = {
            'text': 'Вопрос на котором лимит исчерпан?',
            'answer': 'Ответ на котором лимит исчерпан',
            'language': add_question_language_1.id,
        }
        response = api_client_auth_user.post(
            path=self.url,
            data=json.dumps([data]),
            content_type='application/json',
        )

        assert (
                response.status_code == 400
        ), 'Статус код не верный, лимит не сработал'

        assert not AddQuestion.objects.filter(
            text=data.get('text'),
            answer=data.get('answer'),
            language=add_question_language_1,
        ).exists(), 'Вопрос на котором лимит исчерпан добавился в базу'

        assert (
                AddQuestion.objects.count()
                == settings.LIMIT_ADD_QUESTIONS_PER_DAY
        ), 'В базе неверное количество вопросов'

    @pytest.mark.django_db
    def test_add_question_with_not_allowed_fields(
            self,
            add_question_user_1,
            add_question_user_2,
            api_client_auth_user,
            add_question_language_2,
    ):
        assert AddQuestion.objects.count() == 0, 'В базе уже есть вопросы'

        some_datetime = '2020-01-01 01:01:01'
        data = {
            'text': 'Вопрос номер 1?',
            'answer': 'Ответ номер 1',
            'language': add_question_language_2.id,
            # below not allowed field
            'author': add_question_user_2.id,
            'pub_date': some_datetime,
            'status': AddQuestion.StatusChoice.APPROVED,
        }
        response = api_client_auth_user.post(
            path=self.url,
            data=json.dumps([data]),
            content_type='application/json',
        )

        assert (
                response.status_code == 201
        ), 'Статус код не верный при добавлении вопроса'
        assert AddQuestion.objects.count() == 1, 'Вопрос не добавился'

        added_question_with_wrong_data = AddQuestion.objects.get(id=1)
        assert (
                added_question_with_wrong_data.author.id
                == add_question_user_1.id
        ), 'Подмена автора'

        assert (
                added_question_with_wrong_data.pub_date != some_datetime
        ), 'Подмена даты публикации'

        assert (
                added_question_with_wrong_data.status
                == AddQuestion.StatusChoice.PROPOSED
        ), 'Подмена статуса'
