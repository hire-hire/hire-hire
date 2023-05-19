import pytest


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(
        username='Пользователь',
        password='123456qw'
    )


@pytest.fixture
def moderator(django_user_model):
    return django_user_model.objects.create_user(
        username='Пронин',
        password='t096789g',
        is_duel_moderator=True,
    )


@pytest.fixture
def user_token(user):
    from rest_framework_simplejwt.tokens import RefreshToken
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }


@pytest.fixture
def user_client(user_token):
    from rest_framework.test import APIClient

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'JWT {user_token["access"]}')
    return client
