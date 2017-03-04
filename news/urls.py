from django.conf.urls import include, url
from django.contrib import admin

from news.views import *




urlpatterns = [
    url(r'^all/',NewsView.as_view(),name='news'),
    url(r'^(?P<pk>\d+)/$',NewsOneView.as_view(),name='news_one'),
    url(r'^add/',NewsAddView.as_view(),name='add_news'),
    url(r'^add_like/(?P<pk>\d+)/',AddLikeView,name='add_like'),
    url(r'^find/$',news_find),
    url(r'^addlike/(?P<pk>\d+)/',addlike,name='addlike'),
]
