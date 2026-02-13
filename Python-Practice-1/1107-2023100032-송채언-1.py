#실습1

def Fahren_to_Cel():
    C = (F-32)*(5/9)
    return C

while True:
    F = float(input("화씨온도?: "))
    if F == "": #오 이 포인트 기억해야겠다.
        break
    print(f"섭씨온도 = {Fahren_to_Cel():.2f}")
