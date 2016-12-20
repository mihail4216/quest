from django.conf.urls import include, url
from django.contrib import admin

from accounts.views import *

urlpatterns = [
    url(r'^login',LoginView.as_view(),name='login'),
    # url(r'^logout/', include()),

]
