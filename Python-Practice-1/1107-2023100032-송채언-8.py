#실습8

'''import random

x = ['a', 'b', 'c']
z = random.randint(0, 2)
print(x[z])
z = random.choice(x)
print(z)

y = 'abc'
z = random.randrange(len(y))
print(y[z])
z = random.choice(y)
print(z)'''


'''import random
while True:
    answer = input("계속 하시겠습니까? (y, n): ")
    if answer == 'n':
        break
    else:
        x = ['Head', 'Tail']
        z = random.choice(x)
        print(z)'''

import random
x = ['짜장면/짬뽕', '김밥/떡볶이', '치킨/맥주', '피자/파스타', '학생식당']
while True:
    print("추천메뉴는...?")
    import time
    time.sleep(2)
    z = random.choice(x)
    print(z, '!!!')
    answer = int(input("계속? (1: 계속, 2: 그만): "))
    if answer == 2:
        break
