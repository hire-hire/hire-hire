from rest_framework import serializers

from interview.models import Category, Language
from contributors.models import ContributorContact, Contributor, TeamRole


class CategorySerializer(serializers.ModelSerializer):
    languages = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = '__all__'


class ContributorContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContributorContact
        fields = ('social_network', 'contact')


class ContributorSerializer(serializers.ModelSerializer):
    role = serializers.PrimaryKeyRelatedField(
        source='role.name', read_only=True)
    contacts = ContributorContactSerializer(many=True, read_only=True)

    class Meta:
        model = Contributor
        fields = '__all__'


class TeamRoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeamRole
        fields = '__all__'
