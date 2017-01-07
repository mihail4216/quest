# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

from accounts.views import *
from django.contrib.auth.models import User
urlpatterns = [
    url(r'^login/$',LoginView.as_view(),name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^lk/',LkView.as_view(model=User),name='lk'),
    url(r'^register/',RegisterView.as_view(),name='register'),
    url(r'^edit/(?P<pk>\d+)/$',EditView.as_view(),name='edit'),
    # url(r'^logout/', include()),

]
