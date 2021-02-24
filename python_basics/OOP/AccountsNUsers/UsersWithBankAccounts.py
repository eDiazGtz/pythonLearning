from . import BankAccount

class User:
    def __init__(self, uName, uEmail):
        self.name = uName
        self.name = uEmail
        self.account = BankAccount(intRate=0.02)
        self.accounts = []

    # def addAccount(self, accountName):
        #Need to create a way to create account with name
        #Value should be a new INSTANCE of the BankAccount Class.
        #Also need to update all other methods to include the name of WHICH account is being used. 

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
