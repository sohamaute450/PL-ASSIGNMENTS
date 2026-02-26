class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount deposited:", amount)
    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough balance")
        else:
            self.balance = self.balance - amount
            print("Amount withdrawn:", amount)
    def check_balance(self):
        print("Account Number:", self.acc_no)
        print("Current Balance:", self.balance)
acc = BankAccount(7789778, 100000)
acc.deposit(50000)
acc.withdraw(20000)
acc.check_balance()
