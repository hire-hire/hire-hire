from django.conf import settings
import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture
def moderator(django_user_model):
    return django_user_model.objects.create_user(
        username='Roman',
        password='d1f5d68edc9',
        is_duel_moderator=True,
    )


@pytest.fixture
def moderator_token(moderator):
    refresh = RefreshToken.for_user(moderator)
    return refresh.access_token


@pytest.fixture
def moderator_client(moderator_token):
    client = APIClient()
    client.credentials(
        HTTP_AUTHORIZATION=f'{settings.SIMPLE_JWT["AUTH_HEADER_TYPES"][0]} '
                           f'{moderator_token}'
    )
    return client
