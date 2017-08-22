from Database import Database as db
from datetime import datetime

class Account(object):
    user_id = 0
    id = 0
    balance = 0
    type = ""
    
    def __init__(self, id = None):
        if id is None:
            pass
        else:
            self.id = id
            cur = db.getCursor()
            query = "SELECT * FROM accounts WHERE id = %s"
            cur.execute(query, [[id]])
            account = cur.fetchone()
            self.balance = account[4]
            self.user_id = account[1]
            self.type = account[2]

    def deposit(self, amount):
        query = "INSERT INTO transactions (user_id, account_id, type, amount) VALUES(%s, %s, %s, %s)"
        cur = db.getCursor()
        cur.execute(query, (self.user_id, self.id, 'DEPOSIT', amount))
        db.commit()

    def withdraw(self, amount):
        query = "INSERT INTO transactions (user_id, account_id, type, amount) VALUES(%s, %s, %s, %s)"
        cur = db.getCursor()
        cur.execute(query, (self.user_id, self.id, 'WITHDRAW', amount))
        db.commit()

    def saveBalance(self):
        query = "UPDATE accounts SET balance = %s WHERE id = %s"
        cur = db.getCursor()
        cur.execute(query, (self.balance, self.id))
        db.commit()

    @staticmethod 
    def accountExist(id):
        cur = db.getCursor()
        query = "SELECT * FROM accounts WHERE id = %s"
        cur.execute(query, [[id]])
        account = cur.fetchone()
        return account != None

    @staticmethod
    def createAccount(user_id, account_type, balance):
        query = "INSERT INTO accounts (user_id, type, balance) VALUES(%s, %s, %s)"
        cur = db.getCursor()
        if cur.execute(query, (user_id, account_type, balance)):
            db.commit()
            return 1
        else:
            return 0
    
    def getStatements(self):
        query = "SELECT * FROM transactions WHERE account_id = %s and user_id = %s"
        cur = db.getCursor()
        cur.execute(query, [[self.id], [self.user_id]])
        return cur.fetchall()

    def closeAccount(self):
        date = datetime.today().strftime('%Y-%m-%d')
        query = "UPDATE accounts SET active = 0, closed_date = %s"
        cur = db.getCursor()
        cur.execute(query, [[date]])
        db.commit()
        

        

