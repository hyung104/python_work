#-*- coding:utf-8 -*-
'''
    [ random package 사용하기 ]
'''
import random as ran #import 된 random의 별칭 부여

ranNum=ran.random() #0이상 1미만의 무작위 실수
    
ranNum2=int(ran.random()*10)    # 0이상 10 미만의 무작위 정수

ranNum3=int(ran.random()*10)+10 #10이상 20 미만의 무작위 정수

ranNum4=int(ran.random()*45)+1  # 1이상 45이하의 무작위 정수

ranNum5=ran.randint(1,45)   # 1이상 45이하의 무작위 정수

print ranNum, ranNum2, ranNum3, ranNum4, ranNum5

# 로또번호
nums=set() # 로또 번호를 담을 set 객체 - 중북불가.

while True:
    #무작위의 로또 번호를 얻어내서
    lottoNum=ran.randint(1,45)
    #set에 추가한다
    nums.add(lottoNum)
    #set에 번호가 6개가 담기면 반복문 탈출
    if(len(nums)==6):
        break

print nums

# set에 있는 숫자를 이용해서 list 객체 얻어내고 
lottoList=list(nums)
#  오름차순정렬
lottoList.sort()    # sort(reverse=True) : 내림차순

#list의 구조 확인
print lottoList
