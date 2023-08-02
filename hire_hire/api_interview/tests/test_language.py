import pytest

from interview.models import Language


class TestLanguageAPI:

    def setup_class(self):
        self.url_language = '/api/v1/language/'

    @pytest.mark.django_db(transaction=True)
    def test_language_not_auth(self, client, category_1, language_1):
        response = client.get(self.url_language)

        assert response.status_code == 200, ('Подкатегории не отдаются '
                                             'авторизованному юзеру')

    @pytest.mark.django_db(transaction=True)
    def test_language_list_count(self, user_client, category_1,
                                 language_1, language_2):
        response = user_client.get(self.url_language)
        languages = response.json()

        assert isinstance(languages, list), ('Получение подкатегории '
                                             'не результирует в список')
        assert len(languages) == 2, ('Количество подкатегории '
                                     'не соответствует фикстуре')

    @pytest.mark.django_db(transaction=True)
    def test_language_fields(self, user_client, category_1, language_1):
        response = user_client.get(self.url_language)

        languages = response.json()
        test_lang = languages[0]
        for f in Language._meta.fields:
            assert f.name in test_lang,  (f'Нет поля {f.name}'
                                          f' в ответе '
                                          f'{self.url_language}')

    @pytest.mark.django_db(transaction=True)
    def test_language_list_available_not_auth(
            self, client, category_1, language_2,
    ):
        response = client.get(self.url_language)

        assert response.status_code == 200, ('Список подкатегорий '
                                             'недоступен без токена')

    @pytest.mark.django_db(transaction=True)
    def test_single_language_available_not_auth(
            self, client, category_1, language_2,
    ):

        response = client.get(
            self.url_language + f'{Language.objects.first().id}/',
        )

        assert response.status_code == 200, ('Конкретная подкатегория '
                                             'недоступна без токена')

    @pytest.mark.django_db(transaction=True)
    def test_language_list_available_auth(self, user_client,
                                          category_1, language_2):
        response = user_client.get(self.url_language)

        assert response.status_code == 200, ('Список подкатегорий '
                                             'недоступен с токеном')

    @pytest.mark.django_db(transaction=True)
    def test_single_language_available_auth(self, user_client,
                                            category_1, language_2):

        response = user_client.get(
            self.url_language + f'{Language.objects.first().id}/',
        )

        assert response.status_code == 200, ('Конкретная подкатегория '
                                             'недоступна с токеном')

    @pytest.mark.django_db(transaction=True)
    def test_language_non_exist(self, client, language_1,
                                category_1, language_2):
        response = client.get(self.url_language + '3/')

        assert response.status_code == 404, ('Не возвращается 404 ошибка '
                                             'при несуществующем объекте')
