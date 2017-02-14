from django.contrib.auth.models import User
from django.db import models
from PIL import Image

from MyBlog import settings


class PersonalData(models.Model):
    photo = models.FileField(null=True,blank=True,upload_to=settings.MEDIA_ROOT)
    phone = models.IntegerField(null=True,blank=True)
    hbd = models.DateField(null=True,blank=True)
    city = models.CharField(max_length=30,null=True,blank=True)
    user = models.OneToOneField(User)
    def __unicode__(self):
        return  str(self.user)