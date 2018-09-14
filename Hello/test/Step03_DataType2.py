#-*- coding:utf-8 -*-

# list type (수정 가능한 배열)
nums=[10,20,30,40,50]

names=['kim','lee','park']

friends=[u'김구라', u'해골', u'원숭이']

# tuple type (수정 불가능한 배열) - readonly. 수정을 고려하지 않아서 더 빠름.
nums2=(10,20,30,40,50)

names=('kim','lee','park')

friends=(u'김구라', u'해골', u'원숭이')

# dict type  -dictory 사전형태 . 방의 이름. 키값으로 관리됨.  Object, Map 개념
mem1={"num":1, "name":u"김구라", "isMan":True}
mem2={"num":2, "name":u"해골", "isMan":False}

# function type
def a():
    pass

def b():
    print 'one'
    print 'two'
    print 'three'
    
b() # b 라는 함수 call하기

# None type - 빈변수를 만들고 싶을때.
emptyVar=None  # java 의  null이라고 이해하면 된다.

# set type (집합, 묶음)
set1={10, 20, 30, 10, 20}

print u'Step03_DataType2.py 가 종료됩니다.'
    