from register import Ui_registerWindow
from login import Ui_LoginWindow
from home import Ui_HomeWindow
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

import sys
import MySQLdb as mdb


data = "test"
class Communicate(QObject):
    dataChanged = pyqtSignal(str)  
    def __init__(self):
        super().__init__()
        self._data = ""
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, value):
        self._data = value
        self.dataChanged.emit(value)
    
class HomeWindow(QMainWindow, Ui_HomeWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.communicate = Communicate()
        self.communicate.dataChanged.connect(self.receiveData)   
    def receiveData(self, data):
        self.label.setText(data)
   
class LoginWindow(QMainWindow, Ui_LoginWindow):
    def __init__(self, user = ""):
        super().__init__()
        self.setupUi(self)
        self.txtUsername.setText(user)
        self.hide()
        self.homeWindow = HomeWindow()
        self.homeWindow.show()
        self.btnLogin.clicked.connect(self.clickHandler)
        self.btnRegister.clicked.connect(self.showRegisterWindow)

    def clickHandler(self):
        db = mdb.connect('localhost','root','','cdn_btl')
        cursor = db.cursor()
        try:
            user_name = self.txtUsername.text()
            password = self.txtPassword.text()
            cursor.callproc("prCheck_Login", (user_name, password))
            results = cursor.fetchone()
            if(results):
                # self.hide()
                # self.homeWindow = HomeWindow()
                self.homeWindow.communicate.dataChanged.emit(user_name)
                # self.homeWindow.show()
            else:
                print("Login thất bại!")
                global data 
                data = "Thất bại"
                # self.homeWindow = HomeWindow()
                # self.homeWindow.show()
                self.homeWindow.label.setText(data)

        except mdb.Error as e:
            print("Error:", e)

        finally:
            # Đóng kết nối
            cursor.close()
            db.close()
        

    def showRegisterWindow(self):
        self.hide()
        self.registerWindow = RegisterWindow()  
        self.registerWindow.show()     

          
class RegisterWindow(QMainWindow, Ui_registerWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnRegister.clicked.connect(self.clickHandler)
    
    def test(self,user):
        print(f"data là: {user}")    
        
    def clickHandler(self):
        user = self.txtUsername.text()
        password = self.txtPassword.text()
        self.user = user
        db = mdb.connect('localhost','root','','cdn_btl')
        cursor = db.cursor()
        cursor.callproc("prCheckAndInsertUser", (user,password))
        results = cursor.fetchone()
        print(user + password)
        print(results)
        if(1 in results):
            QMessageBox.information(self,"Thành công","Thành công")
            self.hide()
            self.registerWindow = LoginWindow(self.user)  
            self.registerWindow.show()    
        else:
            QMessageBox.information(self,"Thất bại","Thất bại")
        
app = QApplication([])
Window = LoginWindow()
Window.show()
app.exec()

