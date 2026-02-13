#실습5

'''s = [[50, 60, 70, 80, 90], [40, 45, 48, 51, 53], [42, 52, 66, 74, 55]]
print(s)
for i in s:
    print(i)
for i in range(3):
    print(s[i])

print(s[0][2], s[0][4])
print(s[1][0], s[1][1])
print(s[2][1], s[2][3])'''



s = [[50, 60, 70, 80, 90], [40, 45, 48, 51, 53], [43, 52, 66, 74, 55]]
rows = len(s)
cols = len(s[0])
for r in range(rows):
    for c in range(cols):
        print(s[r][c], end = " ")
    print()
