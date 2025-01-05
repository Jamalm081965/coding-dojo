class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.deposit + amount
        return self.balance

    def with_draw(self, amount):
        if self.balance > amount:
            self.balance - amount
            return self 
        else:
            print(f"You have Insufficient funds: {self.balance} Charging a $5 fee")
            self.balance - 5
            return self

    def display_account_info(self):
        print(f"Balance {self.balance}")

    def yield_interest(self):
        self.balance * self.int_rate
        return self

# Create an instance of BankAccount
account_jamal = BankAccount(0.01, 100)

# Call the display_balance method
account_jamal.display_account_info()

# Deposit money and display balance again
account_jamal.deposit(50)

# Withdraw money and display balance
account_jamal.with_draw(30)
account_jamal.yield_interest(0.01)


# Create an instance of BankAccount
account_lee = BankAccount(0.02, 300)

# Call the display_balance method
account_lee.display_account_info()

# Deposit money and display balance again
account_lee.deposit(200)

# Withdraw money and display balance
account_lee.with_draw(70)
# calculating the interest
account_lee.yield_interest(0.03)
###########################################
corrected sample version
##########################################

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
# explaination 
"""
issues Fixed:
Method Overwriting (deposit method):

You defined the deposit method twice. The second definition overwrote the first one. I removed the incorrect second deposit method.
Logical errors in withdraw method:

You were not actually subtracting the withdrawal amount from the balance. Instead of self.balance - amount, it should be self.balance -= amount.
The condition to check for insufficient funds was corrected to if self.balance >= amount.
The $5 fee deduction was corrected to self.balance -= 5.
Interest calculation in yield_interest method:

You need to update the balance after applying the interest. I added self.balance += self.balance * self.int_rate.
Interest should only be applied if the balance is positive.
Display format in display_account_info method:

I formatted the balance to display as a monetary value using :.2f.

# Create an account with 2% interest and a balance of $100
account = BankAccount(0.02, 100)
"""

# Deposit $50
account.deposit(50).display_account_info()

# Withdraw $30
account.withdraw(30).display_account_info()

# Try to withdraw more than the balance
account.withdraw(150).display_account_info()

# Apply interest
account.yield_interest().display_account_info()
