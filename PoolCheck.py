import sqlite3

class PoolCheck():
    def __init__(self):
        self.__con = sqlite3.connect("databases\main.db")
        self.__cur = self.__con.cursor()

    def menu(self):
        choice = input("""******[Menu]******
        1. """)

    def view(self):
        data = self.__cur.execute("SELECT * FROM PoolCheck") 

        for i in data.description:
            print(i[0])
            count = self.__cur.execute("SELECT COUNT(PoolID) FROM PoolCheck")
            count = count.fetchall()
            count = count[0][0]
            print(count)    

    def getNewID(self):
        data = self.__cur.execute("SELECT COUNT(PoolID) FROM PoolCheck")
        data = data.fetchall()
        data = data [0][0]
        return data + 1

    def addto(self, data):
        self.PoolID = self.getNewID()
        data = [self.PoolID] + data
        self.__cur.execute("INSERT INTO PoolCheck (PoolID, FreeChlorine, TotalChlorine, CombinedChlorine, pH, Temperature) VALUES(?,?,?,?,?,?)", tuple(data))