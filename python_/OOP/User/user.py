class User:
    def __init__(self, uName, uEmail):
        self.name = uName
        self.email = uEmail
        self.accountBalance = 0

    def makeDeposit(self, amount):
        self.accountBalance += amount
    def makeWithdrawal(self, amount):
        self.accountBalance -= amount
    def displayUserBalance(self):
        print(self.accountBalance)
    def transferMoney(self, otherUser, amount):
        self.makeWithdrawal(amount)
        otherUser.makeDeposit(amount)

orion = User('Orion', 'oAngelcrest@gmail.com')
silver = User('Silver', 'sRevlis@gmail.com')
luna = User('Luna', 'lStarfall@gmail.com')

orion.makeDeposit(50)
orion.makeDeposit(150)
orion.makeDeposit(500)
orion.makeWithdrawal(25)
orion.displayUserBalance()

silver.makeDeposit(500)
silver.makeDeposit(500)
silver.makeWithdrawal(1000)
silver.displayUserBalance()

luna.makeDeposit(2000)
luna.makeDeposit(2000)
luna.makeDeposit(2000)
luna.makeWithdrawal(100)
luna.displayUserBalance()

orion.transferMoney(luna, 75)
orion.displayUserBalance()
luna.displayUserBalance()

