from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('homepage.urls')),
    path('auth/', include('users.urls')),
    path('contributors/', include('contributors.urls')),
    path('duel/', include('duel.urls')),
    path('interview/', include('interview.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
