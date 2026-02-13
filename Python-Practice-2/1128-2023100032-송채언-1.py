#실습1

sen1 = input("문자열1: ")
sen2 = input("문자열2: ")

result1 = sen1.split()
result2 = sen2.split()

print('문자열 1, 2의 공통 단어 =', end = ' ')

for x in result1:
    if x in result2:
        print(x, end = ' ')

result1 = set(sen1.split())
result2 = set(sen2.split())

print('\n문자열 2에만 포함된 단어 =', result2 - result1)

# 끝에 마침표는 어떻게 처리하지?
