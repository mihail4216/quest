# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=20,unique=True)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    avtor = models.ForeignKey(User,null=True,blank=True,related_name='avtor')
    people = models.ManyToManyField(User,blank=True,related_name='people')
    # news_comments = models.ForeignKey(Comments)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-id']


class Comments(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField()
    avtor = models.ForeignKey(User,null=True,blank=True)
    comments_news = models.ForeignKey(News,null=True,blank=True)

    def __unicode__(self):
        return self.title

