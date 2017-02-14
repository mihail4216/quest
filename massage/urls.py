from django.conf.urls import include, url
from django.contrib import admin

from massage.views import *




urlpatterns = [
    url(r'^all/(?P<pk>\d+)/',AllMessageView.as_view(),name='view'),
    # url(r'^page/(\d+)/$',AllMessageView.as_view,name='view'),
    url(r'^send_messages/(?P<pk>\d+)/',SendMessageView.as_view(),name='send'),
    url(r'^send_message/',SendAnyMessageView.as_view(),name='send_any'),

]
