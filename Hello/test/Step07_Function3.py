#-*- coding:utf-8 -*-
'''
    [ *args ]
    
    - 함수에 여러개의 인자를 동적으로 전달 받을수 있다.
    arg + s 의미
'''
def test1(arg):
    print arg
    
# test1() # 오류
test1(10)
# test1(10,20) # 오류
# test1(10, 'kim', True) # 오류


# *를 붙이면 가능해짐.
def test2(*args):
    # argg는 tuple 이다
    print args
    
test2()         # 빈  tuple
test2(10)       # 방 1개 tuple
test2(10,20)    # 방 2개 tuple
test2(10, 'kim', True)  # 방 3개 tuple 


