class BankAccount:
    def __init__(self, intRate = 0.01, bal = 0):
        self.interest = intRate
        self.balance = bal
    
    def deposit(self, amount):
        if (amount <= 0):
            print("Must deposit positive amount. Make a withdrawal for reducing balance.")
            return self
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance <= 0):
            print("Cannot withdraw on Empty or Overdrawn Account. Please deposit funds and try again.")
            return self
        elif (amount > self.balance):
            print("Insufficient Funds: Charging Overdraft Fee $35")
            self.balance -= amount + 35
            return self
        else:
            self.balance -= amount
            return self

    def displayAccountInfo(self):
        print(f"Account Info: Balance: {self.balance}   Interest Rate: {self.interest}")
        return self

    def yieldInterest(self):
        if(self.balance <= 0):
            print("Must have positive balance to add interest. Please deposit funds and try again.")
            return self
        self.balance += self.balance*self.interest
        return self

class User:
    def __init__(self, uName, uEmail):
        self.name = uName
        self.name = uEmail
        self.account = BankAccount(intRate=0.02)

    def depositFromBank(self, amount):
        self.account.deposit(amount)
        return self

    def withdrawFromBank(self, amount):
        self.account.withdraw(amount)
        return self

    def seeMyBalance(self):
        self.account.displayAccountInfo()
        return self

    

max = User('Max', 'mAxe@gmail.com')
max.depositHundoP()
