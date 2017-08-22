from Account import Account

class SAccount(Account):
    balance = 0

    def deposit(self, amount):
        self.balance += amount
        super(Account, self).saveBalance()
        super(CAccount, self).deposit(amount)
        return 1
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            super(SAccount, self).saveBalance()
            super(SAccount, self).withdraw(amount)
            return 1
        else:
            return 0

    @staticmethod
    def createAccount(user_id):
        super(SAccount).createAccount(user_id, 'SA', 0)
