#-*- coding:utf-8 -*-
'''
    예외처리 문법 학습  : 자바 try catch
'''

if __name__ == '__main__':
    try:
        num1=input('나눌수 입력:')
        num2=input('나누어 지는 수 입력:')
        
        result=num2/num1
        
        #코드 여러줄 사용할경우 \ 붙임. 그뒤에는 주석도 달수없음
        print u'{} 를 {} 로 나눈 값은 {} 입니다.'\
            .format(num2, num1, result)
            
    except ZeroDivisionError, zde:  # exception type, 변수
        print zde
        print '어떤수를 0으로 나눌수 없습니다.'
        
    print u'메인 스레드가 종료 됩니다.'
