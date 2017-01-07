# -*- coding: utf-8 -*-
from django.contrib import admin
from news.models import *

class NewsAdmin(admin.ModelAdmin):
   fields = [
       'title',
       'text',
       'avtor',

   ]
   # inlines = ['NewsInLine']

# class NewsInLine(admin.StackedInline):
#     model = Comments
#     extra = 2

admin.site.register(News,NewsAdmin)
admin.site.register(Comments)
