class Account:
    def __init__(self, __id: int, __balance: float = 100, __annualInterestRate: float = 0):
        self.__id = __id
        self.__balance = __balance
        self.__monthlyInterest = 0.0
        self.__annualInterestRate = __annualInterestRate / 100
        self.__monthlyInterestRate = 0.0

    def set_id(self, __id):
        self.__id = __id

    def set_balance(self, __balance):
        self.__balance = __balance

    def set_annualInterestRate(self, __annualInterestRate):
        self.__annualInterestRate = __annualInterestRate / 100

    def get_id(self):
        return self.__id

    def get_balance(self):
        return self.__balance

    def get_annualInterestRate(self):
        return self.__annualInterestRate * 100

    def get_monthlyInterestRate(self):
        self.__monthlyInterestRate = self.__annualInterestRate / 12
        return self.__monthlyInterestRate * 100

    def get_monthlyInterest(self):
        self.__monthlyInterestRate = self.__annualInterestRate / 12
        self.__monthlyInterest = self.__monthlyInterestRate * self.__balance
        return self.__monthlyInterest

    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount
