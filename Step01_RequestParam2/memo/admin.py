#-*- coding:utf-8 -*-
from django.contrib import admin
from memo.models import Memo

# 정의한 모델을 여기서 등록을 해야 한다.

class MemoAdmin(admin.ModelAdmin):
    list_display=('id','content','regdate')
    
admin.site.register(Memo, MemoAdmin)

