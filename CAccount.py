from Account import Account

class CAccount(Accounr):
    balance = 0

    def deposit(self, amount):
        balance += amount
        return 1
        
    def withdraw(self, amount):
        if balance >= amount:
            balance -= amount
        return 1

