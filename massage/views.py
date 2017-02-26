from time import timezone

from django.core.mail import send_mail
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
    template_name = 'all_message.html'

    def get_context_data(self, **kwargs):
        context = super(AllMessageView, self).get_context_data(**kwargs)

        a=Message.objects.filter(asker=self.request.user.id)
        namelist=[]
        namelist1=[]
        for i in a:
            if i.sender not in namelist:
                namelist.append(i.sender)
                namelist1.append(i)
        context['message1'] = namelist1
        return context


class SendMessageView(CreateView):
    form_class = SendMessageForm
    template_name = 'send_message.html'
    model = Message

    def form_valid(self, form):
        sms=form.save(commit=False)
        sms.sender = User.objects.get(id=self.request.user.id)
        sms.asker = User.objects.get(id=self.kwargs['pk'])
        sms.save()
        return redirect('/message/send_messages/'+ str(self.kwargs['pk']))

    def get_context_data(self, **kwargs):
        context = super(SendMessageView,self).get_context_data(**kwargs)
        a=self.request.user.asker_mails.filter(sender= self.kwargs['pk'])
        b=self.request.user.sending_mails.filter(asker=self.kwargs['pk'])
        c=[]
        for i in b:
            c.append(i)
        for i in a:
            c.append(i)
        for i in range(len(c)-1):
            for j in range(len(c)-1):
                if c[j].date>c[j+1].date:
                    c[j], c[j + 1] = c[j + 1], c[j]
        context['message2'] = a
        context['message3']=c

        return context


class SendAnyMessageView(CreateView):
    form_class = SendMessageForm
    template_name = 'send_any_message.html'
    model = Message

    def form_valid(self, form):
        sms=form.save(commit=False)
        sms.sender = User.objects.get(id=self.request.user.id)
        sms.save()
        return redirect('/message/all/'+ str(self.request.user.id))

    # def get_context_data(self, **kwargs):
    #     context = super(SendAnyMessageView,self).get_context_data(**kwargs)
    #     a = self.request.user.asker_mails.filter(sender= self.kwargs['pk'])
    #     context['message2'] =a
    #
    #     return context
