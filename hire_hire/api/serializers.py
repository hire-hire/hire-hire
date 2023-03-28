from rest_framework import serializers

from interview.models import Category, Language


class CategorySerializer(serializers.ModelSerializer):
    languages = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = '__all__'