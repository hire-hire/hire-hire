from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from users.forms import CreationForm, LoginForm


class SignUpView(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('homepage:index')
    template_name = 'users/signup.html'


class CustomLoginView(LoginView):
    success_url = reverse_lazy('homepage:index')
    form_class = LoginForm
    template_name = 'users/login.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'
