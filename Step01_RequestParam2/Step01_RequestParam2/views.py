#-*- coding:utf-8 -*-
'''
    views.py
'''
# from django.shortcuts import render_to_response
# def index(request):
#     
#     # templates/index.html 해석한 결과를 응답해라
#     return render_to_response('index.html')


from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.context_processors import request

# http://localhost:8000 - 최상위 요청  r'^$' 표현 
def index(request):
    
    # templates/index.html 해석한 결과를 응답해라
    return render(request,'index.html')

def fortune(request):
    
    return render(request,'fortune_today.html',\
                  {'fortune':u'동쪽으로 가면 귀인을 만나요'})

def detail(request):
    # get 방식 파리미터 추출
    num=request.GET.get("num")
    print '파라미터로 전달된 num :', num
    
    # 임시 문자열 응답
    return HttpResponse('detail ok!')

def login(request):
    
    # post 방식 전송된 파라미터 추출
    id=request.POST.get("id")
    pwd=request.POST.get("pwd")
    
    print "id : {} pwd: {}".format(id, pwd)
    
    # 임시 문자열 응답
    return HttpResponse("post /login/ ok!")
