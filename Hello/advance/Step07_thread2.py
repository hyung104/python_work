#-*- coding:utf-8 -*-

# http 요청할수 있는 요청 객체 import
from pip._vendor import requests
import threading

def getHtml(url):
    
    # http 요청을 하고 응답 객체를 리턴 받는다.
    responseObj=requests.get(url)
    # 응답된 문자열 출력해보기
    print responseObj.text
    
if __name__ == '__main__':
    print '메인 메소드가 시작 되었습니다.'
    
    #getHtml('http://daum.net')
    #t=threading.Thread(target=getHtml, kwargs={'url':'http://daum.net'})
    t=threading.Thread(target=getHtml, args=('http://daum.net',))
    t.start()
    
    print '메인 메소드가 종료 되었습니다.'