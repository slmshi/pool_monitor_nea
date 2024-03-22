import sqlite3
import time
import json
import random

"""
Redundant function

def createonetable():
    name = input("Enter the name: ")
    again = 1
    fields = ""

    while again == 1:
        fieldname = input("Enter the field name (Enter a number to quit): ")
        if fieldname.isnumeric():
            again = 0
        else:
            fields = fields + f"{fieldname},"
    fields = fields.rstrip(",")
    con = sqlite3.connect(f"databases/{name}.db")
    cur = con.cursor()
    cur.execute(f"CREATE TABLE {name} ({fields});")*
    con.commit()
    con.close()
    return name"""

#class to view each database
class database():
    def __init__(self):
        con = sqlite3.connect("databases\main.db")
        self.__cur = con.cursor()

    def AddRecord(self):
        #Request user
        user = input("Enter Username: ")

    def viewPoolCheck(self):
        data = self.__cur.execute("SELECT * FROM PoolCheck")
        print(data.description)

    def viewChecks(self):
        data = self.__cur.execute("SELECT * FROM Checks")
        print(data.description)

    def viewFilters(self):
        data = self.__cur.execute("SELECT * FROM Filters")
        print(data.description)

    def viewUser(self):
        data = self.__cur.execute("SELECT * FROM User")
        print(data.description)

    def createalltables(self):
        con = sqlite3.connect("databases\Main.db")
        cur = con.cursor()
        with open("sql/createalltables.json", "r") as f:
            scripts = json.load(f)
        
        for i in scripts:
            cur.execute(i)

        con.close()

def databasepanel(name):
    print(f"""
    ****** Current Database: {name}.db ******

    1. Show 
    2. Delete
    3. Add items
    4. Exit to Menu
    """)
    choice = input("Enter the choice: ")
    tries = 3
    while choice.isnumeric() != True and tries:
        tries -= 1
        print(f"Enter a number ({tries})")
        choice = input("Enter the choice: ")

    if choice.isnumeric():
        match int(choice):
            case 1:
                showDatabase(name)
            case 2:
                delete(name)
            case 3:
                addtodatabase(name)
            case 4:
                main()
    else:
        print("\n Not a number \n")
        main()
        
def viewAll(name):
    con = sqlite3.connect(f"databases/Main.db")
    cur = con.cursor()
    data = cur.execute('SELECT name from sqlite_master where type= "table"')
    tablelist = data.fetchall()
    index = 0
    print("Tables: ")
    for i in tablelist:
        index += 1
        data = cur.execute(f"SELECT * FROM {i[0]}")
        print(str(index) , "-", i[0])
        
    

def openfile():
    name = input("Enter the name of the database: ")
    tries = 3
    while os.path.isfile(f"databases/{name}.db") != True and tries:
        if tries == 0:
            print(f"Database not Found (1 try left)\n")
        else:
            print(f"Database not Found ({tries} tries left)\n")
        tries -= 1
        name = input("Enter the name of the database: ")

    if os.path.isfile(f"databases/{name}.db"):
        databasepanel(name)

def main():
    print("""****** Database manager ******
    1. Open Database
    2. Create Database
    3. Exit
    """)

    choice = input("Enter the choice: ")
    tries = 3
    while choice.isnumeric() != True and tries:
        tries -= 1
        print(f"Enter a number ({tries})")
        choice = input("Enter the choice: ")

    if choice.isnumeric():
        match int(choice):
            case 1:
                openfile()
            case 2:
                createtable()
            case 3:
                pass

viewAll("Main")