import mysql.connector
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.connect_to_database()
        return cls._instance

    def connect_to_database(self):
        self.mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="Library")
        self.mycursor = self.mydb.cursor()
