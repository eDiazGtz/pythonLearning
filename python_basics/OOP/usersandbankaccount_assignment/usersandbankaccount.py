class BankAccount:
    def __init__(self, intRate, balance=0):
        self.balance = balance
        self.intRate = intRate

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if(amount <= self.balance):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def displayAccountInfo(self):
        print("Balance:", self.balance)
        return self
    
    def yieldInterest(self):
        if(self.balance >= 0):
            self.balance += self.balance*self.intRate
        return self

# -------------------------------------------------------------------

# Update the User class __init__ method  
# Update the User class make_deposit method  
# Update the User class make_withdrawal method  
# Update the User class display_user_balance method

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0.01)

    def makeDeposit(self, amount):
        self.account.deposit(amount)
        return self

    def makeWithdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def displayUserBalance(self):
        self.account.displayAccountInfo()
        return self

    def give_money(self, other_user, amount):
        self.makeWithdrawal(amount)
        other_user.makeDeposit(amount)
        print(f"{self.name} gave {amount} to {other_user.name}")
        return self

harry = User("Harry Potter", "voldilocks@hogwarts.com")
ron = User("Ron Weasley", "ilovehermione@hogwarts.com" )

# harry.makeDeposit(100).makeWithdrawal(50).displayUserBalance()
# harry.account.yieldInterest().displayAccountInfo()
# harry.displayUserBalance()

harry.give_money(ron, 100)