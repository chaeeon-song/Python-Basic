# 실습 10

# p.13


'''while True:
    n= int(input("정수 입력: "))
    if n == 0:
        break

print("\n종료")'''


while True :
    try:
        n = int(input("정수 입력 : "))
    except ValueError :
        print("정수 아님! 다시 입력!")
    else :
        if n == 0:
            break
    finally:
        print('★')
print('\n종료')


