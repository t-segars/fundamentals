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
        print(f"Account Interest Rate: $ {self.int_rate}")
        print(f"Account Balance: $ {self.balance}")
        print("******************************")
        return self

    def yield_interest(self):
        self.balance = self.balance * self.int_rate + self.balance
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()
        return cls

checking = BankAccount(0.03)
savings =  BankAccount(0.07)

checking.deposit(50).deposit(100).deposit(150).withdraw(150).yield_interest()
savings.deposit(15000).deposit(5000).withdraw(1000).withdraw(2500).withdraw(750).withdraw(220).yield_interest()

BankAccount.print_all_accounts()