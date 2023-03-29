from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('', include('homepage.urls')),
    path('auth/', include('users.urls')),
    path('contributors/', include('contributors.urls')),
    path('duel/', include('duel.urls')),
    path('interview/', include('interview.urls')),
    path('add_question/', include('add_question.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
    from drf_yasg import openapi
    from drf_yasg.views import get_schema_view
    from rest_framework import permissions

    schema_view = get_schema_view(
        openapi.Info(
            title='Snippets API',
            default_version='v1',
            description='Ты хотел ручки, вот они',
        ),
        public=True,
        permission_classes=[permissions.AllowAny],
    )

    urlpatterns += [
        re_path(
            r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json',
        ),
        re_path(
            r'^swagger/$',
            schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui',
        ),
        re_path(
            r'^redoc/$',
            schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc',
        ),
    ]
