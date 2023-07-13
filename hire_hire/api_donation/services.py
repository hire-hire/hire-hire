from http import HTTPStatus

from api_donation.exceptions import (
    ERRORS_TO_RETURN,
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

    except YookassaBadRequest:
        return ERRORS_TO_RETURN[YookassaBadRequest]

    except YookassaForbidden:
        return ERRORS_TO_RETURN[YookassaForbidden]

    except YookassaInternalError:
        return ERRORS_TO_RETURN[YookassaInternalError]

    except YookassaInvalidCredentials:
        return ERRORS_TO_RETURN[YookassaInvalidCredentials]

    except YookassaMethodNotAllowed:
        return ERRORS_TO_RETURN[YookassaMethodNotAllowed]

    except YookassaNotFound:
        return ERRORS_TO_RETURN[YookassaNotFound]

    except YookassaTooManyRequests:
        return ERRORS_TO_RETURN[YookassaTooManyRequests]

    except YookassaUnsupportedMediaType:
        return ERRORS_TO_RETURN[YookassaUnsupportedMediaType]

    except CannotFindConfirmationURL:
        return ERRORS_TO_RETURN[CannotFindConfirmationURL]
