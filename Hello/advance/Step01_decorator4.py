#-*- coding:utf-8 -*-

def outDeco(func):
    #장식이 되는 함수에 전달되는 다양한 인자를 받을수 있게 준비
    def wrapper(*args, **kwargs):
        print args, kwargs
        func(*args, **kwargs)
    return wrapper

@outDeco
def test1():
    print 'test1()'
@outDeco
def test2(name):
    print 'test2()'
@outDeco
def test3(num, name):
    print 'test3()'
test1()
test2('kim')
test3(1,'kim')
test3(num=1, name='kim')
