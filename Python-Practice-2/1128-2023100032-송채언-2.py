f = open('hello.txt', 'w')

f.write('Hello! \n')
f.write('Bye!')

f.close()

print('파일 쓰기 완료!')

f = open("hello.txt", "r")
f = open("hello.txt", "r", encoding = 'UTF-8')

result = f.read()
print(result)

f.close()

f = open('hello.txt', 'a')

f.write('202512345\n')
f.write('김영희')

f.close

print('파일 추가 완료!')
