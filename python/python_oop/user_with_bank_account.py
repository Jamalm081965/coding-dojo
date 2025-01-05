class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print(f"Insufficient funds: {self.balance}. Charging a $5 fee.")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance:.2f}")

    def yield_interest(self, interest_rate):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self


class User:
    def __init__(self, name, email):
        self.name = name 
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    def make_deposit(self):
        self.account.deposit(100)
        print(self.account.deposit)

    def make_withdraw(self):
        self.account.withdraw()

    def display_user_balance(self):
        self.account.display_account_info

# Create an instance of BankAccount
account_lee = BankAccount(0.02, 300)

# Call the display_balance method
account_lee.display_account_info()

# Deposit money and display balance again
account_lee.deposit(200)
account_lee.display_account_info()

# Withdraw money and display balance
account_lee.withdraw(70)
account_lee.display_account_info()
# calculating the interest
account_lee.yield_interest(0.02)
account_lee.display_account_info()
