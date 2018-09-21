#-*- coding:utf-8 -*-
from django.contrib import admin
from memberApp.models import Member

# Register your models here.

# 관리자 모드에서 관리할 모델 정보 등록
class MemberAdmin(admin.ModelAdmin):
    # 관리자 모드에서 보여질 칼럼 목록 설정 
    list_display=('num', 'name', 'addr')

# 등록
admin.site.register(Member, MemberAdmin)