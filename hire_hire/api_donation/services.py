import uuid

from django.conf import settings as sets
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
        currency=sets.DONATION_SETTINGS.get('default_currency'),
        capture=sets.DONATION_SETTINGS.get('is_auto_capture_on'),
        description=sets.DONATION_SETTINGS.get('default_description'),
):
    Configuration.account_id = sets.DONATION_SETTINGS.get('shop_id')
    Configuration.secret_key = sets.DONATION_SETTINGS.get('api_key')

    idempotence_key = create_idempotence_key()
    payment = Payment.create(
        {
            'amount': {
                'value': amount,
                'currency': currency,
            },
            'confirmation': {
                'type': 'redirect',
                'return_url': sets.DONATION_SETTINGS.get(
                    'return_url',
                ),
            },
            'capture': capture,
            'description': description,
        },
        idempotence_key,
    )
    return payment.confirmation.confirmation_url
