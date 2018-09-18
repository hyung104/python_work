#-*- coding:utf-8 -*-

#import 해서
import MyPen
import MyUtil   #from advance import MyUtil
from advance.MyUtil import Messenger


# import 한 모듈에 있는 메소드 사용하기
MyPen.write()

# import 한 모듈에 있는 변수 참조 
print MyPen.name

m1=MyUtil.Messenger()
m1.sendMessage('hello~')

m2=Messenger()
m2.sendMessage('okay')
