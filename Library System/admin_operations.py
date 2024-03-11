import mysql.connector
from connect import DatabaseConnection
from abc import ABC, abstractmethod

# Database connection using Singleton pattern
db_connection = DatabaseConnection()
mydb = db_connection.mydb
mycursor = db_connection.mycursor

# Usage:
db_connection = DatabaseConnection()
mydb = db_connection.mydb
mycursor = db_connection.mycursor

class AdminCommand(ABC):
    @abstractmethod
    def execute(self):
        pass

class DisplayAdminCommand(AdminCommand):
    def __init__(self, mycursor):
        self.mycursor = mycursor

    def execute(self):
        print()
        print("Admin Records: \n")
        self.mycursor.execute("SELECT * FROM AdminRecord")
        records = self.mycursor.fetchall()
        row_no = 0
        for rows in records:
            row_no += 1
            print("******************************", "Row no.", row_no, "******************************")
            print("\t             AdminID: ", rows[0])
            print("\t            Password: ", rows[1])
            print()
        x = input("Press Enter to continue")

# Usage:
command = DisplayAdminCommand(mycursor)
command.execute()