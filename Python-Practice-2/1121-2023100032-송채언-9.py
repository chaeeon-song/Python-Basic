#실습9

x, y, z = input("점수를 입력하세요.: ").split()

''''합 = 0
for i in result:
    합 += i
평균 = 합 / len(result)

print(f'합 = {합}')
print(f'평균 = {평균}')'''

# 강의안... 오류 발생...

result = 0

for i in x :
    print(i, end = ' ')
    result += int(i)
print()
print(f'합 = {result}')
print(f'평균 = {result/3:.1f}')
