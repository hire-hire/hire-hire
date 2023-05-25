from io import BytesIO
import tempfile

from django.core.files.base import File
from PIL import Image
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
        photo='team/image2.png',
    )


@pytest.fixture
def image_file(name='image2.png', ext='png', size=(50, 50), color=(256, 0, 0)):
    file_obj = BytesIO()
    image = Image.new('RGBA', size=size, color=color)
    image.save(file_obj, ext)
    file_obj.seek(0)
    return File(file_obj, name=name)


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
