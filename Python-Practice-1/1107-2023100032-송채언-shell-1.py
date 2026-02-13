Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
================================================================= RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-1.py ================================================================
화씨온도?: 80
26.666666666666668
>>> 
====== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-1.py =====
화씨온도?: 80
섭씨온도 = 26.67
>>> 
====== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-1.py =====
화씨온도?: 
Traceback (most recent call last):
  File "C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-1.py", line 7, in <module>
    F = float(input("화씨온도?: "))
ValueError: could not convert string to float: ''
>>> 
====== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-1.py =====
화씨온도?: 80
섭씨온도 = 26.67
화씨온도?: 20
섭씨온도 = -6.67
화씨온도?: 
Traceback (most recent call last):
  File "C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-1.py", line 8, in <module>
    F = float(input("화씨온도?: "))
ValueError: could not convert string to float: ''
>>> 
====== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-1.py =====
화씨온도?:  
Traceback (most recent call last):
  File "C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-1.py", line 8, in <module>
    F = float(input("화씨온도?: "))
ValueError: could not convert string to float: ' '
>>> 
====== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-2.py =====
(1, 2, 3)
<class 'tuple'>

===================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-2.py ====================
(1, 2, 3)
<class 'tuple'>
1 2 3

===================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-2.py ====================
숫자 입력: 
    F = float(input("화씨온도?: "))
Traceback (most recent call last):
  File "C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-2.py", line 18, in <module>
    x = int(input("숫자 입력: "))
ValueError: invalid literal for int() with base 10: ''

===================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-2.py ====================
숫자 입력: 3
숫자 입력: 5
Traceback (most recent call last):
  File "C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-2.py", line 22, in <module>
    print(f"덧셈 = {덧셈결과}")
NameError: name '덧셈결과' is not defined

===================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-2.py ====================
Traceback (most recent call last):
  File "C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-2.py", line 32, in <module>
    print(exchange(a,b))
NameError: name 'a' is not defined

===================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-3.py ====================
안녕 영희,철수
Traceback (most recent call last):
  File "C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-3.py", line 7, in <module>
    greet("길동")
TypeError: greet() missing 1 required positional argument: 'msg'

===================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-3.py ====================
안녕 영희, 철수
안녕 길동, 파이썬!
안녕 둘리, 철수
안녕 희동, 파이썬!

===================== RESTART: C:\Users\nasks\OneDrive\문서\컴프2 공부\1107-2023100032-송채언-3.py ====================
숫자 입력: 3
숫자 입력: 5
숫자 입력: 3
합 = 3
합 = 8
합 = 11
5


===================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-4.py ====================
60
60
60
60

n = 10
print(n)
10
print(id(n))
140722602616216
n+=1
print(n)
11
print(id(n))
140722602616248

k = 1 >0
print(k)
True
print(id(k))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    rint(id(k))
NameError: name 'rint' is not defined. Did you mean: 'print'?
print(id(k))
140722601708288
k = 1<0
print(k)
False
print(id(k))
140722601708320
msg = "Happy"
print(msg)
Happy
print(id(msg))
1774304092416
msg += "Birthday"
print(msg)
HappyBirthday
print(id(msg))
1774304158896

listA = [1, 2, 3, 4, 5]
print(listA)
[1, 2, 3, 4, 5]
print(id(listA))
1774304218112
listB = listA
print(listB)
[1, 2, 3, 4, 5]
print(id(listb))
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(id(listb))
NameError: name 'listb' is not defined. Did you mean: 'listB'?
print(id(listB))
1774304218112
listA[2] = 30
print(listA)
[1, 2, 30, 4, 5]
print(id(listA))
1774304218112
print(listB)
[1, 2, 30, 4, 5]
print(id(listB))
1774304218112
1774304218112
1774304218112



===================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-5.py ====================
10
140722602616216
11
140722602616248
10
140722602616216

===================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-5.py ====================
[1, 2, 3, 4, 5]
1511580430208
[1, 2, 30, 4, 5]
1511580430208
[1, 2, 30, 4, 5]
1511580430208

===================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-6.py ====================
정수값 입력: 20
결과: 21

===================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-6.py ====================
정수값 입력: 5
결과: 6

def recur():
    print("파이썬")
    recur()
recur()
SyntaxError: invalid syntax

recur()
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    recur()
NameError: name 'recur' is not defined. Did you mean: 'repr'?
def recur():
    print("파이썬")
    recur()

    
recur()
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
파이썬
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    recur()
  File "<pyshell#48>", line 3, in recur
    recur()
  File "<pyshell#48>", line 3, in recur
    recur()
  File "<pyshell#48>", line 3, in recur
    recur()
  [Previous line repeated 121 more times]
  File "<pyshell#48>", line 2, in recur
    print("파이썬")
KeyboardInterrupt

===================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-6.py ====================
정수값 입력: 5
결과: 6

===================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-6.py ====================
정수값 입력: 5
결과: 6
정수값 입력: 
===================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-6.py ====================
정수값 입력: 4
결과:  24

===================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-6.py ====================
양수를 입력하세요 : 5
5
4
3
2
1


===================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-7.py ====================
번호(인덱스) 입력: 
    Traceback (most recent call last):
      File "<pyshell#49>", line 1, in <module>
Traceback (most recent call last):
  File "C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-7.py", line 9, in <module>
    n= int(input("번호(인덱스) 입력: "))
ValueError: invalid literal for int() with base 10: ''

===================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1107-2023100032-송채언-7.py ====================
번호(인덱스) 입력: 4
fibonacci = 3
