import sqlite3
import time
import json
import random
import PoolCheck
import Record
import ResultData
import User
import Filter
import Check

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
    
    def pc_addto(self, data):
        pc = PoolCheck()
        self.pcID = pc.getNewID()
        pc.addto(data[0].slice(1))
        pc.close()
        
    def c_addto(self, data):
        c = Check()
        self.cID = pc.getNewID()
        c.addto(data[1].slice(1))
        c.close()
    
    def f_addto(self, data):
        f = Filter()
        self.fID = pc.getNewID
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