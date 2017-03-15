# -*- coding: utf-8 -*-
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django.shortcuts import render, render_to_response, redirect
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView, CreateView, UpdateView

from accounts.forms import CustomUserCreationForm, EditForm, EditsForm

# from accounts.models import User
from accounts.models import PersonalData


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
    def get_context_data(self, **kwargs):
        context = super(LkView, self).get_context_data(**kwargs)
        try:
            context['self_info'] = PersonalData.objects.get(user=self.request.user.id)
            # PersonalData.objects.get(user=self.request.user.id)
        except:
            context['self_info'] = '1'
            return context
        return context





class LogoutView(RedirectView):
    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return redirect('/')




# class RegisterView(CreateView):
#     template_name = 'register.html'
#     model = User
#     form_class = CustomUserCreationForm
#     def get_success_url(self):
#         self.urls='/register/'
#     def form_valid(self, form):
#         self.user = form.save()
#         return redirect('/',self.user)

class RegisterView(CreateView):
    template_name = 'register.html'
    model = User
    form_class = CustomUserCreationForm
    def get_success_url(self):
        self.urls='/register/'
    def form_valid(self, form):
        user = form.save()
        # User.email = form.cleaned_data['email']
        # User.password = form.cleaned_data['password2']
        # User.username = form.cleaned_data['username']
        user.save()
        return redirect('/')



class EditView(UpdateView):
    template_name = 'edit.html'
    form_class = EditForm
    model = PersonalData
    def get_success_url(self):
        self.urls = '/lk/'
    def form_valid(self, form):
        user= form.save()
        user.save()
        return redirect('/accounts/lk/')


class CreatePDView(CreateView):
    template_name = 'creat_pd.html'
    model = PersonalData
    form_class = EditsForm
    def form_valid(self, form):
        print 2
        pd = form.save(commit=False)
        print 1
        pd.user = self.request.user
        pd.save()
        return redirect('/accounts/lk')
