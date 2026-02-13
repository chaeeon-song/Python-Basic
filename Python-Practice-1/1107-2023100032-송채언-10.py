#실습10

'''import time
def cnt_dn(num):
    for i in range(num, 0, -1):
        print(i)
        time.sleep(1)

number = int(input("숫자 입력: "))
cnt_dn(number)
print("발사!")

#모듈은 파일 형태로 저장됨.'''

import cnt
number = int(input("숫자 입력: "))
cnt.cnt_dn(number)
print('발사!')
