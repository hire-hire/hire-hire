import pytest

from django.conf import settings


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(
        username='Polzovatel',
        password='123456qw'
    )


@pytest.fixture
def moderator(django_user_model):
    return django_user_model.objects.create_user(
        username='Pronin',
        password='t096789g',
        is_duel_moderator=True,
    )


@pytest.fixture
def user_token(user):
    from rest_framework_simplejwt.tokens import RefreshToken
    refresh = RefreshToken.for_user(user)

    return {
        'access': refresh.access_token
    }


@pytest.fixture
def user_client(user_token):
    from rest_framework.test import APIClient

    client = APIClient()
    client.credentials(
        HTTP_AUTHORIZATION=f'{settings.SIMPLE_JWT["AUTH_HEADER_TYPES"][0]} '
                           f'{user_token["access"]}'
    )
    return client
