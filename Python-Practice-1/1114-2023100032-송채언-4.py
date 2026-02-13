#실습4

num = [8, 4, 12, 9, 10]
print(num, '\n')

while True:
    n = input('원하는 인덱스 번호는? ')

    if n == '':
        print('종료...')
        break

    x = input(f'인덱스 [{n}] 위치에 추가할 값은? ')

    num.insert(int(n), int(x))
    print(num, '\n')
