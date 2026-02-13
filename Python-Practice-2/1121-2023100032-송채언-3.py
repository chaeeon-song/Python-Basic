#실습3

'''sugang = {'글쓰기', '실용영어', '컴퓨터'}
print(sugang)

print('컴퓨터' in sugang)

sugang.remove('글쓰기')
sugang.add('심리학')
sugang.add('논리사고')
print(sugang)
print(len(sugang))'''


A = {'수학', '영어', '과학'}
B = {'영어', '미술', '체육'}
print(f'A만 듣는 과목: {A-B}')
print(f'A 또는 B가 듣는 과목: {A|B}')
print(f'둘 다 듣는 과목: {A&B}')
print(f'서로 다른 과목: {A^B}')
