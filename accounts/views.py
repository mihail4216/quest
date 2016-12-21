# -*- coding: utf-8 -*-
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, render_to_response, redirect
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView


class LoginView(FormView):
    template_name = "login.html"
    success_url = "/login/"
    form_class = AuthenticationForm

    def form_valid(self, form):
        user = form.get_user()
        auth.login(self.request,user)
        return redirect('/accounts/lk/',user)
class LkView(TemplateView):
    template_name = "lk.html"
class LogoutView(RedirectView):

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return redirect('/')
class RegisterView(FormView):
    template_name = 'register.html'
    success_url = '/register/'
    form_class = UserCreationForm
    def form_valid(self, form):
