#-*- coding:utf-8 -*-

class AttackUnit:
    # 모든 객체가 공유할 클래스 변수 만들고 초기값 부여
    attackPower=10
    
    # 공격하는 인스턴스 메소드(참조값으로 호출하는 메소드)
    def attack(self):
        print u'{} 의 파워로 공격합니다.'\
            .format(AttackUnit.attackPower)
    
    # 클래스 명으로 접근하는 클래스 메소드 만들기
    @classmethod
    def setPower(cls, power):
        # 인자로 전달되는 cls 에는 클래스의 참조값이 전달된다.
        # 아래의 코드는 AttackUnit.attackPower=power 와 같다. 
        cls.attackPower=power
    
    @classmethod
    def showPower(cls):
        print u'현재의 공격력: {} '.format(cls.attackPower)    

if __name__ == '__main__':
    #AttackUnit 객체 생성하고 참조값에 . 찍어서 메소드 호출 
    AttackUnit().attack()
    #클래스명에 . 찍어서 메소드 호출 (클래스 메소드)
    AttackUnit.setPower(20)
    AttackUnit.showPower()
    
    # AttackUnit 객체 생성하고 
    unit1=AttackUnit()
    unit1.attack() # 참조값에 . 찍어서 메소드 호출 
    
    
    
    
    
    
    
    
    
    
    
    
    
    