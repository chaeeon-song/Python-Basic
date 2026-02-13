# 실습2

class Counter:
    def __init__(self, value = 0):
        self.cnt = value
    def reset(self):
        self.cnt = 0
    def increment(self):
        self.cnt += 1
    def get(self):
        return self.cnt

'''a = Counter()

print("a =0", a.get())
a.increment()
print("a =", a.get())
a.reset()
print('a =', a.get())

b = Counter()
print('b =', b.get())
b.increment()
print('b =', b.get())

print(a.cnt, b.cnt)'''

a = Counter()
b = Counter(10)
print('a =', a.get())
a.increment()
print('a =', a.get())
print('b =', b.get())
b.increment()
print('b =', b.get())



#num을 cnt로...
