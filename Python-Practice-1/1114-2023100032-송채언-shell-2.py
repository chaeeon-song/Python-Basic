Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

====== RESTART: C:\Users\nasks\OneDrive\문서\컴프2 공부\1114-2023100032-송채언-5.py =====
[[50, 60, 70, 80, 90], [40, 45, 48, 51, 53], [42, 52, 66, 74, 55]]
[50, 60, 70, 80, 90]
[40, 45, 48, 51, 53]
[42, 52, 66, 74, 55]
[50, 60, 70, 80, 90]
[40, 45, 48, 51, 53]
[42, 52, 66, 74, 55]
70 90
40 45
52 74

====== RESTART: C:\Users\nasks\OneDrive\문서\컴프2 공부\1114-2023100032-송채언-5.py =====
50 60 70 80 90 
40 45 48 51 53 
43 52 66 74 55 

====== RESTART: C:\Users\nasks\OneDrive\문서\컴프2 공부\1114-2023100032-송채언-6.py =====
15
18

====== RESTART: C:\Users\nasks\OneDrive\문서\컴프2 공부\1114-2023100032-송채언-6.py =====
[[2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 1]]
15
18

====== RESTART: C:\Users\nasks\OneDrive\문서\컴프2 공부\1114-2023100032-송채언-7.py =====
입력: 1
입력: 3
입력: 5
입력: 7
입력: 2
입력: 4
입력: 6
입력: 8
홀수의 합:  16
짝수의 합:  20
총합:  36

====== RESTART: C:\Users\nasks\OneDrive\문서\컴프2 공부\1114-2023100032-송채언-8.py =====
('철수', 19, 'CS')
철수
19
CS

====== RESTART: C:\Users\nasks\OneDrive\문서\컴프2 공부\1114-2023100032-송채언-8.py =====
원의 반지름? 3
원의 넓이: 28.3
원의 둘레: 18.8
ll = [1, 2, 3]
print(ll)
[1, 2, 3]
type(ll)
<class 'list'>
tt = (4, 5, 6)
print(tt)
(4, 5, 6)
type(tt)
<class 'tuple'>
ss = {3, 6, 9}
print(ss)
{9, 3, 6}
type(ss)
<class 'set'>
dd = {1: 'one', 2: 'two'}
print(dd)
{1: 'one', 2: 'two'}
type(dd)
<class 'dict'>
for name in ['철수', '양희', '길동', '유신']:
    print(name)

    
철수
양희
길동
유신
for name in ['철수', '영희', '길동', '유신']:
    print(name)

    
철수
영희
길동
유신

list1 = []
print(list1)
[]
list2 = list()
print(list2)
[]
list3 = ['H', 'e', 'l', 'l', 'o']
print(list3)
['H', 'e', 'l', 'l', 'o']
list4 = list('Hello')
print(list4)
['H', 'e', 'l', 'l', 'o']
list = [0, 1, 2, 3, 4]
print(list5)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(list5)
NameError: name 'list5' is not defined. Did you mean: 'list1'?
list5 = [0, 1, 2, 3, 4]
print(list5)
[0, 1, 2, 3, 4]
print(len(list5))
5
result = sum(list5)
print(result)
10
word = ['a', 'e']
num = [1, 3, 5]
result = word + num
print(result)
['a', 'e', 1, 3, 5]
result = word * 3
print(result)
['a', 'e', 'a', 'e', 'a', 'e']
hero1 = ['스파이더맨', '헐크', '아이언맨']
hero2 = ['슈퍼맨', '배트맨', '원더우먼']
heroes = hero1 + hero2
print(heroes)
['스파이더맨', '헐크', '아이언맨', '슈퍼맨', '배트맨', '원더우먼']
numbers = [1, 2, 3]
numers.append(4)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    numers.append(4)
NameError: name 'numers' is not defined. Did you mean: 'numbers'?
p
s = [
    [50, 60, 70, 80, 90],
    [40, 45, 48, 51, 53],
    [42, 52, 66, 74, 55]
    ]
print(s)
[[50, 60, 70, 80, 90], [40, 45, 48, 51, 53], [42, 52, 66, 74, 55]]
for i in s:
    print(i)

    
[50, 60, 70, 80, 90]
[40, 45, 48, 51, 53]
[42, 52, 66, 74, 55]
print(s[0])
[50, 60, 70, 80, 90]
print(s[1])
[40, 45, 48, 51, 53]
print(s[2])
[42, 52, 66, 74, 55]
print(s[0][2], s[0][4])
70 90
print(s[1][0], s[1][1])
40 45
print(s[2][1], s[2][3])
52 74
rows = len(s)
cols = len(s[0])
print(rows)
3
p
rint(cols)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    rint(cols)
NameError: name 'rint' is not defined. Did you mean: 'print'?
print(cols)
5
for r in range(rows):
    for c in range(cols):
        print(s[r][c], end = " ")
        print()

        
50 
60 
70 
80 
90 
40 
45 
48 
51 
53 
42 
52 
66 
74 
55 

s = [[2, 3, 4], [3, 4, 5], [4, 5, 6]. [5, 6, 1]]
SyntaxError: invalid syntax
s = [[2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 1]]
print(s)
[[2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 1]]
add = 0
for cols in range(len(s[0])):
    add += s[2][cols]

    
print(add)
15
x = 1
y = 2
x, y = y, x
print(s, y)
[[2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 1]] 1
print(x, y)
2 1
colors = ['red', 'green', 'blue']
print(colors)
['red', 'green', 'blue']
print(colors[1])
green
colors[2] = 'black'
print(colors)
['red', 'green', 'black']
colors = ('red', 'green', 'blue')
print(colors)
('red', 'green', 'blue')
print(colors[1])
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    rint(colors[1])
NameError: name 'rint' is not defined. Did you mean: 'print'?
colors[2] = 'black'
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    colors[2] = 'black'
TypeError: 'tuple' object does not support item assignment
numbers = (1, 2, 3, 4, 5)
numbers[0] = 199
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    numbers[0] = 199
TypeError: 'tuple' object does not support item assignment
>>> value1=()
>>> print(value1)
()
>>> value2 = typle()
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    value2 = typle()
NameError: name 'typle' is not defined. Did you mean: 'tuple'?
p
>>> value2 = typle()
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    value2 = typle()
NameError: name 'typle' is not defined. Did you mean: 'tuple'?
>>> value2 = tuple()
>>> print(value2)
()
>>> num1 = (1, 2)
>>> print(num1)
(1, 2)
>>> num2 = (1)
>>> print(num2)
1
>>> print(type(num2))
<class 'int'>
>>> num3 = (1, )
>>> print(num3)
(1,)
>>> fruits = '사과', '딸기', '포도'
>>> print(fruits)
('사과', '딸기', '포도')
>>> num = 1, 2, 3
>>> print(num)
(1, 2, 3)
>>> print(type(num))
<class 'tuple'>
>>> colors = ('red', 'green', 'blue')
>>> print(colors[0])
red
>>> print(colors[-1])
blue
>>> print(colors[1:])
('green', 'blue')
>>> numbers = 1, 2
>>> colors = ('red', 'green', 'blue')
>>> new = numbers + colors
>>> print(new)
(1, 2, 'red', 'green', 'blue')
>>> new = numbers * 2
>>> print(new)
(1, 2, 1, 2)
>>> t = (1, 'a')
>>> print(t+t)
(1, 'a', 1, 'a')
>>> print(t*3)
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    rint(t*3)
NameError: name 'rint' is not defined. Did you mean: 'print'?
print(len(t))
2
student = ('철수', 19, 'CS')
print(student)
('철수', 19, 'CS')
(ame, age, major) = student
print(name)
유신
(name, age, major) = student
print(name)
철수
p
print(age)
19
print(major)
CS
