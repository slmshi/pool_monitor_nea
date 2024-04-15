import sqlite3

class Filter():
    def __init__(self):
        self.__con = sqlite3.connect("databases\main.db")
        self.__cur = self.__con.cursor()

    def menu(self):
        choice = input("""******[Menu]******
        1. """)

    def view(self):
        data = self.__cur.execute("SELECT * FROM Filter") 

        for i in data.description:
            print(i[0])
            count = self.__cur.execute("SELECT COUNT(FilterID) FROM Filter")
            count = count.fetchall()
            count = count[0][0]
            print(count)    

    def getNewID(self):
        data = self.__cur.execute("SELECT COUNT(FilterID) FROM Filter")
        data = data.fetchall()
        data = data [0][0]
        return data + 1

    def addto(self, data):
        self.FilterID = self.getNewID()
        data = [self.FilterID] + data
        self.__cur.execute("INSERT INTO Filter (FilterID, Skimmer, Main, Flowmeter, Strainers, FilterGauge) VALUES(?,?,?,?,?,?)", tuple(data))