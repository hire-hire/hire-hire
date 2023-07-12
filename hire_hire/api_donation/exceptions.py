from http import HTTPStatus


class CannotFindConfirmationURL(Exception):
    pass


class YookassaInvalidCredentials(Exception):
    pass


class YookassaInternalError(Exception):
    pass


class YookassaNotFound(Exception):
    pass


class YokassaBadRequest(Exception):
    pass


class YokassaForbidden(Exception):
    pass


class YokassaMethodNotAllowed(Exception):
    pass


class YokassaUnsupportedMediaType(Exception):
    pass


class YokassaTooManyRequests(Exception):
    pass


ERRORS_TO_RETURN = {
    CannotFindConfirmationURL: (
        'Не удается получить URL подтверждения оплаты',
        HTTPStatus.INTERNAL_SERVER_ERROR,
    ),
    YokassaBadRequest: (
        'Ошибка в запросе в платежному сервису',
        HTTPStatus.BAD_REQUEST,
    ),
    YokassaForbidden: (
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
    YokassaMethodNotAllowed: (
        'Недопустимый метод',
        HTTPStatus.METHOD_NOT_ALLOWED,
    ),
    YookassaNotFound: (
        'Платежный сервис недоступен',
        HTTPStatus.NOT_FOUND,
    ),
    YokassaTooManyRequests: (
        'Слишком много запросов к платежному сервису, попробуйте позднее',
        HTTPStatus.TOO_MANY_REQUESTS,
    ),
    YokassaUnsupportedMediaType: (
        'Некорректный тип контента',
        HTTPStatus.UNSUPPORTED_MEDIA_TYPE,
    )
}
