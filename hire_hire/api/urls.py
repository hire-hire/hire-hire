from django.urls import include, path, re_path

import api_contributors.urls
import api_interview.urls
import api_duel.urls

urlpatterns = [
    path('', include(api_contributors.urls)),
    path('', include(api_interview.urls)),
    path('', include(api_duel.urls)),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
]
