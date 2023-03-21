from urllib.parse import urlencode

from django.contrib.admin.views.main import SEARCH_VAR
from django.http import HttpRequest, QueryDict


class DefaultFilterMixin:
    default_filters: None

    def get_default_filters(self, request: HttpRequest):
        return self.default_filters

    def changelist_view(self, request: HttpRequest, extra_context=None):
        if request.method == 'GET' and not request.GET:
            if default_filters := self.get_default_filters(request):
                request.GET = QueryDict(
                    f'{urlencode(default_filters)}&{SEARCH_VAR}=',
                    encoding=request.encoding,
                )
                request.META['QUERY_STRING'] = request.GET.urlencode()

        return super().changelist_view(request, extra_context=extra_context)
