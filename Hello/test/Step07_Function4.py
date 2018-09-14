#-*- coding:utf-8 -*-
'''

    함수 call 할때 keyword 인자를 전달할수도 있다.

'''

def test1(num, name, addr):
    print num, name, addr

test1(1, u'김구라', u'노량진')

# 순서와 상관없이 keyword로 직접 지정해서 전달할 수 있다.
# nums.sort(reverse=True) 에서 reverse도 keyword인자임
test1(name=u'해골', num=2, addr=u'행신동')

# 함수를 선언할때 전달되는 인자의  default 값을 지정할수 있다.  - 기본값
def test2(num=0, name='누구게',addr='어디게'):
    print num, name, addr
    
test2()
test2(name=u'원숭이')
test2(num=3,addr=u'동물원')
