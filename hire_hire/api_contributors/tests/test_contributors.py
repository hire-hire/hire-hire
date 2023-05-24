import pytest

from contributors.models import Contributor


class TestContributorsApi:

    def setup_class(self):
        self.url_contributors = '/api/v1/contributors/'

    @pytest.mark.django_db
    def test_get_contributors(self, client):
        response = client.get(self.url_contributors)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_contributors_fields(self, client, contributor):
        response = client.get(self.url_contributors)
        contributors = response.json()
        test_contributor = contributors[0]
        for field in Contributor._meta.fields:
            if field.name != 'id':
                is_field_found = (field.name in test_contributor)
                assert is_field_found, (
                    f'Нет поля {field.name} '
                    f'в ответе {self.url_contributors}'
                )

    @pytest.mark.django_db
    def test_contributors_answer_type(self, client, contributor):
        response = client.get(self.url_contributors)
        contributors = response.json()
        assert response.status_code == 200
        assert isinstance(contributors, list)
        assert isinstance(contributors[0], dict)

    @pytest.mark.django_db
    def test_contributors_thumbnail_image(self, client, contributor):
        response = client.get(self.url_contributors)
        contributors = response.json()
        assert response.status_code == 200
        assert 'thumbnail_image' in contributors[0]
        assert (contributors[0]['thumbnail_image'] ==
               contributor.thumbnail_image)

    @pytest.mark.django_db
    def test_contributors_contacts(
            self, client, contributor, contributor_contact1):
        response = client.get(self.url_contributors)
        contributors = response.json()
        assert 'contacts' in contributors[0]
        assert isinstance(contributors[0]['contacts'], list) is True
        assert isinstance(contributors[0]['contacts'][0], dict) is True
        assert 'social_network' in contributors[0]['contacts'][0]
        assert 'contact' in contributors[0]['contacts'][0]
