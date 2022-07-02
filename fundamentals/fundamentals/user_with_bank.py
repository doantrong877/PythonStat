class BankAccount:
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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {"default" : BankAccount(int_rate=0.02, balance=0)}
    
    # other methods
    
    def make_deposit(self, amount, acc):
        self.account[acc].deposit(amount)

    def make_withdrawal(self, amount,acc):
        self.account[acc].withdraw(amount)

    def display_user_balance(self,acc):
        self.account[acc].display_account_info()
    
    def transfer_money(self, amount, other_user, acc):
        fund = amount
        sender_balance = self.account[acc].balance
        if sender_balance < amount:
            print("Please deposit more money to make the transfer")
        else:
            self.account[acc].withdraw(amount)
            other_user.account[acc].deposit(amount)

    def enroll_new_account(self):
        success = False
        while(success == False):
            acc = input("Please give your account a name: ")
            if acc in self.account:
                print("Please enter a different name: ")
                continue
            else:
                self.account[acc] = BankAccount(int_rate=0.02, balance=0)
                success = True

    def display_account(self):
        print(self.account.keys())

    
trong = User("Trong", "Trong@gmail.com")
ethan = User("Ethan", "Ethan@gmail")

print("Trong: ") 
trong.display_user_balance("default")
trong.make_deposit(100,"default")
trong.display_user_balance("default")
trong.transfer_money(50,ethan, "default")
trong.display_user_balance("default")
trong.display_account()
trong.enroll_new_account()
trong.display_account()
print("Ethan: ")
ethan.display_user_balance("default")


