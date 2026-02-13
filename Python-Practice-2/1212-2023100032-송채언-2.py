#실습 2

class Rectangle:
    def __init__(self, side = 1):
        self.side = side
    def getArea(self):
        return self.side * self.side

def printAreas(r, n):
    while (n>=1):
        print(f'길이 = {r.side}\t면적={r.getArea()}')
        r.side += 1
        n = n -1

rect = Rectangle()
count = int(input("반복 횟수: "))
printAreas(rect, count)

#side는 private하지 않으므로 외부에서 접근 가능
#외부에서 접근 못하게 하려면 밑줄 해서 private하게 속성을 바꿔주자.
