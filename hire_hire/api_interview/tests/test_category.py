import pytest

from interview.models import Category


class TestCategoryAPI:

    @pytest.mark.django_db(transaction=True)
    def test_category_not_auth(self, client, category_1):
        response = client.get('/api/v1/category/')

        assert response.status_code == 200, 'Категории не отдаются авторизованному юзеру'

    @pytest.mark.django_db(transaction=True)
    def test_category_list_count(self, client):
        response = client.get('/api/v1/category')
        print(response)


