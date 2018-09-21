#-*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse

# blogApp/models.py

@python_2_unicode_compatible
class Blog(models.Model):
    # 작성자
    author=models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
        )
    # 제목
    title=models.CharField(max_length=200)
    # 내용
    content=models.TextField()
    
    # 객체 자체를 출력했을때 제목이 출력 되도록
    def __str__(self):
        return self.tite
    
    # 새글 추가한 후 글 자세기 보기로 Redirect 시키기 위한 설정
    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.id])
       