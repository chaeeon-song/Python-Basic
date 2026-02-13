# 실습 11

# p.15

try:
    fname = input("파일 이름 입력: ")
    infile = open(fname, 'r', encoding = 'UTF-8')

except FilneNotFoundError:
    print(fname + '파일 없음!')

else :
    print(infile.read())
    infile.close()

#에러 계층도를 외울 필요는 없어요.
    
