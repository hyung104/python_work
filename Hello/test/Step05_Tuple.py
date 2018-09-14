#-*- coding:utf-8 -*-
'''
    - tuple
    
    1. list type 의 read only 버전 (읽기전용)
    2. 수정, 삭제 불가
    3. list type 보다 처리 속도가 빠르다.
'''

tuple1=(10, 20, 30, 40, 50)

for tmp in tuple1:
    print "tmp:", tmp
    
# tuple1[0]=99 수정불가
# del tuple1[0] 삭제 불가

# 방 1개 짜리 tuple 만들때 주의!    , 를 해줘야 함
# 연산식의 괄호 인지 tuple 의 괄호 여부인지 .  여기서는 연산식. result는 int type이 됨
result=(1+1)     # input type 2
result2=(1+1,)   # tuple type (2)
result3=('kim',) # tuple type ('kim')

# 대입할때 () 생략 가능
result4='kim', 'lee', 'park'    # tuple이 됨.

# 여러개의 변수에 값 한번에 할당하기
a, b, c = 10, 20, 30

# 두 변수에 있는 내용을 상호 교환 하려면
first='girl'
second='boy'

first, second=second, first
