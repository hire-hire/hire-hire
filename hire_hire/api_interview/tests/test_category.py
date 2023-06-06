import pytest

from interview.models import Category


class TestCategoryAPI:
    url_category = '/api/v1/category/'

    @pytest.mark.django_db(transaction=True)
    def test_category_not_auth(self, client, category_1):
        response = client.get(self.url_category)

        assert response.status_code == 200, ('Категории не отдаются '
                                             'авторизованному юзеру')

    @pytest.mark.django_db(transaction=True)
    def test_category_list_count(self, user_client, category_1, category_2):
        response = user_client.get(self.url_category)
        categories = response.json()

        assert type(categories) == list, ('Получение категорий '
                                          'не результирует в список')
        assert len(categories) == 2, ('Количество категорий '
                                      'не соответствует фикстуре')

    @pytest.mark.django_db(transaction=True)
    def test_category_fields(self, user_client, category_1):
        response = user_client.get(self.url_category)

        categories = response.json()
        test_category = categories[0]
        for field in Category._meta.fields:
            is_field_found = (field.name in test_category)
            assert is_field_found is True,  (f'Нет поля {field.name} '
                                             f'в ответе {self.url_category}')

    @pytest.mark.django_db(transaction=True)
    def test_category_available_not_auth(self, client, category_1):
        response = client.get(self.url_category)

        assert response.status_code == 200, ('Список категорий '
                                             'недоступен без токена')

        response = client.get(
            self.url_category + f'{Category.objects.first().id}/'
        )

        assert response.status_code in [200, 301], ('Конкретная категория'
                                                    ' недоступна без токена')

    @pytest.mark.django_db(transaction=True)
    def test_category_available_auth(self, user_client, category_1):
        response = user_client.get(self.url_category)

        assert response.status_code == 200, ('Список категорий '
                                             'недоступен с токеном')

        response = user_client.get(
            self.url_category + f'{Category.objects.first().id}/'
        )

        assert response.status_code in [200, 301], ('Конкретная категория'
                                                    ' недоступна с токеном')

    @pytest.mark.django_db(transaction=True)
    def test_category_non_exist(self, client, category_1, category_2):
        response = client.get(self.url_category + '3/')

        assert response.status_code == 404, ('Не возвращается 404 '
                                             'ошибка при несуществующем '
                                             'объекте')
