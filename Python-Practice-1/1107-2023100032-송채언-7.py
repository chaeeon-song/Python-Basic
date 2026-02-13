#실습7

def fib(n):
    if (n == 0 or n ==1):
        return n
    elif (n >= 2):
        return fib(n-2) + fib(n-1)

n= int(input("번호(인덱스) 입력: "))
result = fib(n)
print(f"fibonacci = {result}")
