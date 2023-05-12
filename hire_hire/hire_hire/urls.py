from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('old/', include('homepage.urls')),
    path('old/auth/', include('users.urls')),
    path('old/contributors/', include('contributors.urls')),
    path('old/duel/', include('duel.urls')),
    path('old/interview/', include('interview.urls')),
    path('old/add_question/', include('add_question.urls')),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
    urlpatterns += [
        path(
            'api/schema/',
            SpectacularAPIView.as_view(),
            name='schema',
        ),
        path(
            'api/schema/swagger-ui/',
            SpectacularSwaggerView.as_view(url_name='schema'),
            name='swagger-ui',
        ),
        path(
            'api/schema/redoc/',
            SpectacularRedocView.as_view(url_name='schema'),
            name='redoc',
        ),
    ]
