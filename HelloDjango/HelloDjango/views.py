#-*- coding:utf-8 -*-
'''
    컨트롤러 역할을 하는 views.py
'''
from django.shortcuts import  render_to_response

def index(request):
    
    #templates/index.html을 해석한 결과를 클라이언트에게 출력하기
    return render_to_response('index.html')

def person(request):
    # Model (데이터)
    person_today=u'김구라'
    
    # dict type에 Model 을 담는다.
    data={'name':person_today}
    
    #person.html 을 해석할때 필요한 데이터 전달하기
    return render_to_response('person.html', data)




