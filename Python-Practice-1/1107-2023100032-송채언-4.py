#실습4

def calc(x, y, z):
    return x + y + z

sum = calc(10, 20, 30)
print(sum)

sum = calc(x = 10, y = 20, z = 30)
print(sum)

sum = calc(y=20, x=10, z=30)
print(sum)

sum = calc(10, y=20, z=30)
print(sum)

'''sum = calc(x = 10, 20, 30)
print(sum)'''
