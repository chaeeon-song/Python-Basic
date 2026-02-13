#실습 9

class Television:
    cnt = 0
    def __init__(self):
        Television.cnt += 1
        self.channel = 11
        self.volume = 10
        self.on = True
    def show(self):
        print(self.channel, self.volume, self.on)


A = Television()
A.show()
B = Television()
B.show()

print(Television.cnt)
