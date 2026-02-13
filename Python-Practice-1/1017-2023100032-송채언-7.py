#실습7

#리스트에서 추가 안 배움. 다음에 할게요.

'''x = int(input("성적 입력: "))
add = 0
횟수 = 0
while x >= 0:
    add += x
    횟수 += 1
    x = int(input("성적 입력: "))
    if x < 0:
        break
avg = add/횟수
print(f"성적의 평균 = {avg}")'''



add = 0
count = 0
average = 0

print("종료 시 음수 입력!")
while(True):
    score = int(input("성적 입력: "))
    if (score < 0):
        break
    add = add + score
    count = count + 1
if (count > 0):
    average = add / count
print(f"성적의 평균 = {average}")
