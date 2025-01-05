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

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
# Create an account with 2% interest and a balance of $100
account = BankAccount(0.02, 100)

# Deposit $50
account.deposit(50).display_account_info()

# Withdraw $30
account.withdraw(30).display_account_info()

# Try to withdraw more than the balance
account.withdraw(150).display_account_info()

# Apply interest
account.yield_interest().display_account_info()
