#-*- coding:utf-8 -*-

from django.shortcuts import render
from django.views.generic.list import ListView
from noticeApp.models import Notice

# noticeApp/views.py

class HomePageView(ListView):
    # 사용할 모델 설정 - 알아서 목록 가져옴
    model=Notice
    # 템플릿 파일 설정
    template_name='notice/home.html'
    
