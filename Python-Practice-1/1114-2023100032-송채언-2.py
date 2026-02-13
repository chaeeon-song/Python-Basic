#실습2

'''score = [32, 56, 64, 72, 12]
for i in range(5):
    print(score[i])'''



fruit = []
'''for i in range(4):
    word = input("좋아하는 과일? :")
    fruit.append(word)'''
while(True):
    word = input("입력(종료 시 엔터)> ")
    if word == "":
        break
    fruit.append(word)
print(fruit)
for i in fruit:
    print(i, end=" ")
