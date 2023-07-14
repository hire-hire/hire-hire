from django.urls import include, path, re_path

import api_add_question.urls
import api_contributors.urls
import api_donation.urls
import api_duel.urls
import api_interview.urls

app_name = 'api'

urlpatterns = [
    path('', include(api_add_question.urls)),
    path('', include(api_contributors.urls)),
    path('', include(api_donation.urls)),
    path('', include(api_duel.urls)),
    path('', include(api_interview.urls)),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
]
