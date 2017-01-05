from django.conf.urls import include, url
from django.contrib import admin

from news.views import NewsView

urlpatterns = [
    url(r'^all/',NewsView.as_view(),name='news'),
    # url(r'^(?P<pk>\d+)/$',NewsOneView.as_view(),name='news(x)'),
]
