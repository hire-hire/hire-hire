import pytest

from contributors.models import Contributor

"""Реальный ответ АПИ:
{
        "first_name": "Тихон",
        "last_name": "Б",
        "middle_name": null,
        "photo": "http://127.0.0.1:8000/media/team/
                  AAclG-wk6XnOFYQgRgk_CEyYVMb.jpg",
        "role": "разработчик",
        "contacts": [
            {
                "social_network": "sfdsf",
                "contact": "http://sfs.tu"
            },
            {
                "social_network": "dfd",
                "contact": "http://asfda.ht"
            },
            {
                "social_network": "dfgd",
                "contact": "http://sf.he"
            }
        ],
        "thumbnail_image": "/media/cache/4b/e7/
                            be71ed3d1c81f02a3df915577832af2.jpg"
    },]
"""


class TestContributorsApi:
    url_contributors = '/api/v1/contributors/'

    @pytest.mark.django_db
    def test_get_contributors(self, client):
        response = client.get(self.url_contributors)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_contributors_fields(self, client, contributor):
        """Соответсвие полей ответа полям модели Contributor."""
        response = client.get(self.url_contributors)
        contributors = response.json()
        test_contributor = contributors[0]
        for field in Contributor._meta.fields:
            if field.name != 'id':
                is_field_found = (field.name in test_contributor)
                assert is_field_found is True, (
                    f'Нет поля {field.name} '
                    f'в ответе {self.url_contributors}'
                    )

    @pytest.mark.django_db
    def test_contributors_answer_type(self, client):
        """Ответ - список словарей."""
        response = client.get(self.url_contributors)
        assert response.status_code == 200
        assert isinstance(response.json(), list) is True
        if response.json():
            assert isinstance(response.json()[0], dict) is True

    @pytest.mark.django_db
    def test_contributors_thumbnail_image(self, client, contributor):
        """В ответе есть поле thumbnail_image."""
        response = client.get(self.url_contributors)
        assert response.status_code == 200
        assert 'thumbnail_image' in response.json()[0]
        assert (response.json()[0]['thumbnail_image'] ==
               contributor.thumbnail_image)

    @pytest.mark.django_db
    def test_contributors_contacts(self, client, contributor):
        """В ответе есть поле contacts, оно является списком со словарями
        с ключами 'social_network' и 'contact'."""
        response = client.get(self.url_contributors)
        assert 'contacts' in response.json()[0]
        assert isinstance(response.json()[0]['contacts'], list) is True
        if response.json()[0]['contacts']:
            assert isinstance(response.json()[0]['contacts'][0], dict) is True
            assert 'social_network' in response.json()[0]['contacts'][0]
            assert 'contact' in response.json()[0]['contacts'][0]
