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

        context['message1'] = Message.objects.filter(asker=self.request.user.id)

        return context


class SendMessageView(CreateView):
    form_class = SendMessageForm
    template_name = 'send_message.html'
    model = Message
    def form_valid(self, form):
        sms=form.save()
        sms.sender = self.request.user.username
        sms.save()
        return redirect('/message/all/'+ str(self.request.user.id))
