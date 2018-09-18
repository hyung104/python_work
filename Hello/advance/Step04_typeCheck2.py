#-*- coding:utf-8 -*-
import types

class Flower:
    pass

#상속
class Rose(Flower):
    pass
#상속
class Tulip(Flower):
    pass

# 함수
def myFunction():
    pass

if __name__ == '__main__':
    f1=Flower()
    f2=Rose()
    f3=Tulip()
    
    #class type 체크
    if isinstance(f1, Flower):
        print "f1 은 Flower type 입니다."
    if isinstance(f2, Flower):
        print "f2 는 Flower type 입니다."
    if isinstance(f2, Rose):
        print "f2 는 Rose type 입니다."
    if isinstance(f3, Flower):
        print "f3 는 Flower type 입니다."
    if isinstance(f3, Tulip):
        print "f3 는 Tulip type 입니다."    

    #함수의 type 체크
    if isinstance(myFunction, types.FunctionType):
        print u'myFunction 은 function type 입니다.'
        
    # 클래스의 참조값을 변수에 대입
    gura=Flower
    if isinstance(gura, types.ClassType):
        print u'gura 는 class type 입니다.'
    
    
    
    
    