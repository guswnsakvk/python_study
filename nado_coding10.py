class Unit:
    def __init__(self, name, hp, damage): # __init__ 생성자
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marlne1 = Unit("마린", 40, 5)
marlne2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

wraith1 = Unit("레이스", 80, 5) # wraith1은 clocking변수가 없음
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True # 파이썬은 외부에서 변수를 추가할 수 있음, wraith2에만 있는 것

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))