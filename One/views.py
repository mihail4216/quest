# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.base import TemplateView

from accounts.models import PersonalData


class MainView(TemplateView):
    template_name = "main.html"


class User_data(DetailView):
    model = PersonalData
    template_name = 'user_data.html'
    # def get_context_data(self, **kwargs):
    #     context = super(User_data,self).get_context_data(**kwargs)
    #     context['au'] = PersonalData.objects.get(user=self.kwargs['pk'])
    #     return context