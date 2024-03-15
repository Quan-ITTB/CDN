from register import Ui_registerWindow
from login import Ui_LoginWindow
from home import Ui_HomeWindow
from PyQt6.QtWidgets import *
import sys
import MySQLdb as mdb

class HomeWindow(QMainWindow, Ui_HomeWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
class LoginWindow(QMainWindow, Ui_LoginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnLogin.clicked.connect(self.clickHandler)
        self.btnRegister.clicked.connect(self.showRegisterWindow)
        
    def clickHandler(self):
        user = self.txtUsername.text()
        password = self.txtPassword.text()
        db = mdb.connect('localhost','root','','login_app')
        query = db.cursor()
        query.execute("select * from agent_list")
        kt = query.fetchone()
        if(kt):
            print("Login thành công!")
            self.hide()
            self.homeWindow = HomeWindow()
            self.homeWindow.show()
        else:
            print("Login thất bại!")
            
    def showRegisterWindow(self):
        self.hide()
        self.registerWindow = RegisterWindow()  
        self.registerWindow.show()     
          
class RegisterWindow(QMainWindow, Ui_registerWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnRegister.clicked.connect(self.clickHandler)
        
    def clickHandler(self):
        user = self.txtUsername.text()
        password = self.txtPassword.text()
        db = mdb.connect('localhost','root','','login_app')
        query = db.cursor()
        query.execute("select * from user_list where user='"+ user + "'")
        kt = query.fetchone()
        if(kt):
            QMessageBox.information(self,"Thất bại","Đã tồn tại!")
        else:
            sql = "INSERT INTO user_list (user, pass) VALUES (%s, %s)"
            val = (user, password)
            query.execute(sql, val)
            db.commit()
            QMessageBox.information(self,"Thành công","Đã thêm thành công!")
            self.hide()
            self.registerWindow = LoginWindow()  
            self.registerWindow.show()    

app = QApplication([])
Window = LoginWindow()
Window.show()
app.exec()

