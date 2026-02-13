#실습6

'''def factorial(n):
    result = 1
    for i in (1, n+1):
        result = result * i
    return result

n = int(input("정수값 입력: "))
결과 = factorial(n)
print(f"결과: {결과}")

#수정해야 함. 이상한 결과 나옴.'''



'''def recur():
    print("파이썬")
    recur()
recur()'''


'''def factorial(n):
    if (n==1):
        return 1
    elif (n >= 2):
        return n * factorial(n-1)

n = int(input("정수값 입력: "))
result = factorial(n)
print("결과: ", result)'''


def lovely(n) :
    if (n==1):
        print(n)
    elif (n>=2):
        print(n)
        lovely(n-1)

n = int(input("양수를 입력하세요 : " ))
lovely(n)
