from django.http import QueryDict


class DefaultFilterMixin:

    def changelist_view(self, request, extra_context=None):
        if (
            request.method == 'GET'
            and not request.GET
            and hasattr(self, 'default_filters')
        ):
            request.GET = QueryDict('', mutable=True)
            request.GET.update(self.default_filters, q='')
        return super().changelist_view(request, extra_context=extra_context)
