import sqlite3
import time
import json
import random
from PoolCheck import PoolCheck
from Record import Record
from ResultData import ResultData
from User import login as User
from Filter import Filter
from Check import Check
import os

class database():

    def __init__(self, userID):
        self.__con = sqlite3.connect("databases\main.db")
        self.__cur = self.__con.cursor()
        self.__UserID = userID
        self.pcID = 0
        self.cID = 0
        self.fID = 0
        self.rdID = 0
        self.rID = 0
    
    def createtable(self):
        self.createR()
        self.createPC()
        self.createC()
        self.createF()
        self.createU()
        self.createRD()
    
    def reset(self):
        os.remove("databases\\main.db")
        self.__con = sqlite3.connect("databases\main.db")
        self.__cur = self.__con.cursor()
        self.createtable()
    
    def createF(self):
        self.__cur.execute("""CREATE TABLE Filters(FilterID int NOT NULL,Skimmer BOOL NOT NULL,Main BOOL NOT NULL,Flowmeter int NOT NULL,Strainers BOOL NOT NULL,MainWater BOOL NOT NULL,FilterGauge BOOL NOT NULL, PRIMARY KEY (FilterID));""")
        self.__con.commit()
    
    def createC(self):
        self.__cur.execute("""CREATE TABLE Checks(checkID int NOT NULL,Alkalinity int NOT NULL,Calcium int NOT NULL,DissolvedSolids int NOT NULL,SatIndex float NOT NULL,VisualClarity float NOT NULL,PoolTemp float NOT NULL,PRIMARY KEY (checkID));""")
        self.__con.commit()

    def createU(self):
        self.__cur.execute("""CREATE TABLE User(userID int NOT NULL,username varchar(255) NOT NULL,email varchar(255) NOT NULL,password varchar(255) NOT NULL,noOfRecords int NOT NULL,PRIMARY KEY (userID));""")
        self.__con.commit()
        
    def createR(self):
        self.__cur.execute("""CREATE TABLE Record(userID int,RecordID int NOT NULL,FOREIGN KEY (userID) REFERENCES User(userID),FOREIGN KEY (RecordID) REFERENCES RecordData(DataID));""")
        self.__con.commit()
    
    def createPC(self):
        self.__cur.execute("""CREATE TABLE PoolCheck(PoolID int NOT NULL,FreeChlorine float NOT NULL,TotalChlorine float NOT NULL,CombinedChlorine float NOT NULL,pH float NOT NULL,Temperature float NOT NULL,PRIMARY KEY (PoolID));""")
        self.__con.commit()
        
    def createRD(self):
        self.__cur.execute("""CREATE TABLE ResultData(DataID int NOT NULL,RecordID int NOT NULL,FilterID int,checkID int, date DATE, time DATETIME,PRIMARY KEY (DataID),FOREIGN KEY (RecordID) REFERENCES Main(RecordID),FOREIGN KEY (FilterID) REFERENCES Filters(FilterID),FOREIGN KEY (checkID) REFERENCES Checks(checkID));""")
        self.__con.commit()
    
    def pc_addto(self, data):
        pc = PoolCheck()
        self.pcID = pc.getNewID()
        pc.addto(data[0].slice(1))
        pc.close()
        
    def c_addto(self, data):
        c = Check()
        self.cID = c.getNewID()
        c.addto(data[1].slice(1))
        c.close()
    
    def f_addto(self, data):
        f = Filter()
        self.fID = f.getNewID
        f.addto(data[2].slice(1))
        f.close()
        
    def r_addto(self, data):
        r = Record(self.__UserID)
        self.rID = r.new_RecordID()
        r.addto()
        
    def addto(self, data):
        self.c_addto(data)
        self.pc_addto(data)
        self.f_addto(data)
        self.r_addto()
        
        rd = ResultData()
        rd.addto(self.pcID, self.fID, self.rID, self.cID)