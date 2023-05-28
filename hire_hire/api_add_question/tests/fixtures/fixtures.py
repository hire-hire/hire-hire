from django.conf import settings
import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken

from interview.models import Category, Language


@pytest.fixture
def api_add_question_category_1():
    return Category.objects.create(title='Программирование')


@pytest.fixture
def api_add_question_category_2():
    return Category.objects.create(title='Тестирование')


@pytest.fixture
def api_add_question_language_1(api_add_question_category_1):
    return Language.objects.create(
        title='Javascript',
        category=api_add_question_category_1,
    )


@pytest.fixture
def api_add_question_language_2(api_add_question_category_1):
    return Language.objects.create(
        title='Python',
        category=api_add_question_category_1,
    )


@pytest.fixture
def api_add_question_language_3(api_add_question_category_1):
    return Language.objects.create(
        title='Java',
        category=api_add_question_category_1,
    )


@pytest.fixture
def api_add_question_user_1(django_user_model):
    return django_user_model.objects.create(
        username='some_user_1',
        password='Some_password_09876_1',
    )


@pytest.fixture
def api_add_question_user_2(django_user_model):
    return django_user_model.objects.create(
        username='some_user_2',
        password='Some_password_09876_2',
    )


@pytest.fixture
def api_add_question_get_token(api_add_question_user_1):
    return AccessToken.for_user(api_add_question_user_1)


@pytest.fixture
def api_client_auth_user(api_add_question_get_token):
    client = APIClient()
    auth_header_type = settings.SIMPLE_JWT['AUTH_HEADER_TYPES'][0]
    client.credentials(
        HTTP_AUTHORIZATION=f'{auth_header_type} {api_add_question_get_token}',
    )
    return client
