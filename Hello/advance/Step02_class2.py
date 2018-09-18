#-*- coding:utf-8 -*-

class Starbucks:
    
    #생성자
    def __init__(self, branch):
        #필드를 만들면서 인자로 전달된 값을 저장 - 필드가 자동으로 만들어짐.
        self.branch=branch
    
    #메소드
    def showInfo(self):
        print u'스타벅스 {}지점 입니다.'.format(self.branch)
        
s1=Starbucks(u'종로지점')
s1.showInfo()

s2=Starbucks(u'을지로')
s2.showInfo()