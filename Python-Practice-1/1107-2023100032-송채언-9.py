#실습9

import random
def genPass():
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    password = ""
    for i in range(6):
        index = random.randrange(len(alphabet))
        print(index)
        password += alphabet[index]
    return password

print("password =", genPass())
