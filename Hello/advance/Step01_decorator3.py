#-*- coding:utf-8 -*-

def myDeco(func):
    def wrapper(arg):   #장식된 함수에 전달된 인자를 받을수있다.
        if arg==u'해골':
            arg=u'해골 바가지'
        func(arg)
    return wrapper

@myDeco
def test1(name):
    print "name :", name

test1(u'김구라')

test1(u'해골')