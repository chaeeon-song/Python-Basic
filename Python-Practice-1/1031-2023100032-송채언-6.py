#실습6

add = 0
for i in range(1, 11):
    add += i
print(add)



def summation():
    add = 0
    for i in range(1, 11):
        add += i
    print(add)

summation()


def summation(num1, num2):
    add = 0
    for i in range(num1, num2+1):
        add += i
    '''return add'''

'''value = summation(1, 10)
print(value)'''

print(summation(1, 10))


