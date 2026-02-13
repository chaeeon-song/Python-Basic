#실습3

x = int(input("시작 단?? "))
y = int(input("끝 단?? "))

for i in range(x, y+1):
    for z in range(1, 10):
        print(f"{i} * {z} = {i*z}")
    print()
