#실습8

'''student = '철수', 19, 'CS'
print(student)

name, age, major = student
print(name)
print(age)
print(major)'''

def round(x):
    square = 3.141592*x*x
    length = 2 * 3.141592 * x
    return square, length

x = int(input("원의 반지름? "))
a, c = round(x)
print(f'원의 넓이: %.1f'%a)
print(f'원의 둘레: %.1f'%c)
