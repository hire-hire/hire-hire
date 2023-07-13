from http import HTTPStatus


class CannotFindConfirmationURL(Exception):
    pass


class YookassaInvalidCredentials(Exception):
    pass


class YookassaInternalError(Exception):
    pass


class YookassaNotFound(Exception):
    pass


class YookassaBadRequest(Exception):
    pass


class YookassaForbidden(Exception):
    pass


class YookassaMethodNotAllowed(Exception):
    pass


class YookassaUnsupportedMediaType(Exception):
    pass


class YookassaTooManyRequests(Exception):
    pass


ERRORS_TO_RETURN = {
    CannotFindConfirmationURL: (
        'Не удается получить URL подтверждения оплаты',
        HTTPStatus.INTERNAL_SERVER_ERROR,
    ),
    YookassaBadRequest: (
        'Ошибка в запросе в платежному сервису',
        HTTPStatus.BAD_REQUEST,
    ),
    YookassaForbidden: (
        'Недостаточно прав для операции',
        HTTPStatus.FORBIDDEN,
    ),
    YookassaInternalError: (
        'Внутренняя ошибка платежного сервиса, попробуйте позднее',
        HTTPStatus.INTERNAL_SERVER_ERROR,
    ),
    YookassaInvalidCredentials: (
        'Ошибка аутентификации в платежном сервисе',
        HTTPStatus.UNAUTHORIZED,
    ),
    YookassaMethodNotAllowed: (
        'Недопустимый метод',
        HTTPStatus.METHOD_NOT_ALLOWED,
    ),
    YookassaNotFound: (
        'Платежный сервис недоступен',
        HTTPStatus.NOT_FOUND,
    ),
    YookassaTooManyRequests: (
        'Слишком много запросов к платежному сервису, попробуйте позднее',
        HTTPStatus.TOO_MANY_REQUESTS,
    ),
    YookassaUnsupportedMediaType: (
        'Некорректный тип контента',
        HTTPStatus.UNSUPPORTED_MEDIA_TYPE,
    )
}
