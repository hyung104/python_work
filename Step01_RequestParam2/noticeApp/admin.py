#-*- coding:utf-8 -*-
from django.contrib import admin
from noticeApp.models import Notice

# admin.py

class NoticeAdmin(admin.ModelAdmin):
    list_display=('id','content')
    
# 이렇게만 해도 models에 정의된 클래스가 테이블로 만들어짐. 단, 관리자모드에서는 볼 수 없음
#admin.site.register(Notice)

# NoticeAdmin을 넘겨줘야 관리자모드에서도 볼 수 있음
admin.site.register(Notice, NoticeAdmin)
