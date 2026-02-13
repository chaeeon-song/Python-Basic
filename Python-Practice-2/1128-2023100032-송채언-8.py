# 실습 8

'''f = open('apple.png', 'rb')
data = f.read(32)
print(data)

for i in range(32):
    print(data[i], end = ' ')

f.close()'''


f1 = open('apple.png', 'rb')
f2 = open('copy.png', 'wb')

data = f1.read()

f2.write(bytes(data))

f1.close()
f2.close()

#이진파일은 시험범위 아니고, 텍스트파일 처리까지만 시험범위
