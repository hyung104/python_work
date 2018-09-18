#-*- coding:utf-8 -*-

import time
import threading

def printCount(num, name):
    #전달 받은 인자 10번 출력하기
    for i in range(10):
        print num, name
        time.sleep(1) # 스레드 1초 지연 시키기
        print '인덱스 :', i
    
    print 'ended printCount()'
        
if __name__ == '__main__':
    print u'메인 스레드가 시작 되었습니다.'
    
    #printCount(1, '김구라')
    # 스레드 객체 생성
    # Thread(target=함수의 참조값, args=함수에 전달할 인자 tuple type)
    t=threading.Thread(target=printCount, args=(1,'김구라'))
    # 스레드 시작 시키기
    t.start()
    
    t2=threading.Thread(target=printCount, kwargs={'num':2, 'name':'해골'})
    t2.start()
    print u'메인 스레드가 종료 됩니다.'
    
    