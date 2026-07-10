class BankAccount():
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Balance after deposit: {self.balance}")
    
    def withdraw(self, amount):
        if self.balance - amount < 0:
            print(f"Insufficinet funds. Current balance: {self.balance}")
            return
        else:
            self.balance -= amount
            print(f"Balance after withdrawal: {self.balance}")
    
bankAcc = BankAccount(1000)
bankAcc.deposit(500)
bankAcc.withdraw(200)
bankAcc.withdraw(2000)
