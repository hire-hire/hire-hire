from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException


class QuestionAlreadyAnswered(APIException):
    status_code = 400
    default_detail = _('Question is already answered!')
    default_code = 'Bad Request'
