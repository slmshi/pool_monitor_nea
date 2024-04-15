import sqlite3
import time
class ResultData():

    def __init__(self):
        self.__con = sqlite3.connect("databases\main.db")
        self.__cur = self.__con.cursor()

    def view(self):
        data = self.__cur.execute("SELECT * FROM ResultData")
        print(data.description)
    
    def reset(self):
        self.__cur.execute("DROP TABLE ResultData")
        self.__con.commit()
        self.__cur.execute("""CREATE TABLE ResultData(
            DataID int NOT NULL, 
            RecordID int NOT NULL, 
            FilterID int, 
            PoolCheckID int, 
            checkID int, 
            date DATE, 
            time DATETIME,
            PRIMARY KEY (DataID), 
            FOREIGN KEY (RecordID) REFERENCES Main(RecordID),
            FOREIGN KEY (FilterID) REFERENCES Filters(FilterID), 
            FOREIGN KEY (PoolID) REFERENCES PoolCheck(PoolID), 
            FOREIGN KEY (checkID) REFERENCES Checks(checkID));""")
        self.__con.commit()

    def addtO(self, PoolCheckID, FilterID, RecordID, CheckID):
        #get time and date
        datetime = self.getdatetime()
        date = datetime[0]
        time = datetime[1]

        dataID = self.getdataID()

        #get dataID
        data = (dataID, RecordID, FilterID, PoolCheckID, CheckID, date, time)
        self.__cur.execute(
            "INSERT INTO ResultData (DataID, RecordID, FilterID, PoolCheckID, checkID, date, time) VALUES (?,?,?,?,?,?)", data)
        self.__con.commit()
        
    def getdatetime(self):
        datetime = time.strftime("%Y %b %d,%H:%M:%S")
        datetime = datetime.split(",")
        return datetime

    def getdataID(self):
        dataid = self.__cur.execute("SELECT COUNT(DataID) FROM ResultData")
        dataid = dataid.fetchall()
        dataid = dataid[0][0]
        return dataid + 1

    def getPoolCheckID(self):
        dataid = self.__cur.execute("SELECT COUNT(PoolCheckID) FROM ResultData")
        dataid = dataid.fetchall()
        dataid = dataid[0][0]
        return dataid + 1

    def getRecordData(self, RecordID):
        data = self.__cur.execute("SELECT userID WHERE RecordID=" + str(RecordID))
        print(data.fetchall())

    def getFilterData(self, FilterID):
        dataid = self.__cur.execute("SELECT COUNT(FilterID) FROM ResultData")
        dataid = dataid.fetchall()
        dataid = dataid[0][0]
        return dataid + 1

    def getCheckData(self, CheckID):
        dataid = self.__cur.execute("SELECT COUNT(checkID) FROM ResultData")
        dataid = dataid.fetchall()
        dataid = dataid[0][0]
        return dataid + 1

    def close(self):
        self.__con.close()
