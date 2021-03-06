from Account import Account

class CAccount(Account):
    balance = 0
    min_balance = 5000

    def deposit(self, amount):
        self.balance += amount
        super(CAccount, self).saveBalance()
        super(CAccount, self).deposit(amount)
        return 1
        
    def withdraw(self, amount):
        if self.balance-self.min_balance >= amount:
            self.balance -= amount
            super(CAccount, self).saveBalance()
            super(CAccount, self).withdraw(amount)
            return 1
        else:
            return 0

    @staticmethod
    def createAccount(user_id):
        super(CAccount).createAccount(user_id, 'CA', 5000)
