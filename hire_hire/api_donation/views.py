from rest_framework.response import Response
from rest_framework.views import APIView

from api_donation.models import Currency, Price, IdempotenceKey
from api_donation.serializers import PriceSerializer
from api_donation.services import create_payment


class DonationView(APIView):

    def get(self, request):
        prices = Price.objects.all()
        serializer = PriceSerializer(data=prices, many=True)
        serializer.is_valid()
        return Response(serializer.data)

    def post(self, request):
        return create_payment()
