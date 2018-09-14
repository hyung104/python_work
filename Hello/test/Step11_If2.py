#-*- coding:utf-8 -*-
'''
    다중 if 문
'''

# 입력한 점수 85점은 B 입니다.

inputNum=input('점수 입력 :')

if inputNum>=90:
    print u'입력한 점수 {} 점은 A 입니다.'.format(inputNum)
elif inputNum >= 80:
    print u'입력한 점수 {} 점은 B 입니다.'.format(inputNum)
elif inputNum >= 70:
    print u'입력한 점수 {} 점은 C 입니다.'.format(inputNum)
elif inputNum >= 60:
    print u'입력한 점수 {} 점은 D 입니다.'.format(inputNum)
else:
    print u'입력한 점수 {} 점은 F 입니다.'.format(inputNum)

    