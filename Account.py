from Database import Database as db

class Account:
    user_id = 0
    id = 0
    balance = 0
    
    def __init__(self, id = None):
        if id is None:
            pass
        else:
            self.id = id
            cur = db.getCursor()
            query = "SELECT * FROM account WHERE id = %s"
            cur.execute(query, (id))
            account = cur.fetchone()
            self.balance = cur['balance']
            self.user_id = cur['user_id']

    def deposit(self, amount):
        pass
    def withdraw(self, amount):
        pass

    @staticmethod
    def createAccount(user_id, account_type, balance):
        query = "INSERT INTO accounts (user_id, type, balance) VALUES(%s, %s, %s)"
        cur = db.getCursor()
        if cur.execute(query, (user_id, account_type, balance)):
            db.commit()
            return 1
        else:
            return 0
        

        

