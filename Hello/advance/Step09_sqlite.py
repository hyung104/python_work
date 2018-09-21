#-*- coding:utf-8 -*-
'''
    python 은 sqlite3 database 를 내장한다.
    (원격지원 안됨. local만 가능)
'''

import sqlite3

if __name__ == '__main__':
    
    print sqlite3.sqlite_version    #3.8.11
    
    try:
        conn=sqlite3.connect('test.db')
        #cursor 객체 얻어오기
        cursor=conn.cursor()
        #table 이 없으면 만든다
        cursor.execute('''
            CREATE TABLE
            IF NOT EXISTS member
            (num INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT, addr TEXT)
        ''')
        
        #이름, 주소 입력받기
        inputName=raw_input("이름:").decode('utf-8')
        inputAddr=raw_input("주소:").decode('utf-8')
        
        # sqlite 를 사용할때 바인딩 인자는 ? 로 표기
        sql='''
            INSERT INTO member
            (name, addr)
            VALUES(?, ?)
        '''
        cursor.execute(sql, (inputName, inputAddr) )    # tuple로 데이터 전달
        conn.commit()
        print u'회원정보를 저장했습니다.'
    except Exception, e:
        print e
    finally:
        try:
            conn.close
        except NameError, ne:
            print ne
                