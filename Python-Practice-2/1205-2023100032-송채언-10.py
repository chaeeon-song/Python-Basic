# 실습 10

class Monster :
    NORMAL = 10

    def __init__(self):
        self.energy = Monster.NORMAL
    def eat(self):
        self.energy += 10
        self.show()
    def attck(self):
        self.energy -= 10
        self.show()
    def show(self):
        print('energy = ', self.energy)

mon = Monster()
mon.show()

while(True):
    num = int(input('선택? (1: 먹기, 2: 공격, 0 : 종료)'))
    if num == 0:
        break
    elif num == 1:
        mon.eat()
    elif num == 2:
        mon.attck()
    else :
        print('잘못 입력!')
