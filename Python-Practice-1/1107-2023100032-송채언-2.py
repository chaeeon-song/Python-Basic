#실습2

'''def 모음():
    return 1, 2, 3

d = 모음()
print(d)
print(type(d))
a, b, c = 모음()
print(a, b, c)'''


'''def 계산():
    덧셈결과 = x + y
    뺄셈결과 = x - y
    return 덧셈결과, 뺄셈결과

x = int(input("숫자 입력: "))
y = int(input("숫자 입력: "))

result1, restult2 = 계산(덧셈결과, 뺄셈결과)'''



def swap(a, b):
    return b, a
num1 = int(input("숫자 입력: "))
num2 = int(input("숫자 입력: "))

result1, result2 = swap(num1, num2)

print(result1, result2)
