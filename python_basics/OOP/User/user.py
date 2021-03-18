class User:
    def __init__(self, uName, uEmail):
        self.name = uName
        self.email = uEmail
        self.accountBalance = 0

    def makeDeposit(self, amount):
        self.accountBalance += amount
        return self
    def makeWithdrawal(self, amount):
        self.accountBalance -= amount
        return self
    def displayUserBalance(self):
        print(self.accountBalance)
        return self
    def transferMoney(self, otherUser, amount):
        otherUser.makeDeposit(amount)
        self.makeWithdrawal(amount)
        return self

orion = User('Orion', 'oAngelcrest@gmail.com')
silver = User('Silver', 'sRevlis@gmail.com')
luna = User('Luna', 'lStarfall@gmail.com')

orion.makeDeposit(50).makeDeposit(150).makeDeposit(500).makeWithdrawal(25).displayUserBalance()

silver.makeDeposit(500).makeDeposit(500).makeWithdrawal(1000).displayUserBalance()

luna.makeDeposit(2000).makeDeposit(2000).makeDeposit(2000).makeWithdrawal(100).displayUserBalance()

orion.transferMoney(luna, 75).displayUserBalance()
luna.displayUserBalance()

