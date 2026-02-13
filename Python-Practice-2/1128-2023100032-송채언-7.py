# 실습 7

'''f = open('num.txt', 'r')
result = f.split('\n')
합 = 0
for i in result :
    합 += i

평균 = 합 / len(result)

k = open('result.txt', 'r')
k.write'''

#강의안...

infile = input('입력 파일 이름: ')
outfile = input('출력 파일 이름: ')

inn = open(infile, 'r')
out = open(outfile, 'w')

add = 0
cnt = 0

for line in inn.readlines():
    line = int(line)
    add += line
    cnt += 1

out.write('합 = ' + str(add) + '\n')
out.write('평균 = ' + str(add/cnt))

inn.close()
out.close()
