import MySQLdb as mysql

class Database:
    'Class for database connection to mysql'
    db = None

    @staticmethod
    def getCursor(server = 'localhost', user ='root', password ='pwd', database = 'bank'):
        if Database.db is None:
            Database.db = mysql.connect('localhost', 'root', 'pwd', 'bank_database')            
        return Database.db.cursor()

    @staticmethod
    def commit():
        Database.db.commit()