#실습7


ROWS = 2
COLS = 4

row1, row2 = 0, 0
x = []

for i in range(ROWS):
    x.append([0]*COLS)

for i in range(ROWS):
    for j in range(COLS):
        x[i][j] = int(input("입력: "))

for j in range(COLS):
    row1 += x[0][j]
    row2 += x[1][j]

print("홀수의 합: ", row1)
print("짝수의 합: ", row2)
print("총합: ", row1 + row2)
