from django.shortcuts import render
from django.views.generic.list import ListView


class MainView(ListView):
    template_name = "main.html"