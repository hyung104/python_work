#-*- coding:utf-8 -*-
'''
    클래스 정의하기
'''

class Car:
    #필드 정의하기
    name=u'소나타'
    
    #객체를 생성할때 호출되는 생성자
    def __init__(self):
        print u'Car 클래스 생성자'
    
    #메소드 정의하기. self class Car 의 참조값을 나타냄. 
    def drive(self):
        print u'달려요!'
    
    def showInfo(self):
        print 'self.name :', self.name

# Car 클래스 이용해서 객체 생성하기                
c1=Car()    # Car 클래스의 생성자를 호출해서 객체 생성

c1.drive()
print c1.name
c1.showInfo()