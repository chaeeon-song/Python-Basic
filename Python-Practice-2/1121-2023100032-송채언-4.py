#실습4

'''nums = {1: 'one', 2: 'two'}
print(nums)

type(nums)

print(nums[2])

nums[2] = 'three'
print(nums)

nums[4] = 'four'
print(nums)'''

phone = {}
print(phone)
phone['Kim'] = '123-4567'
phone['Park'] = '234-5678'
phone['Lee'] = '345-6789'
print(phone)

'''result = phone['Kim']
print(result)

result = phone.get('Park')
print(result)

result = phone.get('Choi')
print(result)
# None : 함수에서 리턴 값 없을 때, 리스트에서 pop() 쓸 때 걔는 리턴 값 없음. 그리고 dictonary에 찾는 값이 없을 때가 세 번째.

result = phone['Choi']
print(result)'''

'''result = phone.pop('Park')
print(result)

print(phone)

del phone['Lee']
print(phone)

phone.clear()
print(phone)'''

for x in phone:
    print(x)

print('Kim' in phone)

print(phone.keys())
print(phone.values())

print(phone.items())

for i in phone.items():
    print(i)
