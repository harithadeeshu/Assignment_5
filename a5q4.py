class Account:

    def __init__(self, title, Balance):
        self.title = title
        self.Balance = Balance
        self.interestRate = 0

class SavingsAccount(Account):

    def __init__(self, title, Balance, interestRate):
        self.title = title
        self.Balance = Balance
        self.interestRate = interestRate

account = Account("Ashish", 5000)
print(account.title, account.Balance)
savingsAccount = SavingsAccount("Ashish", 5000, 5)
print(savingsAccount.title, savingsAccount.Balance, savingsAccount.interestRate)