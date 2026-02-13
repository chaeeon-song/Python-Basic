#실습5

'''def modify(n):
    n = n+1
    print(n)
    print(id(n))

n = 10
print(n)
print(id(n))

modify(n)
print(n)
print(id(n))'''

def modify(listB):
    listB[2] = 30
    print(listB)
    print(id(listB))

listA = [1, 2, 3, 4, 5]
print(listA)
print(id(listA))

modify(listA)
print(listA)
print(id(listA))
