from django.urls import include, path, re_path

import add_question.urls
import api_contributors.urls
import api_donation.urls
import duel.urls
import interview.urls

app_name = 'api'

urlpatterns = [
    path('', include(add_question.urls)),
    path('', include(api_contributors.urls)),
    path('', include(api_donation.urls)),
    path('', include(duel.urls)),
    path('', include(interview.urls)),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
]
