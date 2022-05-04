class BankAccount:
    def __init__(self, int_rate = 0.025, balance = 0):
        self.rate = int_rate
        self.account_balance = balance


    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        if self.account_balance - amount > 0:
            self.account_balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5
        return self

    def display_account_info(self):
        print("Balance:", self.account_balance)
        return self


    def yield_interest(self, int_rate):
        if self.account_balance > 0:
            amount = self.rate * self.account_balance
            self.account_balance += amount
            return self

class User:
    def __init__(self, name, email, ):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)


Larry = User("Larry Stooge", "Larry@stooge.com")
Curly = User("Curly Stooge", "Curly@stooge.com")
Moe = User("Moe Stooge", "moe@stooge.com")

Larry.account.deposit(250).deposit(550).deposit(100).withdraw(200).display_account_info()

Curly.account.deposit(200).deposit(250).withdraw(100).withdraw(175).display_account_info()

Moe.account.deposit(800).withdraw(200).withdraw(300).withdraw(250).display_account_info()
