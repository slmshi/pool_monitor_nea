import sqlite3

class Check():
    def __init__(self):
        self.__con = sqlite3.connect("databases\main.db")
        self.__cur = self.__con.cursor()

    def menu(self):
        choice = input("""******[Menu]******
        1. """)

    def view(self):
        data = self.__cur.execute("SELECT * FROM Check") 

        for i in data.description:
            print(i[0])
            count = self.__cur.execute("SELECT COUNT(checkID) FROM Check")
            count = count.fetchall()
            count = count[0][0]
            print(count)    

    def getNewID(self):
        data = self.__cur.execute("SELECT COUNT(checkID) FROM Check")
        data = data.fetchall()
        data = data [0][0]
        return data + 1

    def addto(self, data):
        self.CheckID = self.getNewID()
        data = [self.CheckID] + data
        self.__cur.execute("INSERT INTO Check (CheckID, Alkalinity, Calcium, DissolvedSolids, SatIndex, VisualClarity, PoolTemp) VALUES(?,?,?,?,?,?,?)", tuple(data))