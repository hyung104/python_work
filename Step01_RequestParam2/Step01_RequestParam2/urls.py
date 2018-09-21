#-*- coding:utf-8 -*-
"""Step01_RequestParam2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from Step01_RequestParam2 import  views

urlpatterns = [
    url(r'^admin/', admin.site.urls),   # r'' -> raw  문자열 그대로 해석하라는 의미.
    url(r'^$', views.index),
    url(r'^fortune/$', views.fortune),
    url(r'^detail/$', views.detail),
    url(r'^login/$', views.login),
    url(r'^memo/', include('memo.urls')),  
         # $를 안붙임 - memo 하위의 요청에 대해서 memo.urls에서 분기하겠다는 의미
    url(r'^member/', include('memberApp.urls')),
    url(r'^pages/', include('pageTestApp.urls')),
    url(r'^notice/', include('noticeApp.urls')),
]
