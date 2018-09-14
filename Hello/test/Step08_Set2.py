#-*- coding:utf-8 -*-

nameSet={'kim','park','lee'}

# set 에 'kim' 이 존재하는지 여부
result1= 'kim' in nameSet       # True
# set 에 'kim' 이 존재하지 않은지 여부 
result2= 'kim' not in nameSet   # False

print "result1:", result1
print "result2:", result2

# list 에서 중복을 제거할때 사용할수 있다.
nums=[10,10,20,20,30,30,40,50]

# 빌트인 set 클래스를 이용해서 중복 제거된 set 얻어내기 
set1=set(nums) # set 객체 생성 - 기본제공되는 class (C) 자바처럼 New하지 않고  set()하면 생성됨.

print set1      # set([40, 10, 20, 50, 30])

# 빌트인 list 클래스를 이용해서 set 를 list 로 얻어내기    - list()-클래스  eq []
nums2=list(set1)

print "nums2:", nums2   #nums2: [40, 10, 20, 50, 30]

# 정렬
nums2.sort(reverse=True)
print "정렬후 nums2"
print nums2     # [50, 40, 30, 20, 10]