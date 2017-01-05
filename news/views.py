from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView

from news.models import News,Comments


class NewsView(ListView):
    model = News
    template_name = 'news.html'
# class NewsOneView(DetailView):
#     def get_object(self, **kwargs):
#         return super(NewsOneView,self).get_object(**kwargs)
#     model = News.objects.filter(news_id=args)
#     queryset = Comments.objects.filter(avtor_id=Comments.)
# #
