#-*- coding:utf-8 -*-
'''
    [ **kwargs ]
    
    - 함수로 전달되는 인자를  dict type 으로 받을수 있다.
     keyword 인자 의 의미로 kw+args. 이름은 마음대로 해도 됨.
'''

def test1(**kwargs):
    print kwargs

# test1(10)   # 오류  - keyword 인자를 전달해야함.

test1(num=1)
test1(num=1,name='kimgura')
test1(num=2,name='monkey', isMan=True)

# 다양한 형태의 호출을 받아줄수 있는 함수
def test2(*args, **kwargs):
    print "args :", args, "kwargs :", kwargs
    
test2(10,20)
test2(num=1,name='kimgura')
test2(30,40, num=2, name="monkey")
