import logging

from rest_framework.response import Response
from rest_framework.views import APIView

from api_donation.models import Price
from api_donation.serializers import AcceptPayment, PriceSerializer
from api_donation.services import create_payment


logger = logging.getLogger(__name__)


class DonationView(APIView):

    def get(self, request):
        prices = Price.objects.all()
        serializer = PriceSerializer(data=prices, many=True)
        serializer.is_valid()
        logger.debug('returning all prices')
        return Response(serializer.data)

    def post(self, request):
        serializer = AcceptPayment(data=request.data)
        serializer.is_valid(raise_exception=True)
        response, status = create_payment(
            serializer.validated_data.get('amount'),
            serializer.validated_data.get('currency'),
        )
        return Response(response, status=status)
