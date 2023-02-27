from django.shortcuts import redirect


class NoLoginRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('users:profile')
        return super().dispatch(request, *args, **kwargs)
