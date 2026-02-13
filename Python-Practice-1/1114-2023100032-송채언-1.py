#실습1

'''def recursion(n):
    if n ==1:
        return n
    else:
        return n*recursion(n-1)

n = int(input("n?"))
result = recursion(n)
print(result)'''


def recursion(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial

n = int(input("정수 n? "))
result = recursion(n)
print(result)
