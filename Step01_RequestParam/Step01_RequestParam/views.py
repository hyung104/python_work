#-*- coding:utf-8 -*-

from django.shortcuts import render_to_response
from django.http.response import HttpResponse

# 최상의  empty 요청에 대한 응답  r'^$'
def index(request):
    
    return render_to_response('index.html')

#/test/ 요청 처리
def test(request):
    # GET 방식 요청 파라미터 추출
    num=request.GET.get("num")
    info='num:{}'.format(num)
    
    # 임시로 문자열 응답하기
    return HttpResponse(info)    
    
#/test2/ 요청 처리
def test2(request):
    num=request.GET.get("num")
    name=request.GET.get("name")    # 한글은 오류남
    info='num:{} name:{}'.format(num, name)
    # 임시 응답
    return HttpResponse(info)    
    