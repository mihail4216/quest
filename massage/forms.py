from django import forms
from django.forms import ModelForm

from massage.models import Message


class SendMessageForm(ModelForm):
    class Meta:
        model = Message
        fields =(
            'text',
            'asker',
            'sender',
        )
