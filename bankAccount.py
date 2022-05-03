class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        return self

    def display_account_info(self):
        return(f"Balance: ${self.balance}")

    def yield_interest(self):
        self.balance = self.balance * self.int_rate + self.balance
        return self

class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = BankAccount (int_rate = 0.02, balance = 0)

    def transfer_money(self, amount, other_user):
        self.account.balance = self.account.balance - amount
        other_user.account.balance = other_user.account.balance + amount 
        print(f"{self.name} just transferred {amount} dollars to {other_user.name}")
        return self

    def display_account_info(self):
        print(f"Name: {self.name}, {self.account.display_account_info()}")
        return self

checking = BankAccount(0.03)
savings =  BankAccount(0.07)
frog = User("Frog","frog@gmail.com")
pig = User("Pig","pig@yahoo.com")
bear = User("Bear","bear@hotmail.com")

frog.account.deposit(300)
frog.display_account_info()
pig.account.deposit(250)
pig.display_account_info()
pig.transfer_money(300,frog)
bear.account.deposit(500).withdraw(75).display_account_info()