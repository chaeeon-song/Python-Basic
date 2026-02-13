#실습3

'''def greet(name, msg):
    print("안녕", name + ',' + msg)

greet("영희", "철수")
greet("길동")'''

'''def greet(name, msg = "파이썬!"):
    print("안녕", name + ',', msg)

greet("영희", "철수")
greet("길동")
greet("둘리", "철수")
greet("희동")

#실습은 교안과 똑같이 작성해도 되는 건가?'''

def difficult(x = 0, y = 0, z = 0):
    add = x + y + z
    return add

x = int(input("숫자 입력: "))
y = int(input("숫자 입력: "))
z = int(input("숫자 입력: "))

print(f"합 = {difficult(x)}")
print(f"합 = {difficult(x, y)}")
print(f"합 = {difficult(x, y, z)}")

#교안 확인
#섞어서 쓸 땐 위치 인수가 앞으로. 뒤로 가면 오류 발생. (실습4 관련 메모.)
