from django.conf.urls import include, url
from django.contrib import admin

from One.views import *




urlpatterns = [
    url(r'^',MainView.as_view(),name='main'),
    # url(r'^logout/', include()),

]
