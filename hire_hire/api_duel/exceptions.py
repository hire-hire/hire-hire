from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException


class QuestionAlreadyAnswered(APIException):
    status_code = 400
    default_detail = _('Question is already answered!')
    default_code = 'Bad Request'


class DuelPlayerDoesNotExist(APIException):
    status_code = 400
    default_detail = _('Player does not exists for this duel!')
    default_code = 'Bad Request'


class DuelQuestionDoesNotExist(APIException):
    status_code = 400
    default_detail = _('Question does not exists for this duel!')
    default_code = 'Bad Request'
