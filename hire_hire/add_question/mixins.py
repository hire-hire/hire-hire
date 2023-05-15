import uuid

from django.http import QueryDict


class DefaultFilterMixin:
    """
    Default preselected filter.
    Just take this mixin in your YourClassAdmin and put default_filters field
    like this:
    class YourClassAdmin(DefaultFilterMixin, admin.ModelAdmin):
        default_filters = (('status__exact', 'default_preselected_status'),)
    .
    """

    default_filters = None

    def changelist_view(self, request, extra_context=None):
        if (
            request.method == 'GET'
            and not request.GET
            and self.default_filters is not None
        ):
            request.GET = QueryDict('', mutable=True)
            request.GET.update(self.default_filters, q='')
        return super().changelist_view(request, extra_context=extra_context)


class GetOrSetUserCookieMixin:
    def get_or_set_user_cookie(self, request, dispatch_func, *args, **kwargs):
        self.user_cookie = request.COOKIES.get('user_cookie')
        if not self.user_cookie:
            self.user_cookie = uuid.uuid4().hex
            response = dispatch_func(request, *args, **kwargs)
            response.set_cookie('user_cookie', self.user_cookie)
        else:
            response = dispatch_func(request, *args, **kwargs)
        return response
