#실습3(while)

'''i=10
while i>0 :
    print("안녕")
    i -= 1'''

'''i = 1
while i<=10:
    print(i)
    i += 1'''

'''i = 10
while i>0:
    print(i)
    i-=1'''

'''i = 1
x = int(input("숫자 입력: "))
while i <= x:
    print(i)
    i += 1'''

'''i = 1
x = int(input("숫자 입력: "))
while i <= x:
    print(i)
    i += 2'''


"""i = 1
x = int(input("몇 단?? "))
while i < 10:
    print(f"{x} * {i} = {x*i}")
    i += 1"""

factorial = 1

n = int(input("정수 입력: "))
i = n
while (i>1):
    factorial*=i
    i-=1
print(f"{n}!={factorial}")

