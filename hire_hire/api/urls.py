from django.urls import include, path, re_path

import api_add_question.urls
import api_contributors.urls
import api_interview.urls

urlpatterns = [
    path('', include(api_contributors.urls)),
    path('', include(api_interview.urls)),
    path('', include(api_add_question.urls)),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
]
