import sqlite3
import time
class login():

    def __init__(self):
        self.__con = sqlite3.connect("databases\Main.db")
        self.__cur = self.__con.cursor()
        print("Established")
    
    def view(self): #debug
        count = self.__cur.execute("SELECT COUNT(userID) from User")
        count = count.fetchone()
        count = count[0]
        for i in range(count):
            data = self.__cur.execute(f"SELECT * FROM User WHERE userID='{i+1}'") 
            data = data.fetchall()
            data = data[0]
            print(data)

    def UsernamegetByUserID(self, userID): #gets the username by user id
        data = self.__cur.execute(f"SELECT username FROM User WHERE userID='{userID}'")
        data = data.fetchone()
        print(data[0])
        return str(data[0])

    def ifEmailExists(self, email): #checks if the email exists in the database
        print(email)
        data = self.__cur.execute(f"SELECT userID from User where email='{email}'")
        data = data.fetchone()
        if data:
            print("User Exists")
            return True
        else:
            print("User does not Exists")
            return False

    def userLogin(self, username, password, email): # logs in the user
        check = self.__cur.execute(f"SELECT UserID FROM User WHERE email='{email}' AND username='{username}' AND password='{password}'")
        check = check.fetchone()
        print(check)
        if check:
            return check[0]
        else:
            print("wrong")
            return False

    def reset(self): # resets the table (only used)
        self.__cur.execute("DROP TABLE User")
        self.__con.commit()
        self.__cur.execute("CREATE TABLE User(userID int NOT NULL,username varchar(255) NOT NULL,email varchar(255) NOT NULL,password varchar(255) NOT NULL,noOfRecords int NOT NULL,PRIMARY KEY (userID));")

    def createUserID(self): # gets a new user id
        data = self.__cur.execute("SELECT COUNT(userID) FROM User")
        data = data.fetchone()
        data = data[0]
        return data + 1

    def addto(self, username, email, password): # creates a new user
        UserID = self.createUserID()
        data = (UserID, username, email, password, 0)

        self.__cur.execute("INSERT INTO User (userID, username, email, password, noOfRecords) VALUES (?,?,?,?,?)", data)
        self.__con.commit()
        print("Successful")

    def validatepswd(self, password): # validates the password
        hasnumber = False
        hasspecial = False
        hascapital = False
        specialchars = ["'",'#','.',',',';','@','£','$','%','^','&']

        if len(password) >= 8:
            for i in password:
                if i.isnumeric():
                    hasnumber = True
                elif i in specialchars:
                    hasspecial = True
                elif i.capitalize() == i:
                    hascapital = True

        if not hasnumber or not hasspecial or not hascapital:
            print("Invalid password")
            return False
        else:
            return True

    def validateemail(self, email): # validates the email
        if "@" in email:
            return not self.ifEmailExists(email)
        else:
            return False

    def validateUser(self, username): # Validates the username
        data = self.__cur.execute(f"SELECT * from User where username='{username}'")
        data = data.fetchone()
        if data:
            print("Data")
        else:
            print("no data")

    def login(self): #logs in the player (used in debug)
        email = input("Email: ")
        while self.validateemail(email):
            email = input("(Invalid input, Try Again) Email: ")

        username = input("Username: ")
        password = input("Password: ")
        while self.userLogin(username, password, email):
            password = input("(Incorrect) Password: ")

        self.__con.close()

    def signup(self): # signs a user up (used in debug)
        username = input("Username: ")
        email = input("Email: ")
        while not self.validateemail(email):
            email = input("(not valid, Try Again) Email: ")
        password = input("Password: ")
        while not self.validatepswd(password):
            password = input("(not valid, Try Again) Password: ")
        self.addto(username, email, password)
        self.__con.close()

    def close(self): #allows closing of the database outside of the class
        self.__con.close()