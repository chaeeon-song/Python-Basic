def 출력(name):
    print(name)

def 추가(name, friend):
    found = False
    for n in name:
        if friend == n:
            print(f"{friend}는 리스트에 있습니다.")
            found = True
            break
    
    if not found:
        name.append(friend)
        
    return name

def 삭제(name, delete):
    found = False
    for n in name: 
        if delete == n:
            name.remove(delete)
            found = True
            break
    if not found:
        print(f"{delete}는 리스트에 없습니다.")
        
    return name

def 변경(name, change1, change2):
    if change1 in name:
        x = name.index(change1)
        name.remove(change1)
        name.insert(x, change2)
        print(f"[{change2}]")
        
    return name

def main():
    name = []
    
    while True:
        print("-" * 10)
        print("1. 친구 리스트 출력\n2. 친구 추가\n3. 친구 삭제\n4. 이름 변경\n9. 종료")
        print("-" * 10)
        
        menu = int(input("메뉴 선택: "))
        
        if menu == 1:
            출력(name)
        
        elif menu == 2:
            friend = input("추가할 이름 입력: ")
            name = 추가(name, friend)
            print(name)
        
        elif menu == 3:
            delete = input("삭제할 이름 입력: ")
            name = 삭제(name, delete) 
            print(name)
        
        elif menu == 4:
            change1 = input('변경할 이름 입력: ')
            change2 = input('새로운 이름 입력: ')
            name = 변경(name, change1, change2)
            print(name)
        
        elif menu == 9:
            print("프로그램을 종료합니다.")
            break
        
        elif menu not in [1, 2, 3, 4, 9]:
            print("범위를 벗어났습니다")

main()
