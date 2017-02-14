

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Message(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(User,related_name='sending_mails',blank=True,null=True)
    asker = models.ManyToManyField(User,related_name='asker_mails',blank=True,null=True)
    date = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        # ss = 'sender( '+self.sender +')   text:   '+ self.text
        ss= self.text
        return ss
    class Meta:
        ordering = ['-id']
