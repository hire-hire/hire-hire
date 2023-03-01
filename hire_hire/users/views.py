from django.contrib.auth import authenticate, login, mixins, views
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from users.forms import CreationForm, LoginForm
from users.mixins import NoLoginRequiredMixin


class SignUpView(NoLoginRequiredMixin, CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('homepage:index')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        form.save()

        user = authenticate(
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password1')
        )
        login(self.request, user)

        return redirect('users:profile')


class CustomLoginView(NoLoginRequiredMixin, views.LoginView):
    success_url = reverse_lazy('homepage:index')
    form_class = LoginForm
    template_name = 'users/login.html'


class CustomLogoutView(views.LogoutView):
    template_name = 'homepage/index.html'


class ProfileView(mixins.LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'
