import mysql.connector
def create_connection():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="Library")
    mycursor=mydb.cursor()
