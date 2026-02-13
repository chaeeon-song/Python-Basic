#실습 5

'''Class Student :
    def __init__(self, name = None, age=0):
        self.name = name
        self.age = age

obj = Student()
print(obj.name, obj.age)

obj.age = -21
print(obj.name, obj.age)

obj = Student('kim', 22)
print(obj.name, obj.age)


Class Student:
    def __init__(self, name=Name, age-0):
        self.name = name
        self.__age = age

obj = Student()
print(obj.name, obj.__age)'''


class Student:
    def __init__(self, name=None, age=0):
        self.__name = name
        self.__age = age
    def setAge(self, age):
        self.__age=age
    def setName(self, name):
        self.__name = name
    def getAge(self):
        return self.__age
    def getName(self):
        return self.__name


obj = Student('Hong', 20)
print(obj.getName(), obj.getAge())

obj.setAge(21)
obj.setName('Park')

print(obj.getName(), obj.getAge())

