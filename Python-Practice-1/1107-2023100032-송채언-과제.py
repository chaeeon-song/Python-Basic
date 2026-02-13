def gcd(x,y):
    if y == 0:
        print(f"gcd({x}, {y})")
        return x
    else :
        print(f"gcd({x}, {y})")
        return gcd(y, x%y)
    

x = int(input("수1을 입력하세요: "))
y = int(input("수2를 입력하세요: "))
if x < y :
    x, y = y, x
result = gcd(x,y)
print(f"최대공약수 = {result}")
