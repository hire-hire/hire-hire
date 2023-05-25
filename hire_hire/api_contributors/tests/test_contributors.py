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
                assert field.name in test_contributor, (
                    f'Нет поля {field.name} '
                    f'в ответе {self.url_contributors}'
                )

    @pytest.mark.django_db
    def test_contributors_answer_type(self, client, contributor):
        response = client.get(self.url_contributors)
        assert response.status_code == 200
        contributors = response.json()
        assert isinstance(contributors, list)
        assert isinstance(contributors[0], dict)

    @pytest.mark.django_db
    def test_contributors_thumbnail_image(self, client, contributor):
        response = client.get(self.url_contributors)
        assert response.status_code == 200
        contributors = response.json()
        assert len(contributors) == 1
        assert 'thumbnail_image' in contributors[0]
        assert (contributors[0]['thumbnail_image'] ==
               contributor.thumbnail_image)

    @pytest.mark.django_db
    def test_contributors_contacts(
            self, client, contributor, contributor_contact1):
        response = client.get(self.url_contributors)
        contributor = response.json()[0]
        assert 'contacts' in contributor
        assert isinstance(contributor.get('contacts'), list) is True
        assert isinstance(contributor.get('contacts')[0], dict) is True
        assert 'social_network' in contributor.get('contacts')[0]
        assert 'contact' in contributor.get('contacts')[0]

    @pytest.mark.django_db
    def test_contributors_contacts_fields(
            self, client, contributor,
            contributor_contact1, contributor_contact2):
        response = client.get(self.url_contributors)
        contributor = response.json()[0]
        assert len(contributor.get('contacts')) == 2
        assert contributor.get('contacts')[0].get('social_network') == (
            contributor_contact1.social_network)
        assert contributor.get('contacts')[0].get('contact') == (
            contributor_contact1.contact)

    @pytest.mark.django_db
    def test_contributors_fields(self, client, contributor):
        response = client.get(self.url_contributors)
        contributor_api = response.json()[0]
        assert contributor_api.get('first_name') == contributor.first_name
        assert contributor_api.get('last_name') == contributor.last_name
        assert contributor_api.get('middle_name') == contributor.middle_name
        assert contributor_api.get('role') == contributor.role.name
        assert contributor_api.get('photo').endswith('team/image2.png')
        assert contributor_api.get('thumbnail_image') == (
            contributor.thumbnail_image)
