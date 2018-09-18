#-*- coding:utf-8 -*-
'''
     변수에 들어있는 데이터의 type 체크
    
   isinstance(값, type)
    
     메소드는 bool type 을 리턴 합니다.
'''
from __builtin__ import isinstance

if __name__ == '__main__':
    #입력받기
    inputData=input('input:')
        
    if isinstance(inputData, int):          #55
        print 'int type!'
    elif isinstance(inputData, long):       #55555555555555555
        print 'long type!'
    elif isinstance(inputData, float):      #1.1
        print 'float type!'
    elif isinstance(inputData, str):        #'aaa'
        print 'str type!'
    elif isinstance(inputData, dict):       #{}
        print 'dict type!'
    elif isinstance(inputData, list):       #[1,2,3]
        print 'list type!'
    else:
        print 'etc type!'
