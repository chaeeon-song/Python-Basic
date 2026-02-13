#실습11

string = input("문자열 입력: ")

alphas = 0
digits = 0
spaces = 0
lower_cnt = 0
upper_cnt = 0

for c in string:
    if (c.isalpha()):
        alphas += 1
    if (c.isdigit()):
        digits += 1
    if (c.isspace()):
        spaces += 1
    if (c.islower()):
        lower_cnt += 1
    if (c.isupper()):
        upper_cnt += 1

print(f"문자열 길이 = {len(string)}")
print(f"알파벳 문자의 개수 = {alphas}")
print(f"숫자 문자의 개수 = {digits}")
print(f"스페이스 문자의 개수 = {spaces}")
print(f"소문자 개수 = {lower_cnt}")
print(f"대문자 개수 = {upper_cnt}")
