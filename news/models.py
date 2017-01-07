# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    avtor = models.ForeignKey(User)
    # news_comments = models.ForeignKey(Comments)

    def __unicode__(self):
        return self.title


class Comments(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField()
    avtor = models.ForeignKey(User)
    comments_news = models.ForeignKey(News)

    def __unicode__(self):
        return self.title

