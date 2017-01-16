from django.contrib.auth.models import User
from django.db import models

class Message(models.Model):
    text = models.TextField()
    sender = models.CharField(max_length=30,blank=True)
    asker = models.ManyToManyField(User)

    def __unicode__(self):
        ss = 'sender( '+self.sender +')   text:   '+ self.text
        return ss
