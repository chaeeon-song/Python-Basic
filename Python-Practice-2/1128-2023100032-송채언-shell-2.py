Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

====== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-1.py =====
문자열1: My name is kim.
문자열2: And My name is choi,
문자열 1, 2의 공통 단어 = My name is 
문자열 2에만 포함된 단어 = {'And', 'choi,'}

str = 'apple '
str
'apple '
str.strip()
'apple'
# 불필요한 문자가 무엇인지 어떻게 알고 판단하는 거지?
str = 'apple \n'
print(str)
apple 

str.strip()
'apple'
# 내용 수정할게요. 지난주 set. 이번주 ppt 7페이지.

======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-2.py =======================
파일 쓰시 완료!

======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-2.py =======================
파일 쓰기 완료!

======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-2.py =======================
파일 쓰기 완료!

======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-2.py =======================
Traceback (most recent call last):
  File "C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-2.py", line 13, in <module>
    f,write("2023100032 송채언")
NameError: name 'write' is not defined

======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-2.py =======================
Traceback (most recent call last):
  File "C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-2.py", line 13, in <module>
    f,write("2023100032 송채언")
NameError: name 'write' is not defined

======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-2.py =======================
파일 추가 완료!

======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-2.py =======================
파일 추가 완료!

======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-2.py =======================
파일 쓰기 완료!
파일 추가 완료!

======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-2.py =======================
파일 쓰기 완료!

======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-2.py =======================
파일 쓰기 완료!
파일 추가 완료!

======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-3.py =======================
Traceback (most recent call last):
  File "C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-3.py", line 6, in <module>
    result = f.read()
  File "<frozen codecs>", line 325, in decode
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xbc in position 24: invalid start byte

======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-3.py =======================
Traceback (most recent call last):
  File "C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-3.py", line 14, in <module>
    f = open("student.txt", "r", enconding = 'UTF-8')
TypeError: open() got an unexpected keyword argument 'enconding'. Did you mean 'encoding'?

======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-3.py =======================
김철수,남,010-123-4567


======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-3.py =======================
김철수,남,010-123-4567

박민희,여,010-234-5678

이영민,남,010-345-6789

======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-3.py =======================
김철수,남,010-123-4567

박민희,여,010-234-5678

이영민,남,010-345-6789
Traceback (most recent call last):
  File "C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-3.py", line 21, in <module>
    print(f.readline())
ValueError: I/O operation on closed file.

======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-3.py =======================
김철수,남,010-

======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-3.py =======================
Traceback (most recent call last):
  File "C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-3.py", line 27, in <module>
    y = open("student.txt", "r", enconding = 'UTF-8')
TypeError: open() got an unexpected keyword argument 'enconding'. Did you mean 'encoding'?

======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-3.py =======================
김철수,남
,010-123-4567
박민희,여,010-234-5678
이영민,남,010-345-6789

======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-4.py =======================
['김철수,남,010-123-4567\n', '박민희,여,010-234-5678\n', '이영민,남,010-345-6789']

======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-4.py =======================
['김철수,남,010-123-4567\n', '박민희,여,010-234-5678\n', '이영민,남,010-345-6789']
김철수,남,010-123-4567

박민희,여,010-234-5678

이영민,남,010-345-6789

======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-4.py =======================
김철수,남,010-123-4567

박민희,여,010-234-5678

이영민,남,010-345-6789

======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-4.py =======================
김철수,남,010-123-4567

박민희,여,010-234-5678

이영민,남,010-345-6789

======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-4.py =======================
김철수,남,010-123-4567
박민희,여,010-234-5678
이영민,남,010-345-6789

======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-4.py =======================
김철수,남,010-123-4567

박민희,여,010-234-5678

이영민,남,010-345-6789

======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-4.py =======================
010-123-4567
010-234-5678
010-345-6789
Traceback (most recent call last):
  File "C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-4.py", line 30, in <module>
    f,close()
NameError: name 'close' is not defined

======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-4.py =======================
010-123-4567
010-234-5678
010-345-6789

======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-4.py =======================
김철수
남
010-123-4567
박민희
여
010-234-5678
이영민
남
010-345-6789

======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-4.py =======================
김철수
남
010-123-4567

박민희
여
010-234-5678

이영민
남
010-345-6789


======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-5.py =======================
Traceback (most recent call last):
  File "C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-5.py", line 3, in <module>
    f.open("dan.txt", "r", encoding = 'UTF-8')
NameError: name 'f' is not defined
>>> 
======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-5.py =======================
Traceback (most recent call last):
  File "C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-5.py", line 3, in <module>
    f.open("dan.txt", "r", encoding = 'UTF-8')
NameError: name 'f' is not defined
>>> 
======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-5.py =======================
Traceback (most recent call last):
  File "C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-5.py", line 3, in <module>
    f.open("dan.txt", "r", encoding = 'UTF-8')
NameError: name 'f' is not defined
>>> 
======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-5.py =======================
Traceback (most recent call last):
  File "C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-5.py", line 3, in <module>
    f.open("dan.txt", "r", encoding = 'UTF-8')
NameError: name 'f' is not defined
>>> 
======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-5.py =======================
Traceback (most recent call last):
  File "C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-5.py", line 3, in <module>
    f = open("dan.txt", "r", encoding = 'UTF-8')
FileNotFoundError: [Errno 2] No such file or directory: 'dan.txt'
>>> 
======================== RESTART: C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-5.py =======================
Traceback (most recent call last):
  File "C:/Users/nasks/OneDrive/문서/컴프2 공부/1128-2023100032-송채언-5.py", line 3, in <module>
    f = open("dan.txt", "r", encoding = 'UTF-8')
FileNotFoundError: [Errno 2] No such file or directory: 'dan.txt'
