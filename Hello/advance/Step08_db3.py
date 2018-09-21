#-*- coding:utf-8 -*-

#Maria DB 연결 객체
import mysql.connector

# DB 접속 정보를 dic type에  준비한다.
config={
        'user':'root',          # 계정
        'password':'maria',     # 비밀번호
        'host':'127.0.0.1',     # 접속 ip
        'database':'acorn',     # DB 이름
        'port':3306             # 포트번호 (default:3306)
    }

if __name__ == '__main__':
    try:
        #Maria DB 연결 객체 conn-(java : Connection 객체)
        conn=mysql.connector.connect(**config) #dict type 매칭
        # cursor - (java : PreparedStatement)
        cursor=conn.cursor()
         
        #select할 회원의 번호 입력받기
        inputNum=input('select 할 회원번호:')
        
        sql='''
            SELECT num, name, addr
            FROM member
            WHERE num=%s
        '''   
        cursor.execute(sql, (inputNum,))
        '''
            cursor.fetchone() 하면  tuple이 리턴된다.
            tuple 에는  select 된 row의 정보가 들어 있다.
            select 된 결과가 없을때는 None 이 리턴된다. 
        '''        
        result=cursor.fetchone()
        if result:
            print u'번호:{} 이름:{} 주소:{}'.format(result[0], result[1], result[2])
        else:
            print u'{} 번 회원은 존재하지 않습니다.'.format(inputNum)
        
    except Exception, e:
        print e
    finally:
        try:
            conn.close()
        except NameError, ne:
            print ne
    
    print u'Step08_db3.py가 종료됩니다.'