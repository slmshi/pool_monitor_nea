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
        username = self.ids.username.text
        password = self.ids.password.text
        email = self.ids.email.text
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
        username = self.ids.username.text
        password = self.ids.password.text
        email = self.ids.email.text
        user = login()
        if not user.validateemail(email):
            self.ids.email_label.text = "Incorrect Email, Try again:"
            self.resetfields()
            if not user.validatepswd(password):
                self.ids.pass_label.text = "Password not met requirements, Try again:"
                self.resetfields() 
        else:
            self.ids.email_label.text = "Email: "
            self.ids.pass_label.text = "Password: "
            user.addto(username, email, password)
            self.manager.current = 'loginwindow'
    
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
        self.ids.username.text = "Hello" + user.UsernamegetByUserID(self.userID)

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
    def get_variables(self):
        self.__con = sqlite3.connect("databases\Main.db")
        self.__cur = self.__con.cursor()
        self.__cur.execute("SELECT name from sqlite_master WHERE type='table';")
        for i in self.__cur.fetchall():
            self.categories.append(i[0])
        return self.get_varslength()

    def on_enter(self):
        self.categories = []
        self.variables = self.get_all()
        self.cat_txt = ""
        self.var_txt = ""
        self.catindex = 0
        self.cur_cat = ""
        self.varindex = 0
        self.cur_var = ""
        with open("temp\\id.txt", "r") as f:    
            self.userID = f.read()        
        os.remove("temp\\id.txt")
    
    def get_varslength(self):
        data=self.__cur.execute(f'''SELECT * FROM {self.categories[self.catindex]}''')
        return len(data.description)
    
    def gonext(self):
        if self.varindex < len(self.get_varslength):
            self.varindex += 1
        else:
            #if catindex is at the end of its list
            if self.catindex < len(self.categories):
                self.catindex += 1
                self.varindex = 0
                
            #if end of category and var indexes - go results
            else:
                pass 
                #enter code to go results page
                
    def button_press(self):
        pass
    
    def update_text(self):
        self.cur_cat = self.categories[self.catindex]
        self.cur_var = self.variables[self.varindex]

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