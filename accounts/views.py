# -*- coding: utf-8 -*-
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django.shortcuts import render, render_to_response, redirect
from django.views.generic import ListView
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView, CreateView, UpdateView

from accounts.forms import CustomUserCreationForm, EditForm


# from accounts.models import User


class LoginView(FormView):
    template_name = "login.html"
    success_url = "/login/"
    form_class = AuthenticationForm

    def form_valid(self, form):
        user = form.get_user()
        auth.login(self.request,user)
        return redirect('/accounts/lk/',user)


class LkView(ListView):
    template_name = "lk.html"
    model = User




class LogoutView(RedirectView):
    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return redirect('/')




class RegisterView(CreateView):
    template_name = 'register.html'
    model = User
    form_class = CustomUserCreationForm
    def get_success_url(self):
        self.urls='/register/'
    def form_valid(self, form):
        self.user = form.save()
        return redirect('/',self.user)




class EditView(UpdateView):
    template_name = 'edit.html'
    form_class = EditForm
    model = User
    def get_success_url(self):
        self.urls = '/edit/'
    def form_valid(self, form):
        self.user = form.save()
        return redirect('/lk/')

