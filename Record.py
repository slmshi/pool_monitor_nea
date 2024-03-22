import sqlite3

class Record():
    def __init__(self, userID):
        self.__userID = userID
        self.con = sqlite3.connect("databases\Main.db")
        self.cur = self.con.cursor()

    def get_userID(self):
        return self.__userID

    def new_RecordID(self):
        return countdatabase(self.__userID) + 1

    def view(self):
        data = self.cur.execute("SELECT * FROM Record")
        print(data.description)

    def addto(self):
        RecordID = self.countdatabase("userID", self.__userID) + 1
        data = (self.__userID, self.__RecordID)
        self.cur.execute("INSERT INTO Record (userID, RecordID) VALUES (?,?)", data)
        self.con.commit()

    def reset(self):
        self.cur.execute("DROP TABLE Record")
        self.cur.execute(f"CREATE TABLE Record(userID int,RecordID int NOT NULL,FOREIGN KEY (userID) REFERENCES User(userID),FOREIGN KEY (RecordID) REFERENCES RecordData(DataID));")
        self.con.commit()

    def countdatabase(self, userID):
        amount = self.cur.execute(f"SELECT COUNT(userID) FROM Record WHERE userID = '{userID}'")
        count = amount.fetchall()
        count = count[0][0]
        return count