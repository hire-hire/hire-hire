from http import HTTPStatus

from api_donation.exceptions import (
    CannotFindConfirmationURL,
    YookassaBadRequest,
    YookassaForbidden,
    YookassaInternalError,
    YookassaInvalidCredentials,
    YookassaMethodNotAllowed,
    YookassaNotFound,
    YookassaTooManyRequests,
    YookassaUnsupportedMediaType,
)
from api_donation.payment import Payment


def create_payment(amount, currency):

    payment = Payment(amount, currency)

    try:
        return payment.create(), HTTPStatus.OK

    except (CannotFindConfirmationURL, YookassaBadRequest,
            YookassaForbidden, YookassaInternalError,
            YookassaInvalidCredentials, YookassaMethodNotAllowed,
            YookassaNotFound, YookassaTooManyRequests,
            YookassaUnsupportedMediaType) as e:
        return e.args
