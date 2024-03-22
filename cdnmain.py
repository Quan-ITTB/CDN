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
        query = db.cursor()
        try:
            user_name = self.txtUsername.text()
            password = self.txtPassword.text()
            query.callproc("prCheck_Login", (user_name, password))

            results = query.fetchone()
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
            query.close()
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
    def checkUserExists(self, username):
        try:
            # Kết nối đến cơ sở dữ liệu MySQL
            db= mdb.connect('localhost','root','','cdn_btl')
            query = db.cursor()


            # Kiểm tra xem tên người dùng đã tồn tại trong cơ sở dữ liệu hay chưa
            query.execute("SELECT COUNT(*) FROM tbl_user WHERE sUserName = %s", (username,))
            count = query.fetchone()[0]

            # Đóng kết nối
            query.close()
            db.close()

            return count > 0

        except mdb.connector.Error as err:
            print(f"Lỗi MySQL: {err}")
            return False
  
    def clickHandler(self):
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        if self.checkUserExists(username):
            QMessageBox.warning(self, "Lỗi", "Tài khoản đã tồn tại!")
        else:
            try:
                # Kết nối đến cơ sở dữ liệu MySQL
                db= mdb.connect('localhost','root','','cdn_btl')
                query = db.cursor()

            # Gọi stored procedure để thêm người dùng
                query.callproc("sp_AddUser", (username, password))
                db.commit()

            # Hiển thị thông báo thành công
                QMessageBox.information(self, "Thành công", "Đã đăng ký tài khoản thành công!")

            # Đóng kết nối
                query.close()
                db.close()

            except mdb.connector.Error as err:
                print(f"Lỗi MySQL: {err}")
                QMessageBox.critical(self, "Lỗi", "Đã xảy ra lỗi khi thực thi.")
        
app = QApplication([])
Window = LoginWindow()
Window.show()
app.exec()

