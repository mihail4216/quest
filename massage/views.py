from time import timezone
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView

from massage.forms import SendMessageForm
from massage.models import Message


class AllMessageView(TemplateView):
    # model = Message
    template_name = 'all_message.html'

    def get_context_data(self, **kwargs):
        context = super(AllMessageView, self).get_context_data(**kwargs)

        # ds = dict()
        # for i in Message.:
        #     a=Message.objects.i
        #     a=a.id
        #     ds.update(i,a)
        # print ds
        # all_message = Message.objects.filter(asker=self.request.user.id)
        # page = Paginator(all_message,7)
        #
        # context['message1'] = page.page(1)
        context['message1']= Message.objects.filter(asker=self.request.user.id)
        return context


class SendMessageView(CreateView):
    form_class = SendMessageForm
    template_name = 'send_message.html'
    model = Message

    def form_valid(self, form):
        sms=form.save(commit=False)
        sms.sender = User.objects.get(id=self.request.user.id)
        # sms.asker = User.objects.get(id=self.kwargs['pk'])
        # sms.asker.add(User.objects.get(id=self.kwargs['pk']))
        # sms.date = timezone.now()
        sms.save()
        sms.asker.add(User.objects.get(id=self.kwargs['pk']))
        return redirect('/message/send_messages/'+ str(self.request.user.id))

    def get_context_data(self, **kwargs):
        context = super(SendMessageView,self).get_context_data(**kwargs)
        # a = User.objects.get(id=self.kwargs['pk'])
        # a=a.username
        a=self.request.user.asker_mails.filter(sender= self.kwargs['pk'])
        b=self.request.user.sending_mails.filter(asker=self.kwargs['pk'])
        context['message2'] = a
        context['message3']= b
        return context


class SendAnyMessageView(CreateView):
    form_class = SendMessageForm
    template_name = 'send_any_message.html'
    model = Message

    def form_valid(self, form):
        sms=form.save(commit=False)
        sms.sender = User.objects.get(id=self.request.user.id)
        # sms.date = timezone.now()
        sms.save()
        return redirect('/message/all/'+ str(self.request.user.id))

    # def get_context_data(self, **kwargs):
    #     context = super(SendAnyMessageView,self).get_context_data(**kwargs)
    #     a = self.request.user.asker_mails.filter(sender= self.kwargs['pk'])
    #     context['message2'] =a
    #
    #     return context
