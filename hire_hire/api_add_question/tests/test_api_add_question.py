from django.conf import settings
from django.urls import reverse
import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken

from add_question.models import AddQuestion
from interview.models import Category, Language


@pytest.fixture
def category_1():
    return Category.objects.create(title='Программирование')


@pytest.fixture
def category_2():
    return Category.objects.create(title='Тестирование')


@pytest.fixture
def language_1(category_1):
    return Language.objects.create(title='Javascript', category=category_1)


@pytest.fixture
def language_2(category_1):
    return Language.objects.create(title='Python', category=category_1)


@pytest.fixture
def language_3(category_1):
    return Language.objects.create(title='Java', category=category_1)


@pytest.fixture
def api_client_unauth_user():
    return APIClient()


@pytest.fixture
def api_client_auth_user(django_user_model):
    auth_user = django_user_model.objects.create(
        username='some_user',
        password='Some_password_09876',
    )
    token = str(AccessToken.for_user(auth_user))
    client = APIClient()
    auth_header_type = settings.SIMPLE_JWT['AUTH_HEADER_TYPES'][0]
    client.credentials(HTTP_AUTHORIZATION=auth_header_type + ' ' + token)
    return client


@pytest.mark.django_db
def test_get_languages(
    api_client_unauth_user, language_1, language_2, language_3
):
    """Проверка фикстур языка."""
    url = '/api/v1/language/'
    response = api_client_unauth_user.get(url)
    assert response.status_code == 200, 'Ошибка при запросе языков!!!'
    assert Language.objects.count() == 3, 'Проблемы с фикстурами языков!!!'
    assert response.data[1]['title'] == 'Python'


@pytest.mark.django_db
def test_add_question_unauth(
    api_client_unauth_user, language_1, language_2, language_3
):
    """Проверка добавления вопроса анонимом."""
    url = reverse('api:api_add_question:add_question-list')

    assert AddQuestion.objects.count() == 0, 'В базе уже есть вопросы!!!'

    for i in range(1, settings.LIMIT_ADD_QUESTIONS_PER_DAY + 1):
        data = {
            'text': f'Вопрос номер {i}?',
            'answer': f'Ответ номер {i}',
            'language': 2,
        }
        response = api_client_unauth_user.post(
            path=url,
            data=data,
        )
        assert response.status_code == 201, 'Ошибка при добавлении вопроса!!!'
        assert AddQuestion.objects.count() == i, 'Вопрос не добавился!!!'
        assert AddQuestion.objects.last().text == f'Вопрос номер {i}?'
        assert AddQuestion.objects.last().answer == f'Ответ номер {i}'
        assert AddQuestion.objects.last().language.title == 'Python'
        assert AddQuestion.objects.last().status == 'proposed'
        assert AddQuestion.objects.last().author is None
        assert AddQuestion.objects.last().user_cookie_id is not None

    assert AddQuestion.objects.count() == settings.LIMIT_ADD_QUESTIONS_PER_DAY

    data = {
        'text': 'Вопрос на котором лимит исчерпан?',
        'answer': 'Ответ на котором лимит исчерпан',
        'language': 2,
    }
    response = api_client_unauth_user.post(
        path=url,
        data=data,
    )
    assert response.status_code == 400, 'Лимит не сработал!!!'


@pytest.mark.django_db
def test_add_question_auth(
    api_client_auth_user, language_1, language_2, language_3
):
    """Проверка добавления вопроса авторизованным пользователем."""
    url = reverse('api:api_add_question:add_question-list')

    assert AddQuestion.objects.count() == 0, 'В базе уже есть вопросы!!!'

    for i in range(1, settings.LIMIT_ADD_QUESTIONS_PER_DAY + 1):
        data = {
            'text': f'Вопрос номер {i}?',
            'answer': f'Ответ номер {i}',
            'language': 2,
        }
        response = api_client_auth_user.post(
            path=url,
            data=data,
        )
        assert response.status_code == 201, 'Ошибка при добавлении вопроса!!!'
        assert AddQuestion.objects.count() == i, 'Вопрос не добавился!!!'
        assert AddQuestion.objects.last().text == f'Вопрос номер {i}?'
        assert AddQuestion.objects.last().answer == f'Ответ номер {i}'
        assert AddQuestion.objects.last().language.title == 'Python'
        assert AddQuestion.objects.last().status == 'proposed'
        assert AddQuestion.objects.last().author.username == 'some_user'
        assert AddQuestion.objects.last().user_cookie_id is None

    assert AddQuestion.objects.count() == settings.LIMIT_ADD_QUESTIONS_PER_DAY

    data = {
        'text': 'Вопрос на котором лимит исчерпан?',
        'answer': 'Ответ на котором лимит исчерпан',
        'language': 2,
    }
    response = api_client_auth_user.post(
        path=url,
        data=data,
    )
    assert response.status_code == 400, 'Лимит не сработал!!!'
