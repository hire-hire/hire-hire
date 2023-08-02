import pytest

from api_contributors.serializers import ContributorSerializer


class TestContributorsApi:

    def setup_class(self):
        self.url_contributors = '/api/v1/contributors/'

    @pytest.mark.django_db
    def test_get_contributors(self, client):
        response = client.get(self.url_contributors)
        assert response.status_code == 200

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
        test_contributor = contributors[0]
        assert 'thumbnail_image' in test_contributor
        assert (test_contributor['thumbnail_image'] ==
                contributor.thumbnail_image)

    @pytest.mark.django_db
    def test_contributors_contacts(
            self, client, contributor, contributor_contact1):
        response = client.get(self.url_contributors)
        assert response.status_code == 200
        response = response.json()
        assert len(response) != 0
        contributor = response[0]
        assert 'contacts' in contributor
        list_contacts = contributor.get('contacts')
        assert len(list_contacts) != 0
        assert isinstance(list_contacts, list)
        contributor_contact = list_contacts[0]
        assert isinstance(contributor_contact, dict)
        assert 'social_network' in contributor_contact
        assert 'contact' in contributor_contact

    @pytest.mark.django_db
    def test_contributors_contacts_fields(
            self, client, contributor,
            contributor_contact1, contributor_contact2):
        response = client.get(self.url_contributors)
        assert response.status_code == 200
        response = response.json()
        assert len(response) != 0
        contributor_contacts = response[0].get('contacts')
        assert len(contributor_contacts) == 2
        test_contact = contributor_contacts[0]
        assert test_contact.get('social_network') == (
            contributor_contact1.social_network)
        assert test_contact.get('contact') == (
            contributor_contact1.contact)

    @pytest.mark.django_db
    def test_get_contributor_serializer_fields(self, client, contributor):
        response = client.get(self.url_contributors)
        assert response.status_code == 200
        response = response.json()
        assert len(response) != 0
        test_contributor = response[0]
        for field in ContributorSerializer.Meta.fields:
            if field != 'id':
                assert field in test_contributor, (
                    f'Нет поля {field} '
                    f'в ответе {self.url_contributors}'
                )

    @pytest.mark.django_db
    def test_post_auth_user_not_allowed(self, client, admin_user):
        client.force_login(admin_user)
        response = client.post(
            self.url_contributors,
            data={
                'first_name': 'Тихон',
                'last_name': 'Б',
                'middle_name': 'Nothing',
                'role': 'разработчик',
                'photo': 'fixtures/image_for_tests.jpg',
            },
        )
        assert response.status_code == 405
