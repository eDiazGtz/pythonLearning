# If you've been following along, you're going to utilize the User class we've been discussing for this assignment.

# For this assignment, we'll add some functionality to the User class:

# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance


# Create a file with the User class, including the __init__ and make_deposit methods  
# Add a make_withdrawal method to the User class  
# Add a display_user_balance method to the User class  
# Create 3 instances of the User class  
# Have the first user make 3 deposits and 1 withdrawal and then display their balance  
# Have the second user make 2 deposits and 2 withdrawals and then display their balance  
# Have the third user make 1 deposits and 3 withdrawals and then display their balance  

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = 10

    def makeDeposit(self, amount):
        self.account += amount

    def makeWithdrawal(self, amount):
        self.account -= amount

    def displayUserBalance(self):
        print(self.account)


# edgar = User("Edgar", "e@e.com")
# edgar.makeDeposit(10)
# edgar.makeWithdrawal(15)
# edgar.displayUserBalance()

kaladin = User("Kaladin", "kal@whatisthis.com")
shallan = User("Shallan", "shallan@jsnah.com")
adolin = User("Adolin", "adolin@dalinarkholin.com")

# Have the first user make 3 deposits and 1 withdrawal and then display their balance  
kaladin.makeDeposit(1)
kaladin.makeDeposit(5)
kaladin.makeDeposit(500)
kaladin.makeWithdrawal(506)
kaladin.displayUserBalance()

# Have the second user make 2 deposits and 2 withdrawals and then display their balance  
shallan.makeDeposit(2000)
shallan.makeDeposit(200)
shallan.makeWithdrawal(1500)
shallan.makeWithdrawal(710)
shallan.displayUserBalance()

# Have the third user make 1 deposits and 3 withdrawals and then display their balance 
adolin.makeDeposit(10)
adolin.makeWithdrawal(2000)
adolin.makeWithdrawal(5000)
adolin.makeWithdrawal(10000)
adolin.displayUserBalance()
