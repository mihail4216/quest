# -*- coding: utf-8 -*-
import json

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect, render_to_response
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import RedirectView
from django.views.generic.edit import CreateView

from news.forms import NewsAddForm, CommentAddForm
from news.models import News,Comments


def news_find(request):

    if request.GET:
        # todo_items=['123','345','567']
        # data = json.dumps(todo_items)
        # return HttpResponse(data,content_type='aplication/json')
        news = request.GET['news_name']

        find = News.objects.get(title=news)
        # find=json.dumps(find)
        avtor_id =News.objects.get(title=news).avtor
        avtor = avtor_id.username
        avtor_id = avtor_id.id


        response={
            'avtor': avtor ,
            'title': News.objects.get(title=news).title,
            'likes': News.objects.get(title=news).likes,
            'text': News.objects.get(title=news).text,
            'id': News.objects.get(title=news).id,
            'avtor_id':avtor_id,
        }

        # return HttpResponse('13',content_type='application/json')
        return JsonResponse(data=response)
    return HttpResponse('qwe', content_type='text/html')
    #     return  HttpResponse('yes',content_type='text/html')
    # return HttpResponse('no',content_type='text/html')


class NewsView(ListView):
    model = News
    template_name = 'news.html'

# class CommentAddView(CreateView):
#     form_class = CommentAddForm
#     model = Comments
#     # success_url = '//'
#     def form_valid(self, form):
#         comment = form.save()
#         Comments.text = form.cleaned_data['text']
#         Comments.title = form.cleaned_data['title']
#         # News.avtor_id = self.request.user
#         comment.save()
#         return redirect('/news/all/')


"""
    Ниже CreateView  - создает форму для создания объекта, там мы указываем модель, для которой создаем
    и форма для этой модели

    т. к. ты захотел еще и вывести новости на этой странице через такой способ
    в контексте мы передаем саму новость, которую берем через pk/id
    и выводим на странице эу новость + ее комментария

    но при создании комментария, она не узнает к какой новсти прикрепляться должна, ведь новости просто выводятся
    поэтому в методе валид, мы снова через pk получили носоть(ее объет из базы)
    и через связь comments_news указали к какой новости она должна прикрепляться

    еще есть вопросы &,
смотри
"""

class NewsOneView(CreateView):
    template_name = 'news_one.html'
    model = Comments
    form_class = CommentAddForm

    def get_context_data(self, **kwargs):
        context = super(NewsOneView, self).get_context_data(**kwargs)
        # это нужно чтобы какие либо данные передавать в шаблон
        # в твоем случае это будет модель NEw
        # context['news'] - это так мы создаем переменную для шаблона
        context['news'] = News.objects.get(id=self.kwargs['pk'])

        return context

    """НЕПРАВИОООО то что ниже"""
    def form_valid(self, form):
        comment = form.save()
        # Комментарий прикрепляем к новости
        comment.comments_news = News.objects.get(id=self.kwargs['pk'])
        comment.avtor = User.objects.get(id=self.request.user.id)
        comment.save()
        # Вот теперь он должен нормально корректно работать
        return redirect('/news/all/')


class NewsAddView(CreateView):
    model = News
    template_name = 'add_news.html'
    form_class = NewsAddForm
    # News.text = form_class.cleaned_data['text']
    # News.title = form_class.cleaned_data['title']
    """ТУт тоже не правильно, ты где пишешь то"""


    def form_valid(self, form):


        user = User.objects.get(id=self.request.user.id)
        form.save(user)
        return redirect('/news/all/')

def AddLikeView(requst,pk):
    # try:
    if pk not in requst.COOKIES:
        news = News.objects.get(id=pk)
        news.likes += 1
        news.save()
        response = redirect('/news/'+pk)
        response.set_cookie(pk,news.title)
        # except ObjectDoesNotExist:
        #     raise Http404
        return response
    else:
        redirect('/news/'+pk)
    return redirect('/news/' + pk)


def addlike(request,pk):
    print 1
    if request.GET:
        news = News.objects.get(id=pk)
        print 1



# class AddLikeViews(RedirectView):
#
#     def get(self, request, *args, **kwargs):
#         news = News.objects.filter(id=args)
#         news.likes += 1
#         news.save()
#         return redirect('/news/'+kwargs)
