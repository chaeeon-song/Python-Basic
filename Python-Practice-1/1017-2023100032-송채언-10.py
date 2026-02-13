#실습10


'''x = input('문자열 입력: ')
for i in x:
    if x in ['a', 'e', 'i', 'o', 'u']:
        print(i, end=' ')'''

number = input("전화번호 입력: ")
for i in number:
    if i == '-':
        continue
    print(i, end='')

#.isdigit() 같은 문자열 함수... 외우자

#for문 안에도 break continue 사용 가능함.)

