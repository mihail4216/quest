# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

from One.views import *




urlpatterns = [

    # url(r'^/(?P<pk>\d+)/$',User_data.as_view(),name='user_data'),
    # url(r'^logout/', include()),
    url(r'^$',MainView.as_view(),name='main'),

]
