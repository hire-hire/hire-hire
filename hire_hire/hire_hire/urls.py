from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('homepage.urls')),
    path('contributors/', include('contributors.urls')),
    path('duel/', include('duel.urls')),
    path('interview/', include('interview.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
