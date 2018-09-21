#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# noticeApp/models.py

'''
    CREATE TABLE notice (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT
    )
'''

@python_2_unicode_compatible    #python 2.7에서 한글 깨지지 않도록
class Notice(models.Model):
    content=models.TextField() 
    
    # 객체 자체를 출력할때 출력할 문자열 리턴
    def __str__(self):
        # 앞의 10글자만 리턴 해주기
        return self.content[:10]