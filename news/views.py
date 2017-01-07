# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView

from news.models import News,Comments


class NewsView(ListView):
    model = News
    template_name = 'news.html'


class NewsOneView(DetailView):
    template_name = 'news_one.html'
    model = News


    # s=Comments.objects.filter(id=News.)



    # s=Comments.comments_news
    # def get_object(self, queryset=None):
    #     pk_url = self.kwargs['pk']
    #     return Comments.objects.filter(id=pk_url)


    # def get_queryset(self):
    #     pk_url = self.kwargs['pk']
    #     return News.objects.filter(id=pk_url)

        # return {'News':News.objects.filter(id=pk_url),'Comments':Comments.objects.filter(comments_news_id=pk_url)}

    # def get_object(self, item):
    #     pk_url = self.kwargs['pk']
    #     return Comments.objects.filter(pk=pk_url)
# comments_news_id