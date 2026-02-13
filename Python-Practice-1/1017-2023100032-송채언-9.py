#실습9

x = int(input("시작값: "))
y = int(input("끝값: "))
합 = 0
if x > y:
    x, y = y, x
if x <= y:
    for i in range(x, y+1):
        합 += i

print(f"{x} ~ {y}의 합 = {합}")
