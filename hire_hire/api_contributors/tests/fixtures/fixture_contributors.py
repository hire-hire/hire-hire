import pytest

from contributors.models import Contributor, ContributorContact, TeamRole


@pytest.fixture
def team_role():
    return TeamRole.objects.create(
        name='разработчик',
    )


@pytest.fixture
def contributor(team_role):
    return Contributor.objects.create(
        first_name='Тихон',
        last_name='Б',
        role=team_role,
        middle_name=None,
        photo='fixtures/image_for_tests.jpg',
    )


@pytest.fixture
def thumbnail_image(contributor):
    return contributor.thumbnail_image


@pytest.fixture
def contributor_contact1(contributor):
    return ContributorContact.objects.create(
        contributor=contributor,
        contact='http://t.me/username',
        social_network='telegram',
    )


@pytest.fixture
def contributor_contact2(contributor):
    return ContributorContact.objects.create(
        contributor=contributor,
        contact='http://vk.com/username',
        social_network='vk',
    )


@pytest.fixture
def contributor_contact3(contributor):
    return ContributorContact.objects.create(
        contributor=contributor,
        contact='http://ok.ru/username',
        social_network='ok',
    )
