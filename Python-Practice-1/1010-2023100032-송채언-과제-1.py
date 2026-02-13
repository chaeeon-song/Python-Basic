ID = input("아이디 입력: ")

if ID == 'apple':
    PW = int(input("비밀번호 입력: "))
    if PW == 1234:
        print("회원 로그인 ")
    else :
        print("비밀번호 오류")
    print("end")
elif ID == 'guest':
    print("비회원 로그인")
    print("end")
else :
    print("end")


#input()은 그 자체로 프린트되는 기능까지 포함... ID = input()으로 정의하면, 정의한 상태가 서술되어 있는 게 아니라, 당장 화면에 새로 입력하라고 뜸.
