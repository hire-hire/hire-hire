from django.urls import path

from users.views import (
    SignUpView,
    CustomLoginView,
    ProfileView,
    CustomLogoutView,
)

app_name = 'users'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout', CustomLogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),

    path('profile/', ProfileView.as_view(), name='profile'),
]
