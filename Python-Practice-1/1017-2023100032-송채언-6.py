#실습6

'''print("*****숫자 맞히기 게임****")
import random
x = random.randint(1, 100)
y = int(input("1~100 사이의 숫자를 입력하세요: "))
if y == x :
    print("맞았습니다!" )
elif y > x :
    print("입력값이 큼!")

else:
    print("입력값이 작음!")

print(f"정답은 {x}")'''

#elif 뒤에는 반드시 조건, else 뒤에는 조건X


print("*****숫자 맞히기 게임*****")
import random
x = random.randint(1, 100)
y = int(input("1~100 사이의 숫자를 입력하세요: "))
tries = 0
while y != x:
    if y == x:
        print("축하합니다!")
        print(f"시도 횟수 = {tries}")
        break
    if y < x:
        print("입력값이 작음!")
        y = int(input("1~100 사이의 숫자를 입력하세요: "))
    elif y > x:
        print("입력값이 큼!")
        y = int(input("1~100 사이의 숫자를 입력하세요: "))

#이런 프로그래밍이 어려우시면 연습하셔야 합니다... 심각하네 지금 상황.
