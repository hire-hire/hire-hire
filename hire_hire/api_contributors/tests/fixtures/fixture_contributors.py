# создать тестового contributor по модели Contributor
import pytest

from contributors.models import Contributor, ContributorContact, TeamRole


@pytest.fixture
def team_role():
    team_role = TeamRole.objects.create(
        name='разработчик'
    )
    return team_role


@pytest.fixture
def contributor(team_role):
    contributor = Contributor.objects.create(
        first_name='Тихон',
        last_name='Б',
        role=team_role,
        middle_name=None,
        photo='photo.jpg',
    )
    return contributor


@pytest.fixture
def thumbnail_image(contributor):
    thumbnail_image = contributor.thumbnail_image
    return thumbnail_image


@pytest.fixture
def contributor_contact1(contributor):
    contributor_contact1 = ContributorContact.objects.create(
        contributor=contributor,
        contact='http://t.me/username',
        social_network='telegram',
        )
    return contributor_contact1


@pytest.fixture
def contributor_contact2(contributor):
    contributor_contact2 = ContributorContact.objects.create(
        contributor=contributor,
        contact='http://vk.com/username',
        social_network='vk',
        )
    return contributor_contact2


@pytest.fixture
def contributor_contact3(contributor):
    contributor_contact3 = ContributorContact.objects.create(
        contributor=contributor,
        contact='http://ok.ru/username',
        social_network='ok',
        )
    return contributor_contact3
