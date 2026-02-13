# 실습 5

'''f = open("dan.txt", "r", encoding = 'UTF-8')
x = input("단 입력: ")
for i in range(9):
    '''결과 = '{x} * {i} = {result}'
    f.write(결과)'''
    print(f'{x} * {i} = {x*i}')
    f.write(f'{x} * {i} = {x*i}')

f.close()
print("파일 쓰기 완료!")'''

    
# 오류 발생

f = open("구구단.txt", "w")
i = 1
n = int(input("단 입력: "))

while (i <= 9):
    print(f'{n}*{i} = {n*i}')
    f.write(f'{n}*{i} = {n*i}\n')
    i+= 1

f.close()
print("파일 쓰기 완료!")
