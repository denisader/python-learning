class BankAccount():
    def __init__(self, balance):
        self.__balance = balance # name mangling
        # makes it inaccessible from outside the class

    @property # turns balance method into a read-only attribute-style accessor
    # write account.balance instead of account.balance()
    def balance(self):
        return self.__balance
    
    @balance.setter # intercepts any assignment to account.balance = value
    # runs the validation logic before updating __balance
    def balance(self, amount):
        if amount < 0:
            print("Invalid balance. Must be non-negative.")
        else:
            self.__balance = amount
    
    # uses the setter because instead of self.__balance it uses self.balance
    def deposit(self, amount):
        self.balance = self.__balance + amount

account = BankAccount(1000)
print("Current balance:", account.balance)

account.deposit(500)
print("Current balance:", account.balance)

account.balance = -200