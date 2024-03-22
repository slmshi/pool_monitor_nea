import sqlite3

class Filter:
    #connects to the database
    def __init__(self):
        self.__con = sqlite3.connect("databases\main.db")
        self.__cur = self.__con.cursor()

    def view(self):
        data = self.__cur.execute("SELECT * FROM Filters") 

        for i in data.description:
            print(i[0])
            count = self.__cur.execute("SELECT COUNT(FilterID) FROM Filters")
            count = count.fetchall()
            count = count[0][0]
            print(count)

    def getNewID(self):
        data = self.__cur.execute("SELECT COUNT(FilterID) FROM Filters")
        data = data.fetchall()
        data = data [0][0]
        return data + 1

    def trueorfalse(self, strinput):
        y = ["y", "yes"]
        if strinput.lower() in y:
            return True
        else:
            return False

    #adds to the database
    def addto(self, FilterID, Skimmer, Main, Flowmeter, Strainers, MainWater, FilterGauge):
        FilterID = self.getNewID()
        # b = boolean
        # i = integer
        # s = string
        # f = float

        data = (FilterID, Skimmer, Main, Flowmeter, Strainers, MainWater, FilterGauge)

        self.__cur.execute("INSERT INTO Filters (FilterID, Skimmer, Main, Flowmeter, Strainers, MainWater, FilterGauge) VALUES(?,?,?,?,?,?,?)", data)
        self.__con.commit()