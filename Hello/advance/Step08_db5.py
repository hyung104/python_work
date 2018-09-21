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
        
        #수정할 회원번호
        inputNum=raw_input("수정할 회원 번호:")
        inputAddr=raw_input("주소:").decode('utf-8')
        
        sql='''
            UPDATE member
            SET addr=%s
            WHERE num=%s
        '''
        #query 수행하기
        cursor.execute(sql, (inputAddr, inputNum))
        
        #sql문의 영향을 받은 row 의 갯수
        updateCount=cursor.rowcount
        
        if updateCount>0:
            print u'{}번 회원 정보를 수정했습니다.'.format(inputNum)
        else:
            print u'{}번 회원정보 수정 실패.'.format(inputNum)
        
        # DB에 실제 반영하기
        conn.commit()
                        
    except Exception, e:
        print e
    finally:
        try:
            conn.close()
        except NameError, ne:
            print ne
    
    print u'Step08_db5.py가 종료됩니다.'