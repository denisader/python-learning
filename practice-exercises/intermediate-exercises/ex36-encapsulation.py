class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance # hide this variable
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New Balance: {self.__balance}")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.__balance}")
        else:
            print("Insufficient funds!")
    
    def get_balance(self):
        return self.__balance

acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(200)
print(f"Final Balance: {acc.get_balance()}")