#-*- coding:utf-8 -*-
'''
    입력한 정보를 문자열로 입력 받기
'''

result = raw_input('문자열입력 :')

print 'type :', type(result)
print 'result :', result

# str type을 unicode로 바꾸기
result2=result.decode('utf-8')

print 'type :', type(result2)
print 'result :', result2
