#-*- coding:utf-8 -*-

'''
    - list type
    
    1. 순서가 있다(인덱스로 데이터를 관리한다.
    2. 여러개의 데이터를 저장할 수 있다.
    3. 값 변경 가능
'''
from pkg_resources._vendor.pyparsing import hexnums

family=[u"엄마", u"아빠", u"나"]
# 데이터 추가
family.append(u"남동생")
family.append(u"여동생")
# 데이터 삭제
del family[3] # 인덱스를 이용한 삭제
# 데이터 삭제
family.remove(u"여동생") # 값에 의한 삭제
#가장 마지막 방의 내용 가져오기
result=family.pop()
# 데이터 수정
family[0]=u"어머니"
# 데이터 참조
person=family[1]

nums=[50,20,10,30,40]

# 오름 차순 정렬
nums.sort()

# 내림 차순 정렬
nums.sort(reverse=True)

# 반복문
for tmp in nums:
    print tmp
    
#배열의 방의 갯수
size=len(nums)

print "size: ", size

print u"Step04_List.py 가 종료 됩니다."
