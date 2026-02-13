# 실습8

# 클래스 첫 문자는 보통 대문자로 써요.

class Number:
    count = 0
    def __init__(self):
        Number.count += 1
        self.number = Number.count
    def prn(self):
        print(self.number)

A = Number()
B = Number()
C = Number()

A.prn()
B.prn()
C.prn()
