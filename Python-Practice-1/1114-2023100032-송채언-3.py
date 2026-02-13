#실습3


'''myList = ['두부', '양배추', '사과']
myList.insert(2, "딸기")
print(myList)

myList.insert(3, '토마토')
print(myList)

myList.pop()
print(myList)

myList.pop(1)
print(myList)

p = myList.pop(2)
print(p)
print(myList)'''

#리무브 함수는 리턴 값이 없는데, 변수에 넣어서 출력하려고 하니까 None이 출력되는 겁니다.

'''myList = ['두부, ', '양배추', '딸기', '토마토', '사과']
myList.remove("딸기")
print(myList)

p = myList.remove('사과')
print(p)
print(myList)

myList = ['두부, ', '양배추', '딸기', '토마토', '사과']
idx = myList.index('딸기')
print(idx)
print(myList.index('토마토'))

myList.append("딸기")
print(myList)
print(myList.count('딸기'))
print(myList.index('딸기'))
myList.clear()
print(myList)

# extend는 리스트 + 리스트. 값이 들어가면 에러 발생.
value = [10, 20, 30]
value.extend([40, 50, 60])
print(value)
value.extend(40)'''




'''num1 = [1, 3, 5]
num2 = [2, 4, 6]
num3 = [11, 12, 13]

num1.extend(num2)
print(num1)

num1.extend([num2])
print(num1)
print(len(num1))

num1.append(num3)
print(num1)
print(len(num1))'''




values = []
import random
for i in range(4):
    number = random.randint(1, 100)
    values.append(number)

print(values)

values.sort()
print(values)

values.reverse()
print(values)
