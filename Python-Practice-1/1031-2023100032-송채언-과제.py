x = int(input("반 수 입력: "))
y = int(input("반별 학생 수 입력: "))
add = 0
print()

for i in range(x):
    for j in range(y):
        가 = int(input("국어 점수 입력: "))
        나 = int(input("영어 점수 입력: "))
        add = add + 가 + 나
        print(f"합 = {가+나}, 평균 = {(가+나)/2:.2f}")
        print()

print(f"총합 = {add}, 과목 당 평균 = {add/(x*y*2):.2f}")
