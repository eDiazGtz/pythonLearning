# The BankAccount class should have a balance. When a new BankAccount instance is created, if an amount is given, 
# the balance of the account should initially be set to that amount; otherwise, the balance should start at $0. 
# The account should also have an interest rate, saved as a decimal (i.e. 1% would be saved as 0.01), 
# which should be provided upon instantiation. (Hint: when using default values in parameters, the order of parameters matters!)

# The class should also have the following methods:

# deposit(self, amount) - increases the account balance by the given amount
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; 
# if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
# 
# display_account_info(self) - print to the console: eg. "Balance: $100"
# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)



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

# Create 2 accounts  
# To the first account, make 3 deposits and 1 withdrawal, then calculate interest and display the account's info all in one line of code (i.e. chaining)  
# To the second account, make 2 deposits and 4 withdrawals, then calculate interest and display the account's info all in one line of code (i.e. chaining)

checking = BankAccount(0.01)
savings = BankAccount(0.02, 500)

checking.deposit(1).deposit(2).deposit(3).withdraw(1).yieldInterest().displayAccountInfo() #result 5.05  

savings.deposit(10).deposit(20).withdraw(2.5).withdraw(2.5).withdraw(2.5).withdraw(2.5).yieldInterest().displayAccountInfo() #520 + 10.4 = 530.4
