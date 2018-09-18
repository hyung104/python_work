#-*- coding:utf-8 -*-

'''
     정규 표현식으로 매칭되는 모든 문자열 찾기 
'''
import re

# 검증할 문자열
msg='monday gura tuesday monkey wednesday thursday friday saturday sunday'

if __name__ == '__main__':
    # 정규 표현식 - 영문소문자 0번이상 반복
    pattern='[a-z]*day'
    
    result=re.findall(pattern, msg) # result : list type
    
    # result는 찾은 문자열이 담겨 있는 list type 이다 
    print 'result :', result
    print u'- 매칭되는 문자열 목록 - '
    for tmp in result:
        print tmp
    