#-*- coding:utf-8 -*-
'''
    제어문 if
'''
# 숫자를 입력 받아서 
inputNum=input('정수 입력 :')

# 홀수 인지 짝수인지 판별
if inputNum%2 == 0:
    print u'입력한 수 {} 는 짝수 입니다.'.format(inputNum)
else:
    print u'입력한 수 {} 는 홀수 입니다.'.format(inputNum)

'''
    문자열 format
'''

result1=u'이름:{} 주소:{}'.format(u'김구라', u'노량진')
print result1

result2=u'이름:{1} 주소:{0}'.format(u'노량진', u'김구라')
print result2

#오류남
#result3=u'이름:{name} 주소:{addr}'
#        .format(name=u'김구라', addr=u'노량진')

# \ - 개행기호 무시해라.       
result3=u'이름:{name} 주소:{addr}' \
        .format(name=u'김구라', addr=u'노량진')
        
print result3

print u'Step11_if.py가 종료 됩니다.'
