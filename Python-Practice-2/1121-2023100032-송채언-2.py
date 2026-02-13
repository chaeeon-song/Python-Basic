#실습2

'''numbers = set()
print(numbers)
print(type(numbers))

numbers.add(1)
print(numbers)
print(len(numbers))

numbers = {2, 1, 3}
print(numbers[0])'''


'''city = {'파리', '서울', '런던', '베를린', '서울'}
print(city)'''

'''numbers = {}
print(numbers)
print(type(numbers))

numbers.add(1)'''

'''numbers = {2, 1, 3}
numbers.add(4)
print(numbers)

numbers.remove(2)
print(numbers)

numbers.discard(3)
print(numbers)

numbers.update({7, 8, 9})
print(numbers)

for i in numbers:
    print(i)

numbers.clear()
print(numbers)'''


'''A = {'포도'}
B = {'사과', '포도', '딸기'}
print(A.issubset(B))

A = {1, 2, 3, 4, 5}
B = {1, 2, 3}
print(A.issubset(B))
print(A.issuperset(B))'''

'''numbers = {2, 1, 3}'''
# 강의안 보고 덧붙이기.


'''A = {1, 2, 3}
B = {3, 4, 5}

print(A|B)
print(A.union(B))
print(A)

print(A&B)
print(A.intersection(B))
print(A)

print(A-B)
print(A.difference(B))
print(A)

print(A)
print(sum(A))'''

A = {1, 2, 3, 5}
B = {1, 2, 4}
print(A>B)
print(A>=B)
print(A<B)
