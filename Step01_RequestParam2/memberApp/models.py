#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.fields import AutoField, CharField

# memberApp/models.py


'''
    회원의 번호, 이름, 주소를 관리할 모델 설정 
'''
class Member(models.Model):
    # 자동증가 되는 숫자 , primary key 
    num=AutoField(primary_key=True)
    # 문자 최대 30자 null 허용 하지 않음
    name=CharField(max_length=30, null=False)
    # 문자 최대 30자 null 허용
    addr=CharField(max_length=50, null=True)
