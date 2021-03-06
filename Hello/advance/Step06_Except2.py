#-*- coding:utf-8 -*-

if __name__ == '__main__':
    try:
        num1=input('나눌수 입력:')
        num2=input('나누어 지는 수 입력:')
        
        result=num2/float(num1)    #정수/정수는 정수만 나옴 둘중 하나를 실수로 변경
        
        #코드 여러줄 사용할경우 \ 붙임. 그뒤에는 주석도 달수없음
        print u'{} 를 {} 로 나눈 값은 {} 입니다.'\
            .format(num2, num1, result)
            
    except ZeroDivisionError, zde:  # exception type, 변수
        print zde
        print '어떤수를 0으로 나눌수 없습니다.'
    except ValueError, ve:
        print ve
    except Exception, e:    # 위의 두가지를 제외한 모든 예외
        print e    
    else:
        print '예외가 발생하지 않았습니다.'
    finally:
        print '예외 발생과 상관 없이 실행이 보장되는 블럭'
        
    print u'메인 스레드가 종료 됩니다.'
