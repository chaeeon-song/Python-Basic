f = open("in(homework).txt", "r", encoding = 'UTF-8')

for line in f.readlines():
    line = line.strip()
    sen = line.split()
    집합 = set(sen)


count = [0] * len(집합)
    

x = 0
for i in 집합:
    for word in sen: 
        if i == word:
            count[x] += 1
            x += 1
        else:
            continue

dic = dict()
y = 0
while y < len(집합):
    dic[y] = count[y]
    

print(dic)
            
