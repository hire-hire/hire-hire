from django.urls import path

from users.views import (
    SignUpView,
    CustomLoginView,
    ProfileView,
    CustomLogoutView,
)

app_name = 'users'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout', CustomLogoutView.as_view(), name='logout'),

    path('profile/', ProfileView.as_view(), name='profile'),
]
