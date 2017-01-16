from django.conf.urls import include, url
from django.contrib import admin

from massage.views import *




urlpatterns = [
    url(r'^all/(?P<pk>\d+)/',AllMessageView.as_view(),name='news'),
    url(r'^send_message/',SendMessageView.as_view(),name='news'),

]
