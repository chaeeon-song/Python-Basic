#실습1

fname = input("파일 이름 입력: ")
str = open(fname, "r", encoding = 'UTF-8')
name = input("단어 입력: ")

cnt = 0
for line in str.readlines():
    line = line,strip()
    words = line.split()
    for i in words:
        print(i)
        if (i == name) :
            cnt += 1

print(cnt, '개')
str.close()
