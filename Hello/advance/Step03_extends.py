#-*- coding:utf-8 -*-

class Phone():
    def call(self):
        print u'전화를 걸어요'
        

class HandPhone(Phone): #Phone 클래스를 상속 받는 문법
    def mobileCall(self):
        print u'이동중에 전화를 걸어요'
    def takePicture(self):
        print u'100만 화소의 사진을 찍어요'

class SmartPhone(HandPhone):
    def doInternet(self):
        print u'인터넷을 해요'
    def takePicture(self):
        #부모 메소드 호출 여부
        #HandPhone.takePicture(self)     # 자바 : super
        print u'1000만 화소의 사진을 찍어요'
        
if __name__ == '__main__':
    
    p1=Phone()
    p2=HandPhone()
    
    p3=SmartPhone()    
    p3.call()
    p3.mobileCall()
    p3.doInternet()
    p3.takePicture()