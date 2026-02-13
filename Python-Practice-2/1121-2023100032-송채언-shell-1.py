Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
====== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1121-2023100032-송채언-8.py =====
홀수의 합 : 7
Traceback (most recent call last):
  File "C:/Users/nasks/OneDrive/문서/컴프2 공부/1121-2023100032-송채언-8.py", line 13, in <module>
    for r in ranage(rows):
NameError: name 'ranage' is not defined. Did you mean: 'range'?
>>> s = {}3, 6, 9}
SyntaxError: unmatched '}'
>>> s = {3, 6, 9}
>>> print(s)
{9, 3, 6}
>>> type(s)
<class 'set'>
>>> s.clear()
>>> print(s)
set()
>>> d = {1: 'one', 2: 'two'}
>>> print(d)
{1: 'one', 2: 'two'}
>>> type(d)
<class 'dict'>
>>> d.clear()
>>> print(d)
{}
>>> l = [1, 2, 3]
>>> print(l)
[1, 2, 3]
>>> type(l)
<class 'list'>
>>> l.clear()
>>> fruits = {'Apple', 'Banana', 'Pineapple'}
>>> print(fruits)
{'Banana', 'Apple', 'Pineapple'}
>>> print(sroted(fruits))
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(sroted(fruits))
NameError: name 'sroted' is not defined. Did you mean: 'sorted'?
print(sorted(fruits))
['Apple', 'Banana', 'Pineapple']
my = {1.0, 2.0, 'Hello', (1, 2, 3)}
print(my)
{1.0, 2.0, (1, 2, 3), 'Hello'}
print(my)
{1.0, 2.0, (1, 2, 3), 'Hello'}
my = {1.0, 2.0, 'Hello', [1, 2, 3]}
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    my = {1.0, 2.0, 'Hello', [1, 2, 3]}
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
my = {1.0, 2.0, 'Hello', {1, 2, 3}}
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    my = {1.0, 2.0, 'Hello', {1, 2, 3}}
TypeError: cannot use 'set' as a set element (unhashable type: 'set')

====== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1121-2023100032-송채언-2.py =====
set()
<class 'set'>

====== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1121-2023100032-송채언-2.py =====
set()
<class 'set'>
{1}
1

====== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1121-2023100032-송채언-2.py =====
set()
<class 'set'>
{1}
1
Traceback (most recent call last):
  File "C:/Users/nasks/OneDrive/문서/컴프2 공부/1121-2023100032-송채언-2.py", line 12, in <module>
    print(numbers[0])
TypeError: 'set' object is not subscriptable

====== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1121-2023100032-송채언-2.py =====
{'베를린', '파리', '서울', '런던'}

====== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1121-2023100032-송채언-2.py =====
Traceback (most recent call last):
  File "C:/Users/nasks/OneDrive/문서/컴프2 공부/1121-2023100032-송채언-2.py", line 22, in <module>
    numbers.add(1)
NameError: name 'numbers' is not defined. Did you forget to import 'numbers'?

====== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1121-2023100032-송채언-2.py =====
{}
<class 'dict'>
Traceback (most recent call last):
  File "C:/Users/nasks/OneDrive/문서/컴프2 공부/1121-2023100032-송채언-2.py", line 22, in <module>
    numbers.add(1)
AttributeError: 'dict' object has no attribute 'add'

====== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1121-2023100032-송채언-2.py =====
{1, 2, 3, 4}

====== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1121-2023100032-송채언-2.py =====
{1, 2, 3, 4}
{1, 3, 4}
{1, 4}
{1, 4, 7, 8, 9}

====== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1121-2023100032-송채언-2.py =====
{1, 2, 3, 4}
{1, 3, 4}
{1, 4}
{1, 4, 7, 8, 9}
set()

====== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1121-2023100032-송채언-2.py =====
{1, 2, 3, 4}
{1, 3, 4}
{1, 4}
{1, 4, 7, 8, 9}
1
4
7
8
9
set()

====== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1121-2023100032-송채언-2.py =====
True
False
True

====== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1121-2023100032-송채언-2.py =====
{1, 2, 3, 4, 5}
{1, 2, 3, 4, 5}
{1, 2, 3}
{3}
{3}
{1, 2, 3}
{1, 2}
{1, 2}
{1, 2, 3}
{1, 2, 3}
6

====== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1121-2023100032-송채언-2.py =====
False
False
False

====== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1121-2023100032-송채언-3.py =====
{'실용영어', '글쓰기', '컴퓨터'}
True
{'논리사고', '컴퓨터', '실용영어', '심리학'}
4

====== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1121-2023100032-송채언-3.py =====
A만 듣는 과목: {'수학', '과학'}
A 또는 B가 듣는 과목: {'수학', '미술', '체육', '영어', '과학'}
둘 다 듣는 과목: {'영어'}
서로 다른 과목: {'미술', '체육', '수학', '과학'}
