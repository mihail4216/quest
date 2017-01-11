# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from news.forms import NewsAddForm, CommentAddForm
from news.models import News,Comments


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
        print context
        return context

    """НЕПРАВИОООО то что ниже"""
    def form_valid(self, form):
        comment = form.save()
        # Комментарий прикрепляем к новости
        comment.comments_news = News.objects.get(id=self.kwargs['pk'])
        # здесь мне нужно указать к какой новости я делаю комментарий?
        # а автора тоже нужно в форм валид указыать?
        # <= Вот
        # твоя
        # строка
        # которая
        # это
        # делает
        # Comments.text тавк вообще делать нельзя  + странно ты тут вещи делаешь

        # Comments.text = form.cleaned_data['text']
        # Comments.title = form.cleaned_data['title']
        # Формы вручную не так создают, по другому совсем, тебе рановато так их создавать
        # News.avtor_id = self.request.user
        # Comments.comments_news_id = self.request.News.id
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
        """Если честно то у теб тут магия, я не понимаю почему он тут не добавляет пользователя, хлотя должен
        поэтому пришлось переписать стандартный метод сохранения у формы, то есть передать тужда объект пользователя
        и при сохранении самого объекта его уже добавлять


        если еще будут вопросы, то пиши в слаке, сейчас уже не могу ок
        """
        user = User.objects.get(id=self.request.user.id)
        form.save(user)
        # Вот так можно, через super мы вызываем стандартный метод form valid которые
        # все сделает нам правильно, как нужно
        #Затем, мы берем этот объект form , он уже в базе есть, и меняем его поля, в твоем случает добавляем объет пользователя
        # и обязателнно сохраняем его
        return redirect('/news/all/')

