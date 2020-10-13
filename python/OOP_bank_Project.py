
class Account():

    def __init__(self, owner, balance):
        Account.owner = owner
        Account.balance = balance

    def __repr__(self):
        return f"owner:{self.owner}, balance:{self.balance}"

    def deposit(self, deposit):
        self.balance = self.balance + deposit
        print('Succeed')
        return self.balance


    def withdraw(self, withdraw):
        self.balance = self.balance - withdraw
        if self.balance < 0:
            return "Not enough balance in your account!!!"
        else:
            print('Succeed')
            return self.balance


acct1 = Account('Jose',100)



print(acct1)




# Show the account owner attribute
print(acct1.owner)




# Show the account balance attribute
print(acct1.balance)




# Make a series of deposits and withdrawals
print(acct1.deposit(50))




print(acct1.withdraw(75))




# Make a withdrawal that exceeds the available balance
print(acct1.withdraw(500))
