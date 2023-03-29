from django.urls import include, path, re_path

from api_contributors import urls as contributor_urls
from api_interview import urls as interview_urls

urlpatterns = [
    path('v1/', include(contributor_urls)),
    path('v1/', include(interview_urls)),
    re_path(r'^v1/auth/', include('djoser.urls')),
    re_path(r'^v1/auth/', include('djoser.urls.jwt')),
]
