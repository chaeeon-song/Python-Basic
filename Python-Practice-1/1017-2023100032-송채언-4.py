#실습4

i = int(input("수1: "))
x = int(input("수2: "))
add = 0
while i > x:
    if i > x:
        i, x = x, i

while i <= x:
    add += i
    i += 1

print(f"합 = {add}")
