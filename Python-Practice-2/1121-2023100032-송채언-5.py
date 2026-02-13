#실습5

'''info = {1: ['Kim', '123-4567'], 2: ['Park', '234-5678'], 3 : ['Lee', '345-6789']}

print(info[1])
print(info[1][0])
print(info[1][1])'''


사전 = {'school' : '학교', 'student' : '학생', 'class' : '학급'}
'''while True:
    word = input("단어 입력: ")
    if word in 사전 :
        print(사전.get(word))
    else :
        print('None')'''

while(True):
    word = input('단어 입력: ')
    if word == "":
        break
    print(사전.get(word, '해당 단어는 사전에 없습니다.'), '\n')
        
