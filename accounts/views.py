from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, render_to_response
from django.views.generic.edit import FormView


class LoginView(FormView):
    template_name = "accounts/login.html"
    success_url = "/login/"
    form_class = AuthenticationForm
    def form_valid(self, form):
        user = self.form_class
        render_to_response("main.html",user)
    render("accounts/login.html", form_class)