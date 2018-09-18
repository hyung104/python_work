#-*- coding:utf-8 -*-

names=['kim', 'lee', 'park', 'jo', 'choi']

for item in names:
    print item
    
print '----------'

for i in [0,1,2,3,4]:
    #배열의 i번째 방 참조
    tmp=names[i]
    
    print u'{} : {}'.format(i, tmp)
    
print '----------'
    


for i in range(5):  # 5는 배열의 방의 갯수
    #배열의 i번째 방 참조
    tmp=names[i]
    
    print u'{} : {}'.format(i, tmp)
    
print '----------'


for i in range(len(names)):  # len(names) 는 배열의 방의 갯수
    #배열의 i번째 방 참조
    tmp=names[i]
    
    print u'{} : {}'.format(i, tmp)
    
print '----------'

#역순
for i in [4,3,2,1,0]:
    #배열의 i번째 방 참조
    tmp=names[i]
    
    print u'{} : {}'.format(i, tmp)
    
print '----------'

for i in range(4,-1,-1):
    #배열의 i번째 방 참조
    tmp=names[i]
    
    print u'{} : {}'.format(i, tmp)
    
print '----------'

for i in range(len(names)-1,-1,-1):
    #배열의 i번째 방 참조
    tmp=names[i]
    
    print u'{} : {}'.format(i, tmp)
    
print '----------'


#1~100 까지의 합을 구해서 출력하는 코드를 구성해 보세요.

sum=0
for i in range(1,101):
    sum=sum+i
    
print u'1~100 까지의 합 : {}'.format(sum)