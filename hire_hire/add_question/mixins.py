from django.http import QueryDict


class DefaultFilterMixin:
    '''
    Default preselected filter.
    Just take this mixin in your YourClassAdmin and put default_filters field
    like this:
    class YourClassAdmin(DefaultFilterMixin, admin.ModelAdmin):
        default_filters = (('status__exact', 'default_preselected_status'),)
    .
    '''

    default_filters = None

    def changelist_view(self, request, extra_context=None):
        if (
            request.method == 'GET'
            and not request.GET
            and self.default_filters
        ):
            request.GET = QueryDict('', mutable=True)
            request.GET.update(self.default_filters, q='')
        return super().changelist_view(request, extra_context=extra_context)
