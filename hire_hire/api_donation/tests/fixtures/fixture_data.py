import pytest
from rest_framework.test import APIClient

from api_donation.models import Currency, Price


@pytest.fixture()
def currency_rub():
    return Currency.objects.create(name='RUB')


@pytest.fixture()
def price_100(currency_rub):
    return Price.objects.create(
        value=100,
        currency=currency_rub,
    )


@pytest.fixture()
def price_200(currency_rub):
    return Price.objects.create(
        value=200,
        currency=currency_rub,
    )


@pytest.fixture()
def price_300(currency_rub):
    return Price.objects.create(
        value=300,
        currency=currency_rub,
    )

@pytest.fixture()
def some_client():
    client = APIClient()
    return client
