#-*- coding:utf-8 -*-

# memberApp/urls.py

from django.conf.urls import url, include
from memberApp import views

urlpatterns = [
    url(r'^list/$', views.list),
    url(r'^insertform/$', views.insertform),
    url(r'^insert/$', views.insert),
    url(r'^delete/$', views.delete),
    url(r'^updateform/$', views.updateform),
    url(r'^update/$', views.update),
]