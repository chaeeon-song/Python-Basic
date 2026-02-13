#실습 6

price = {'노트북' : 120, '모니터' : 40, '키보드' : 5, '스피커' : 20}

'''print(f'최댓값 : {max(price)}')
print(f'최솟값 : {min(price)}')
print(f'총합 : {sum(price)}')
print(f'평균 : {avg(price)}')'''

value = max(price.values())
print(f'최댓값: {value}')

value = min(price.values())
print(f'최솟값: {value}')

total = sum(price.values())
print(f'총합 : {total}')

average = total / len(price)
print(f'평균: {round(average,1)}')
