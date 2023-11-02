import pytest


class TestDonationAPI:

    def setup_class(self):
        self.url = '/api/v1/donation/'

    @pytest.mark.django_db(transaction=True)
    def test_get_correct_data(
            self,
            some_client,
            price_100,
    ):
        response = some_client.get(self.url)
        assert response.status_code == 200, ('При запросе прайсов '
                                             'неожиданный код ответа')

        prices = response.json()
        assert isinstance(prices, list), 'Прайсы пришли не списком'

        amount = prices[0]['value']
        assert amount == price_100.value, ('Некорректная сумма '
                                           'первого платежа')

    @pytest.mark.django_db(transaction=True)
    def test_post_incorrect_data(
            self,
            some_client,
    ):
        data = {'amount': 300, 'currency': 'NOT_CORRECT_VALUE'}
        response = some_client.post(self.url, data=data)
        assert response.status_code == 400, ('При запросе на создание '
                                             'платежа с невалид валютой'
                                             'неожиданный код ответа')
