class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
       self.int_rate = int_rate
       self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

trong = BankAccount(0.01,100)
ethan = BankAccount(0.1,100)

trong.deposit(100).deposit(100).deposit(100).withdraw(200).yield_interest().display_account_info()

ethan.deposit(150).deposit(150).withdraw(20).withdraw(20).withdraw(50).withdraw(10).yield_interest().display_account_info()

