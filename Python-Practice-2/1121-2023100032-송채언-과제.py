sentence = input('문자열 입력: ').split()

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0

for i in sentence:
    if i == 'His':
        count1 += 1
    elif i == 'name':
        count2 += 1
    elif i == 'is':
        count3 += 1
    elif i == 'Kim.':
        count4 += 1
    elif i == 'Her':
        count5 += 1
    elif i == 'Lee.':
        count6 += 1

print(f"'His': {count1}, 'name': {count2}, 'is': {count3}, 'Kim': {count4}, 'Her': {count5}, 'Lee.': {count6}")

'''j = len(sentence)

for k in range(j):
    for i in range(j):
        if k == sentence[i]
        count
    if k == sentence[
for i in sentence:
    if i == sentence[0]:
        count1 += 1
    elif i == sentence[1]:
        count2 += 1
    elif i == sentence'''
