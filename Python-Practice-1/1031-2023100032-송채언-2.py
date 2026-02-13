#실습2

'''for i in range(7):
    print("O", end = "")
    for j in range(3):
        print("X", end = "")
    print()'''


'''for i in range(5):
    for j in range(10):
        print("*", end = "")
    print()'''

'''for i in 'abcde':
    print(i, end = "")
    for j in range(5):
        print(j, end = "")
    print()'''

'''for i in range(1, 6):
    print("*"*i, end = "")
    print()'''

for i in range(5):
    for j in range(i+1):
        print("*", end= "")
    print()
