from django.conf import settings
from rest_framework import serializers

from api_donation.models import Currency, Price


class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = (Currency.name.field.name,)


class PriceSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer().fields[Currency.name.field.name]

    class Meta:
        model = Price
        fields = '__all__'


class AcceptPayment(serializers.Serializer):
    amount = serializers.IntegerField()
    currency = serializers.ChoiceField(
        settings.DONATION.currencies,
    )
