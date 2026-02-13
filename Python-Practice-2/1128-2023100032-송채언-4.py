# 실습 4

'''f = open("student.txt", "r", encoding = 'UTF-8')'''

'''result = f.readlines()
print(result)


for i in result:
    print(i)'''


'''for line in f:
    print(line)'''


'''for line in f.readlines():
    line = line.strip()
    print(line)

f.close()'''


f = open("student.txt", "r", encoding = 'UTF-8')
'''for line in f.readlines() :
    line = line.strip()
    word = line.split(",")
    print(word[2])

f.close()'''

for line in f.readlines():
    line = line.strip()
    word = line.split(",")
    for i in word:
        print(i)
    print() # 이걸 놓침.

f.close()
