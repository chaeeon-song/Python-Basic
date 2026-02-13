#실습6

dice = [[2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 1]]


'''print(sum(dice[2]))
print(dice[0][1] + dice[1][1] + dice[2][1] + dice[3][1])'''



print(dice)
add = 0
for cols in range(len(dice[0])):
    add += dice[2][cols]

print(add)

add = 0
for rows in range(len(dice)):
    add+= dice[rows][1]
print(add)
