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
        if 'contacts' in contributor:
            contributor_contacts = contributor.get('contacts')[0]
            assert isinstance(contributor.get('contacts'), list)
            assert isinstance(contributor_contacts, dict)
            assert 'social_network' in contributor_contacts
            assert 'contact' in contributor_contacts

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
                'photo': 'team/image_for_tests.png',
            },
        )
        assert response.status_code == 405

    @pytest.mark.django_db
    def test_put_auth_user_not_allowed(self, client, admin_user, contributor):
        client.force_login(admin_user)
        response = client.put(
            f'{self.url_contributors}{contributor.id}/',
            data={
                'first_name': 'Новое имя',
                'last_name': 'Б',
                'middle_name': 'Nothing',
                'role': 'разработчик',
                'photo': 'team/image_for_tests.png',
            },
        )
        assert response.status_code == 405
