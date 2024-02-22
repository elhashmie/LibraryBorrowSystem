import mysql.connector

def loginadmin(c,d):
        AdminID=c
        password=d
        
        print()
        mycursor.execute("SELECT Password from AdminRecord where AdminID={0}".format("\'"+AdminID+"\'"))
        result=mycursor.fetchone()
        if result:
            temp,=result 
            if temp==password: 
                return 1
            else :
                return 0
        else :
            return 0
def loginuser(c,d):
        UserID=c
        password=d
        
        print()
        mycursor.execute("SELECT Password from UserRecord where UserID={0}".format("\'"+UserID+"\'"))
        result=mycursor.fetchone()
        if result:
            temp,=result 
            if temp==password: 
                return 1
            else :
                return 0
        else :
            return 0
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="Library")
mycursor=mydb.cursor()
