#실습 8

'''def 출력 (num1, num2):
    if num1 == num2:
        print(-1)
    else:
        print(max(num1, num2))

num1 = int(input("수1 입력: "))
num2 = int(input("수2 입력: "))
출력(num1, num2)'''


def 출력 (num1, num2):
    num1 = int(input("수1 입력: "))
    num2 = int(input("수2 입력: "))
    if num1 == num2:
        return(-1)
    else:
        return(max(num1, num2))

print(출력(num1, num2))
