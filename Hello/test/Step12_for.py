#-*- coding:utf-8 -*-
'''
    [반복문 for ]
'''

for item in [10, 20, 30]:
    print item

# range - 이상 미만의 숫자 list 반환 range(start, end, step)
'''
    range(start, end, step)  start 이상, end 미만
    
    range(10)  start=0(default), end=10, step=1(default)
    range(20)  start=0(default), end=20, step=1(default)
    range(1,10) start=1, end=10, step=1(default)
    range(0,20,2) start=0, end=20, step=2
'''
result1=range(10)           # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result2=range(1,10)         # [1, 2, 3, 4, 5, 6, 7, 8, 9]
result3=range(1,20)         # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
result4=range(10,20)        # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19] 
result5=range(0,20,2)       # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
result6=range(0,20,3)       # [0, 3, 6, 9, 12, 15, 18]

print result1
print result2
print result3
print result4
print result5
print result6
