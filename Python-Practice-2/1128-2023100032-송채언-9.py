# 실습 9


x = int(input("정수1 : "))
y = int(input("정수2 : "))

'''print(f'{x}/{y} = {x/y}')'''

'''try:
    z = x/y
    print(f'{x}/{y} = {x/y}')
except ZeroDivisionError:
    print('0으로 나눌 수 없음.')'''

try:
    z = x/y
except ZeroDivisionError:
    print('0으로 나눌 수 없음.')
    return
else:
    print(f'{x}/{y} = {x/y}')
finally:
    print('종료')


# return 하면 돌아가서 그냥 끝나는데..., finally가 있으면 이건 무조건 거치고 가야 함.
    
