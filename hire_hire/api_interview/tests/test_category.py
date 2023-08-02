import pytest

from interview.models import Category


class TestCategoryAPI:

    def setup_class(self):
        self.url_category = '/api/v1/category/'

    @pytest.mark.django_db(transaction=True)
    def test_category_not_auth(self, client, category_1):
        response = client.get(self.url_category)

        assert response.status_code == 200, ('Категории не отдаются '
                                             'неавторизованному юзеру')

    @pytest.mark.django_db(transaction=True)
    def test_category_correct_data(self, user_client, category_1, category_2):
        response = user_client.get(self.url_category)
        categories = response.json()

        assert isinstance(categories, list), ('Получение категорий '
                                              'не результирует в список')
        assert len(categories) == 2, ('Количество категорий '
                                      'не соответствует фикстуре')

        title = categories[0]['title']

        assert title == category_1.title, ('Название первой '
                                           'категории не совпадает '
                                           'с ожидаемым')

    @pytest.mark.django_db(transaction=True)
    def test_category_fields(self, user_client, category_1):
        response = user_client.get(self.url_category)

        categories = response.json()
        test_category = categories[0]
        for field in Category._meta.fields:
            assert field.name in test_category, (
                f'Нет поля {field.name} в ответе {self.url_category}'
            )

    @pytest.mark.django_db(transaction=True)
    def test_category_list_available_not_auth(self, client, category_1):
        response = client.get(self.url_category)

        assert response.status_code == 200, ('Список категорий '
                                             'недоступен без токена')

    @pytest.mark.django_db(transaction=True)
    def test_single_category_available_not_auth(self, client, category_1):

        response = client.get(
            self.url_category + f'{Category.objects.first().id}/'
        )

        assert response.status_code == 200, ('Конкретная категория'
                                             'недоступна без токена')

    @pytest.mark.django_db(transaction=True)
    def test_category_list_available_auth(self, user_client, category_1):
        response = user_client.get(self.url_category)

        assert response.status_code == 200, ('Список категорий '
                                             'недоступен с токеном')

    @pytest.mark.django_db(transaction=True)
    def test_single_category_available_auth(self, user_client, category_1):

        response = user_client.get(
            self.url_category + f'{Category.objects.first().id}/'
        )

        assert response.status_code == 200, ('Конкретная категория '
                                             'недоступна с токеном')

    @pytest.mark.django_db(transaction=True)
    def test_category_non_exist(self, client, category_1, category_2):
        response = client.get(self.url_category + '3/')

        assert response.status_code == 404, ('Не возвращается 404 '
                                             'ошибка при несуществующем '
                                             'объекте')
