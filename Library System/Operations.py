import Book
import User
import Admin
import Tables
import mysql.connector
import connection
#----------------------------------------------------------------------------------------
#Operations for Admin Menu

def BookManagement():
    while True:
        print("\t\t\t Book Record Management\n")
        print("==============================================================")
        print("1. Add Book Record")
        print("2. Display Book Records")
        print("3. Search Book Record")
        print("4. Delete Book Record")
        print("5. Update Book Record")
        print("6. Return to Main Menu")
        print("===============================================================")
        choice=int(input("Enter Choice between 1 to 6-------> : "))
        if choice==1:
            Book.insertBook()
        elif choice==2:
            Book.displayBook()
        elif choice==3:
            Book.searchBook()
        elif choice==4:
            Book.deleteBook()
        elif choice==5:
            Book.updateBook()
        elif choice==6:
            return
        else:
            print("Wrong Choice......Enter Your Choice again")
            x=input("Press Enter to continue")
#----------------------------------------------------------------------------------------
def UserManagement():
    while True:
        print("\t\t\t User Record Management\n")
        print("==============================================================")
        print("1. Add User Record")
        print("2. Display User Records")
        print("3. Search User Record")
        print("4. Delete User Record")
        print("5. Update User Record")
        print("6. Return to Main Menu")
        print("===============================================================")
        choice=int(input("Enter Choice between 1 to 6-------> : "))
        if choice==1:
            User.insertUser()
        elif choice==2:
            User.displayUser()
        elif choice==3:
            User.searchUser()
        elif choice==4:
            User.deleteUser()
        elif choice==5:
            User.updateUser()
        elif choice==6:
            return
        else:
            print("Wrong Choice......Enter Your Choice again")
            x=input("Press Enter to continue")
#----------------------------------------------------------------------------------------
def AdminManagement():
    while True:
        print("\t\t\t Admin Record Management\n")
        print("==============================================================")
        print("1. Add Admin Record")
        print("2. Display Admin Records")
        print("3. Search Admin Record")
        print("4. Delete Admin Record")
        print("5. Update Admin Record")
        print("6. Return to Main Menu")
        print("===============================================================")
        choice=int(input("Enter Choice between 1 to 5-------> : "))
        if choice==1:
            Admin.insertAdmin()
        elif choice==2:
            Admin.displayAdmin()
        elif choice==3:
            Admin.searchAdmin()
        elif choice==4:
            Admin.deleteAdmin()
        elif choice==5:
            Admin.updateAdmin()
        elif choice==6:
            return
        else:
            print("Wrong Choice......Enter Your Choice again")
            x=input("Press Enter to continue")

#----------------------------------------------------------------------------------------

# User Menu Operations 

def BookCentre():
    while True:
        print("\t\t\t Book Centre \n")
        print("==============================================================")
        print("1. List of all Books ")
        print("2. Issue Book ")
        print("3. Display Borrowed Book Records ")
        print("4. Return Borrowed Book ")
        print("5. Return to Main Menu ")
        print("===============================================================")
        choice=int(input("Enter Choice between 1 to 4-------> : "))
        if choice==1:
            Book.BookList()
        elif choice==2:
            Book.IssueBook()
        elif choice==3:
            Book.ShowIssuedBook()
        elif choice==4:
            Book.returnBook()
        elif choice==5:
            return
        else:
            print("Wrong Choice......Enter Your Choice again")
            x=input("Press Enter to continue")
#----------------------------------------------------------------------------------------
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="Library")
mycursor=mydb.cursor()
#connect.create_connection()
