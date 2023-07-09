import uuid

from django.conf import settings
from django.db.utils import IntegrityError
from yookassa import Configuration, Payment

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
    Configuration.account_id = settings.DONATION.shop_id
    Configuration.secret_key = settings.DONATION.api_key

    idempotence_key = create_idempotence_key()
    payment = Payment.create(
        {
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
        },
        idempotence_key,
    )
    return payment.confirmation.confirmation_url
