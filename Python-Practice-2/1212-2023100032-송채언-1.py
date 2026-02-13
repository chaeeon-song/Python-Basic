#실습 1

class Car :
    def __init__(self, speed=0, gear=1):
        self.__s = speed
        self.__g= gear
    def setSpeed(self, speed):
        self.__s = speed
    def setGear(self, gear):
        self.__g = gear
    def getSpeed(self):
        return self.__s
    def getGear(self):
        return self.__g
    def __str___(self):
        return f'({self.__s}, {self.__g})'


myCar = Car()
print(f'속도 {myCar.getSpeed()}, 기어 {myCar.getGear()}')

myCar.setGear(3)
myCar.setSpeed(100)
print(f'속도 {myCar.getSpeed()}, 기어 {myCar.getGear()}')
