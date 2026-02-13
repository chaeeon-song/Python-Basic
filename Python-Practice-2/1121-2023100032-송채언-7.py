#실습 7

'''region = {101: '서울', 102 : '부산', 103 : '광주', 104 : '대전'}
while True :
    word == input("코드를 입력하세요: ")
    if word == 0:
        break
    result = region.get(word)
    if result == None:
        print("잘못된 입력입니다.")
    else:
        print(result)
    print()'''


def get_area(code):
    result = cities.get(code)
    return result
cities = {101: '서울', 102: '부산', 103: '광주', 104: '대전'}
while(True):
    code = int(input("코드를 입력하세요.: "))
    if (code == 0):
               break
    result = get_area(code)
    if result == None:
        print("잘못된 입력입니다.")
    else:
        print(result)

    print()
