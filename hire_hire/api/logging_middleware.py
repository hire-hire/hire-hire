import logging
import sys
import traceback

from django.utils.deprecation import MiddlewareMixin


logger = logging.getLogger(__name__)


class CatchErrorsMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        exc_type, exc_value, exc_traceback = sys.exc_info()
        stack = traceback.extract_tb(exc_traceback)
        string_to_unpack = stack.format()
        string_to_send = ""
        for s in string_to_unpack:
            string_to_send = string_to_send + s
        logger.error(string_to_send)
