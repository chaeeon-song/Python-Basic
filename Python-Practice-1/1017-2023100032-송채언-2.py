#실습2(for)

'''for i in range(10):
    print("안녕")'''

'''
for i in range(10):
    print(i+1)'''

'''for i in range(10):
    print(10-i)'''

'''x = int(input("숫자 입력: "))
for i in range(1, x+1):
        print(i)'''

'''x = int(input("숫자 입력; "))
for i in range(1, x+1, 2):
    print(i) #while문에서는 range함수가 알아서 +1 처리해줌.'''
    

"""x = int(input("몇 단?? "))
for i in range(1, 10):
    print("%d * %d = %d" % (x, i, x*i))"""

factorial = 1
x= int(input("정수 입력: "))
for i in range(1, x+1):
    factorial *= i
print(f"{x}! = {factorial}")
