import uuid
import requests
from requests.auth import HTTPBasicAuth

from django.conf import settings
from django.db.utils import IntegrityError

from api_donation.models import IdempotenceKey


def create_idempotence_key():
    while True:
        try:
            key = uuid.uuid4()
            return IdempotenceKey.objects.create(value=key)
        except IntegrityError:
            continue


def create_payment(
        amount,
        currency=settings.DONATION.default_currency,
        capture=settings.DONATION.is_auto_capture_on,
        description=settings.DONATION.default_description,
):

    idempotence_key = str(create_idempotence_key())

    payment_data = {
        'amount': {
            'value': amount,
            'currency': currency,
        },
        'confirmation': {
            'type': 'redirect',
            'return_url': settings.DONATION.return_url,
        },
        'capture': capture,
        'description': description,
    }

    payment_headers = {
        'Idempotence-Key': idempotence_key,
        'Content-Type': 'application/json',
    }

    response = requests.post(
        settings.DONATION.api_url,
        json=payment_data,
        headers=payment_headers,
        auth=HTTPBasicAuth(
            settings.DONATION.shop_id,
            settings.DONATION.api_key,
        )
    )

    response = response.json()

    return response.get('confirmation').get('confirmation_url')
