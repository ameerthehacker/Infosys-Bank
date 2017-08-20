from Database import Database as db

class User:
    'Class to maintain user info'

    first_name = ""
    last_name = ""
    password = ""
    address = ""
    city = ""
    state = ""
    pincode = ""

    def __init__(self, first_name, last_name, password, address, city, state, pincode):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.address = address
        self.city = city
        self.state = state
        self.pincode = pincode

    def save(self):
        query = "INSERT INTO users (first_name, last_name, password, address, city, state, pincode) VALUES(%s, %s, %s, %s, %s, %s, %s)"
        cur = db.getCursor()
        if cur.execute(query, (self.first_name, self.last_name, self.password, self.address, self.city, self.state, self.pincode)):
            db.commit()
            return 1
        else:
            return 0
    
    @staticmethod
    def authenticate(id, password):
        query = "SELECT * FROM users WHERE id = %s AND password = %s"
        cur = db.getCursor()
        cur.execute(query, (id, password))
        return cur.fetchone() != None


