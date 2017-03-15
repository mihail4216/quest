# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


from MyBlog import settings
from One.views import User_data
from accounts.views import *
from django.contrib.auth.models import User

urlpatterns = [
    url(r'^login/$',LoginView.as_view(),name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^lk/',LkView.as_view(model=User),name='lk'),
    url(r'^register/',RegisterView.as_view(),name='register'),
    url(r'^edit/(?P<pk>\d+)/$',EditView.as_view(),name='edit'),
    # url(r'^edit/$',EditView.as_view(),name='edit'),
    url(r'^creat/',CreatePDView.as_view(),name='creat'),
    url(r'^(?P<pk>\d+)/$',User_data.as_view(),name='user_data'),
    # url(r'^logout/', include()),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
