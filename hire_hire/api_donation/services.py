from http import HTTPStatus

from api_donation.exceptions import (
    ERRORS_TO_RETURN,
    CannotFindConfirmationURL,
    YokassaBadRequest,
    YokassaForbidden,
    YookassaInternalError,
    YookassaInvalidCredentials,
    YokassaMethodNotAllowed,
    YookassaNotFound,
    YokassaTooManyRequests,
    YokassaUnsupportedMediaType,
)
from api_donation.payment import Payment


def create_payment(amount, currency):

    payment = Payment(amount, currency)

    try:
        return payment.create(), HTTPStatus.OK

    except YokassaBadRequest:
        return ERRORS_TO_RETURN[YokassaBadRequest]

    except YokassaForbidden:
        return ERRORS_TO_RETURN[YokassaForbidden]

    except YookassaInternalError:
        return ERRORS_TO_RETURN[YookassaInternalError]

    except YookassaInvalidCredentials:
        return ERRORS_TO_RETURN[YookassaInvalidCredentials]

    except YokassaMethodNotAllowed:
        return ERRORS_TO_RETURN[YokassaMethodNotAllowed]

    except YookassaNotFound:
        return ERRORS_TO_RETURN[YookassaNotFound]

    except YokassaTooManyRequests:
        return ERRORS_TO_RETURN[YokassaTooManyRequests]

    except YokassaUnsupportedMediaType:
        return ERRORS_TO_RETURN[YokassaUnsupportedMediaType]

    except CannotFindConfirmationURL:
        return ERRORS_TO_RETURN[CannotFindConfirmationURL]
