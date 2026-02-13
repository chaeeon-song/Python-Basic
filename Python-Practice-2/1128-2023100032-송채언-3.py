# 실습 3

'''f = open("hello.txt", "r")
f = open("hello.txt", "r", encoding = 'UTF-8')

result = f.read()
print(result)

f.close()'''

# 오류 발생...


'''f = open("student.txt", "r", encoding = 'UTF-8')
print(f.readline())
print(f.readline())
print(f.readline())


f.close()
print(f.readline())'''

'''x = open("student.txt", 'r', encoding = 'UTF-8')
print(x.readline(10))
x.close()'''

y = open("student.txt", "r", encoding = 'UTF-8')
print(y.read(5))
print(y.read())
y.close()
