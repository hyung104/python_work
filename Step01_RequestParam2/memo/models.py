#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

'''
    데이터 Base에 테이블을 만든다는 느낌으로 클래스를 정의한다.
    
'''
'''
    CREATE TABLE memo
     ( id INTEGER PRIMARY KEY AUTOINCREMENT,
       content TEXT, 
       regdate DATE )
'''
# CREATE TABLE memo 의미.
class Memo(models.Model):
    # 필드정의 - id는 자동으로 생성
    content=models.TextField()      # 칼럼명 = TYPE
    regdate=models.DateTimeField()
    
