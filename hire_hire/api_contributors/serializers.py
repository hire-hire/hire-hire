from sorl.thumbnail.shortcuts import get_thumbnail

from rest_framework import serializers

from contributors.models import Contributor, ContributorContact


class ContributorContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContributorContact
        fields = (
            ContributorContact.social_network.field.name,
            ContributorContact.contact.field.name,
        )


class ContributorSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField(read_only=True)
    contacts = ContributorContactSerializer(many=True, read_only=True)
    photo = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Contributor
        fields = (
            Contributor.first_name.field.name,
            Contributor.last_name.field.name,
            Contributor.middle_name.field.name,
            Contributor.photo.field.name,
            Contributor.role.field.name,
            Contributor.contacts.rel.name,
        )

    @staticmethod
    def get_role(model):
        return model.role.name

    @staticmethod
    def get_photo(model):
        return get_thumbnail(model.photo, '1000x1000').url
