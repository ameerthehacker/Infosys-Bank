from Database import Database as db

class Admin:
    'Class to maintain admin info'

    def __init__():
        pass
    
    @staticmethod
    def authenticate(username, password):
        query = "SELECT * FROM admins WHERE username = %s AND password = %s"
        cur = db.getCursor()
        cur.execute(query, (username, password))
        return cur.fetchone() != None


