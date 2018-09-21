#-*- coding:utf-8 -*-
"""HelloDjango URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from HelloDjango import views

#클라이언트의 요청 매핑
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),    #r'' => r'^$'  아무것도 없는 빈 요청. 최상위요청 의미
    url(r'^person/$', views.person),
]
