#-*- coding:utf-8 -*-
"""
    memo/urls.py
"""
from django.conf.urls import url, include
from memo import views

urlpatterns = [
    url(r'^hello/$', views.hello),    # /memo/가 앞에 생략되어 있음
    url(r'^list/$', views.list),
]
