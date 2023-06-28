from django.conf import settings
import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture
def moderator_1(django_user_model):
    return django_user_model.objects.create_user(
        username='Roman',
        password='Password1',
        is_duel_moderator=True,
    )


@pytest.fixture
def moderator_2(django_user_model):
    return django_user_model.objects.create_user(
        username='Sergey',
        password='Password2',
        is_duel_moderator=True,
    )


@pytest.fixture
def moderator_1_token(moderator_1):
    refresh = RefreshToken.for_user(moderator_1)
    return refresh.access_token


@pytest.fixture
def moderator_2_token(moderator_2):
    refresh = RefreshToken.for_user(moderator_2)
    return refresh.access_token


@pytest.fixture
def moderator_1_client(moderator_1_token):
    client = APIClient()
    client.credentials(
        HTTP_AUTHORIZATION=f'{settings.SIMPLE_JWT["AUTH_HEADER_TYPES"][0]} '
                           f'{moderator_1_token}',
    )
    return client


@pytest.fixture
def moderator_2_client(moderator_2_token):
    client = APIClient()
    client.credentials(
        HTTP_AUTHORIZATION=f'{settings.SIMPLE_JWT["AUTH_HEADER_TYPES"][0]} '
                           f'{moderator_2_token}',
    )
    return client
