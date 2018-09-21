#-*- coding:utf-8 -*-
from django.shortcuts import render
from memberApp.models import Member
from django.http.response import HttpResponseRedirect

# member/views.py

# 회원정보 수정 요청 처리
def update(request):
    #수정할 회원의 정보
    num=request.POST.get('num')
    name=request.POST.get('name')
    addr=request.POST.get('addr')
    
    # 수정할 회원의 Member 객체를 불러와서 
    mem=Member.objects.get(num=num)
    # 수정할 정보를 넣어준다.
    mem.name=name
    mem.addr=addr
    # 저장
    mem.save()
    # 응답
    return render(request, 'member/update.html', {'num':num})
       

# 회원정보 수정 폼 요청 처리
def updateform(request):
    num=request.GET.get('num')
    # 수정할 회원의 정보
    item=Member.objects.get(num=num) # Member 객체
    return render(request, 'member/updateform.html',\
                  {'item':item})

# 회원 삭제 요청 처리
def delete(request):
    # 삭제할 회원의 번호 
    num=request.GET.get('num')
    # DB 에서 삭제
    Member.objects.filter(num=num).delete()
    # 응답
    return HttpResponseRedirect('/member/list/')

# 회원 추가 요청 처리
def insert(request):
    #폼 전송된 파라미터 읽어오기 
    inputName=request.POST.get('name')
    inputAddr=request.POST.get('addr')
    # Member 객체 생성해서 저장하기 
    Member(name=inputName, addr=inputAddr).save()
    # 목록 보기로 리다일렉트 응답
    return HttpResponseRedirect('/member/list/')
    
# 회원 추가 폼 요청 처리
def insertform(request):
    return render(request, 'member/insertform.html')

# 회원 목록 요청 처리 
def list(request):
    # num 에 대해서 내림 차순 정렬된 회원 목록을 얻어온다. 
    memberList=Member.objects.all().order_by('-num')
    
    # 응답
    return render(request, 'member/list.html',\
                  {'memberList':memberList})
