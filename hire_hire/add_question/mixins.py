from urllib.parse import urlencode

from django.contrib.admin.views.main import SEARCH_VAR
from django.http import QueryDict


class DefaultFilterMixin:

    def changelist_view(self, request, extra_context=None):
        if request.method == 'GET' and not request.GET:
            if hasattr(self, 'default_filters'):
                request.GET = QueryDict(
                    f'{urlencode(self.default_filters)}&{SEARCH_VAR}=',
                    encoding=request.encoding,
                )
            request.META['QUERY_STRING'] = request.GET.urlencode()
            print(request.META['QUERY_STRING'])
        return super().changelist_view(request, extra_context=extra_context)
