#실습8

#12시 30분 경

'''x = int(input("수 입력: "))
print(f"1~{x}까지 3의 배수: ")
y = x // 3
i = 1
while i <= y:
    print(3*i)
    i += 1'''

#브레이크는 빠져나가고, continue는 밑에 뭐가 있던 상관없이, 위로 올라가서 다음 반복 진행함. 이 역시 whlie문 내부에서만 쓰일 수 있음.

num = int(input("수 입력: "))
print("1~%d까지 3의 배수" % num)
i = 0

while(i < num):
    i += 1
    if (i % 3)!= 0 :
        continue
    print(i)
