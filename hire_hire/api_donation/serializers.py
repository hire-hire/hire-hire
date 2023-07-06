from rest_framework import serializers

from api_donation.models import Price


class PriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Price
        fields = '__all__'
