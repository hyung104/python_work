#-*- coding:utf-8 -*-

from django.contrib import admin
from blogApp.models import Blog

# blogApp/admin.py

class BlogAdmin(admin.ModelAdmin):
    list_display=('id', 'author', 'title', 'content')
    
admin.site.register(Blog, BlogAdmin)
