class BankAccount:

    class_variable = 'initial'

    def __init__(self, amount):
        self.balance = amount

    def withdraw(self, amount):
        self.balance -= amount
        return amount

    def deposit(self, amount):
        self.balance += amount
        return amount

    def __str__(self):
        return self.__class__.__name__ + ': balance = ' + str(self.balance) + \
               ', class_variable = ' + self.class_variable


class MinimumBalanceAccount(BankAccount):

    def __init__(self, amount, minimum_balance):
        BankAccount.__init__(self, amount)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print('Sorry, balance can not be less then ' + str(self.minimum_balance))
        else:
            BankAccount.withdraw(self, amount)


BankAccount.balance = 200
print('BankAccount.balance = ' + str(BankAccount.balance))

BankAccount.class_variable = 'changed'
print('BankAccount.class_variable = ' + BankAccount.class_variable)

account = BankAccount(100)
print('account.balance = ' + str(account.balance))
money = account.deposit(100)


print('acoount to string:' + str(account))


fixed_account = MinimumBalanceAccount(300, 100)
fixed_account.withdraw(100)
print('fixed_account.balance = ' + str(fixed_account.balance))
fixed_account.withdraw(250)
print('fixed_account.balance = ' + str(fixed_account.balance))