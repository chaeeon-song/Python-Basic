# 실습7

PI = 3.14
class Circle:
    def __init__(self, radius = 1.0):
        self.__radius = radius
    def setRadius(self, r):
        self.__radius = r
    def getRadius(self):
        return self.__radius
    def clacArea(self):
        area = PI * self.__radius * self.__radius
        return area
    def clacCircum(self):
        circumference = 2.0 * PI ** self.__radius
        return circumference


c = Circle()
c.setRadius(10)
pritn(f'반지름: {c.getRadius()}')
