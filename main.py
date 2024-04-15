import os
import sqlite3
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition    
from User import login
from PoolCheck import PoolCheck
from ResultData import ResultData
from Record import Record

class MainWindow(Screen):
    def test(self):
        print("test")

class LoginWindow(Screen):
    
    def loginattempt(self):
        username = self.ids.username.text.lower()
        password = self.ids.password.text
        email = self.ids.email.text.lower()
        user = login()
        user.userLogin(username, password, email)
        if user.userLogin(username, password, email):
            with open("temp/id.txt", "w") as f:
                f.write(str(user.userLogin(username, password, email)))
            self.manager.current = 'basicmenu'
        else:
            self.ids.username.text = ""
            self.ids.password.text = ""
            self.ids.email.text = ""
        user.close()

class SignWindow(Screen):
    def signup(self):
        username = self.ids.username.text.lower()
        password = self.ids.password.text
        email = self.ids.email.text.lower()
        user = login()
        if not user.validateemail(email):
            self.resetfields()
            if not user.validatepswd(password):
                self.resetfields() 
        else:
            self.ids.email_label.text = "Email: "
            self.ids.pass_label.text = "Password: "
            user.addto(username, email, password)
            self.manager.current = 'loginwindow'
        user.close()
    
    def resetfields(self):
        self.ids.password.text = ""
        self.ids.email.text = ""
        return 0

class BasicMenu(Screen):

    def on_enter(self):
        with open("temp\\id.txt", "r") as f:    
            self.userID = f.read()
        os.remove("temp\\id.txt")
        user = login()
        self.ids.username.text = "Hello " + user.UsernamegetByUserID(self.userID).capitalize()

    def on_pre_leave(self):
        with open("temp\\id.txt", "w") as f:    
            f.write(self.userID)      

class Record_menu(Screen):    
    def on_enter(self):
        with open("temp\\id.txt", "r") as f:    
            self.userID = f.read()        
        os.remove("temp\\id.txt")

    def on_pre_leave(self):
        with open("temp\\id.txt", "w") as f:    
            f.write(self.userID)

class Recording(Screen):
    def get_cats(self):
        self.__con = sqlite3.connect("databases\Main.db")
        self.__cur = self.__con.cursor()
        self.categories = []
        self.variables = []
        temp = []# for vars
        cat_temp = [] # for cats
        subtract_varlen = 0
        i = "table"
        data = self.__cur.execute(f"SELECT name from sqlite_master WHERE type='{i}';")
        for i in data.fetchall():
            banlist = ["Record", "ResultData", "User"]
            if i[0] not in banlist:
                cat_temp.append(i[0])
                data = self.__cur.execute(f"SELECT * from {i[0]};")
                
                for column in data.description:
                    if "ID" not in column[0]:
                        temp.append(column[0])
                    else: 
                        subtract_varlen += 1
                self.variables.append(temp)
                self.categories.append([i, len(temp) - subtract_varlen])
                subtract_varlen = 0
                temp = []
        print(self.variables)
        print(self.categories)
        
    def on_enter(self):
        self.get_cats()
        self.cat_txt = ""
        self.var_txt = ""
        self.catindex = 0
        self.cur_cat = ""
        self.varindex = 0
        self.cur_var = ""
        self.results = []
        self.update_text()
        with open("temp\\id.txt", "r") as f:    
            self.userID = f.read()        
        os.remove("temp\\id.txt")
    
    def check_int(self):
        userinput = self.ids.userinput.text
        if userinput.isnumeric():
            return True
        else:
            return False
    
    def check_limits(self):
        pass
    
    def recordbutton(self):
        results.append([self.cur_cat, self.cur_var, self.ids.userinput.text])
    
    def gonext(self):
        self.recordbutton()
        if self.varindex < self.categories[self.catindex][1]:
            self.varindex += 1
            self.update_text()
        elif self.varindex == self.categories[self.catindex][1]:
            self.varindex = 0
            self.catindex += 1
            self.update_text()
        else:
            #if catindex is not at the end of its list
            if self.catindex < len(self.categories[0]):
                self.catindex += 1
                self.varindex = 0
                self.update_text()
            if self.catindex == len(self.categories[0]):
                self.varindex += 1
                self.update_text()
            else:
                self.results()
                #code to go results page
    
    def skip(self):
        self.ids.userinput.text = 0
        self.gonext()
    
    def update_text(self):
        self.cur_cat = self.categories[self.catindex]
        self.cur_var = self.variables[self.catindex][self.varindex]
        print(self.cur_cat)
        print(self.cur_var)
        self.ids.variabletext.text = self.cur_var
        self.ids.categorytext.text = self.cur_cat[0][0]

    def on_pre_leave(self):
        with open("temp\\id.txt", "w") as f:
            f.write(self.userID)

class Recording_p(Screen):
    pass    

class BasicMenu_View(Screen):
    pass

class InputMenu(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("main.kv")

class MainApp(App):
    def build(Self):
        return kv

if __name__=="__main__":
    MainApp().run()