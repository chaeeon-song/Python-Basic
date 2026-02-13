#실습7

def square():
    n = int(input("정수 입력: "))
    result = n*n
    return(result)

square()

def square(n):
    return(n*n)

n = int(input("정수 입력: "))

result = square(n)
print(result)


def size(n):
    return(3,14*n*n)

n = float(input("반지름 입력: ")) 

result = size(n)
print(f"원의 넓이 = ", size(n))

def congratulation(name):
    print("생일 축하합니다!\n"*2)
    print(f"사랑하는 {name}의 생일 축하합니다!")

name = input("이름 입력: ")
congratulation(name)


def happyBirthday(name):
    print(f'{s}\n{s}')
    print(f"사랑하는 {name}의 {s}")

s = "생일 축하합니다!"
name = input("이름 입력: ")
happyBirthday(name)
