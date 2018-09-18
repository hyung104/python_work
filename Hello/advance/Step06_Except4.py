#-*- coding:utf-8 -*-

# 예외 객체를 생성할 클래스 정의하기
class MyError(Exception): #Exception 을 상속 받아서 만든다.
    #생성자
    def __init__(self, msg):
        self.msg=msg
    
    #예외 메세지 리턴
    def __str__(self):
        return self.msg

if __name__ == '__main__':
    
    try:
        msg=input('정수 입력 :')
        if not isinstance(msg, int):
            # 원하는 시점에 예외 발생 시키기
            raise MyError('정수를 입력 해주세요')
        
        print '입력한 정수 :', msg
        
    except MyError, me:
        print me
        print type(me)
       
    print u'메인 스레드가 종료 됩니다.'
    