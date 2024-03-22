import sqlite3
import os
import json

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
    cur.execute(f"CREATE TABLE {name} ({fields});")
    con.commit()
    con.close()
    return name

def createalltables():
    con = sqlite3.connect("databases\Main.db")
    cur = con.cursor()
    with open("sql/createalltables.json", "r") as f:
        scripts = json.load(f)
    
    for i in scripts:
        cur.execute(i)

    con.close()

def viewRecord():
    con = sqlite3.connect("databases\Main.db")
    cur = con.cursor()

    data = cur.execute("SELECT * FROM Record")
    print(data.description)

def viewUser():
    con = sqlite3.connect("databases\Main.db")
    cur = con.cursor()

    data = cur.execute("SELECT * FROM User")
    print(data.description)

def viewResultData():
    con = sqlite3.connect("databases\Main.db")
    cur = con.cursor()

    data = cur.execute("SELECT * FROM ResultData")
    print(data.description)

def viewPoolCheck():
    con = sqlite3.connect("databases\Main.db")
    cur = con.cursor()

    data = cur.execute("SELECT * FROM PoolCheck")
    print(data.description)

def viewChecks():
    con = sqlite3.connect("databases\Main.db")
    cur = con.cursor()

    data = cur.execute("SELECT * FROM Checks")
    print(data.description)

def viewFilters():
    con = sqlite3.connect("databases\Main.db")
    cur = con.cursor()

    data = cur.execute("SELECT * FROM Filters")
    print(data.description)

def addtodatabase(name):
    con = sqlite3.connect(f"databases/{name}.db")
    cur = con.cursor()
    
    #gets the whole database
    data = cur.execute(f"""SELECT * from {name}""")
    fields = []

    for column in data.description:
        fields.append(column[0])

    record = ""
    for i in range(len(fields)):
        print(f"Fields: {fields}")
        detail = input(f"Enter the input for {fields[i]}: ")
        record += detail + ","

    record.rstrip(",")
    record = eval(record)    


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
    con = sqlite3.connect(f"databases/{name}.db")
    cur = con.cursor()
    data = cur.execute('SELECT name from sqlite_master where type= "table"')
    tablelist = data.fetchall()
    tables = []
    for i in range(len(tablelist)):
        tablename = tablelist[i][0]
        cur.execute(f"SELECT * FROM {tablename}")
        print(cur.fetchall())    

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