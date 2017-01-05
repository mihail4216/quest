from django.contrib.auth.models import User
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    avtor = models.ForeignKey(User)


class Comments(models.Model):
    text = models.TextField()
    avtor = models.ForeignKey(User)
    comments_news = models.ForeignKey(News)
