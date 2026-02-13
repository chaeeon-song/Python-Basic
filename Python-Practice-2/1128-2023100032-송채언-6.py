# 실습 6


infile = input("입력 파일?")
str = open(infile, 'r', encoding = 'UTF-8')

cnt = 0
for line in str.readlines():
    line = line.strip()
    words = line.split()
    for w in words:
        print(w)
        cnt += 1
print(cnt, '개')
str.close()
