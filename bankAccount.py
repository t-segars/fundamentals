class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + amount
        print("Account balance has been updated : $", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print ("Insufficient Funds | Balance Available : $", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated ; $", self.balance)

    def display_account_info(self):
        return(f"Account balance: $", self.balance)

    def yield_interest(self):
        self.balance = self.balance * self.int_rate + self.balance
        return self

class User():
    def __int__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal details")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ",)

Tim(User)("Tim", 35,"male")
