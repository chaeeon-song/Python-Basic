# 실습4

class BankAccount:
    def __init__(self):
        self.__balance = 0
        print('잔고:', self.__balance)
    def deposit(self, amount):
        self.__balance += amount
        print('잔고:', self.__balance)
    def withdraw(self, amount):
        self.__balance -= amount
        print(amount, '원 출금됨')



a = BankAccount()
a.deposit(10000)
a.withdraw(1000)

