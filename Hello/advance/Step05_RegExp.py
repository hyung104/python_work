#-*- coding:utf-8 -*-
'''
    [정규 표현식 객체]
'''
import re

if __name__ == '__main__':
    # 검증할 문자열
    msg='Hello, World!'
    # 검증할 문자열에서 정규 표현식에 매칭되는 문자열이 있으면 
    # Match type 객체가 리턴된다.
    result=re.search('Hello', msg)
    # 없으면 None이 리턴된다.
    result2=re.search('hello', msg)
    
    if result!=None:
        print u'Hello를 찾았습니다.'        
    if result:
        print u'Hello를 찾았습니다.'

    if result2!=None:
        print u'hello를 찾았습니다.'        
    if result2:
        print u'hello를 찾았습니다.'

    if result2==None:
        print u'hello를 찾지못했습니다.'
    if not result2:
        print u'hello를 찾지못했습니다.'
