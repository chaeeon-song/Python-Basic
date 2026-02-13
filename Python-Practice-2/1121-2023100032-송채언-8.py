#실습 8

'''str = "my NAME is Choi."

result = str.split()
print(result)

for word in result:
    print(f'{word[0]}')

for word in result:
    print(f'{word.capitalize()}')'''


'''s = input('문자열 입력: ')

acronym = ''

for word in s.split():
    acronym += word[0]

print(acronym.upper())'''


'''email = input('메일 주소: ')
result = email.split('@')'''

result = input("메일 주소: ").split('@')
print(f"ID: {result[0]}")
print(f"도메인: {result[1]}")
