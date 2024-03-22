from register import Ui_registerWindow
from login import Ui_LoginWindow
from home import Ui_HomeWindow
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

import sys
import MySQLdb as mdb

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
        self.cmt = Communicate()
        self.txtUsername.setText(user)
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
                self.hide()
                self.homeWindow = HomeWindow()
                self.cmt.dataChanged.emit(password)
                self.homeWindow.show()
            else:
                print("Login thất bại!")
                self.cmt._data = "thất bại"       


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

        db = mdb.connect('localhost','root','','cdn_btl')
        cursor = db.cursor()

        try:
            # Kiểm tra xem tài khoản đã tồn tại chưa
            cursor.execute("SELECT COUNT(*) FROM tbl_user WHERE username = %s", (user,))
            count = cursor.fetchone()[0]

            if count > 0:
                QMessageBox.warning(self, "Lỗi", "Tài khoản đã tồn tại!")
            else:
                # Thực thi stored procedure để đăng ký user
                cursor.callproc("sp_AddUser", (user, password))

                # Lấy kết quả trả về từ stored procedure
                cursor.execute("SELECT sp_AddUser")  # Thay đổi tên procedure tùy theo tên bạn đã đặt
                result = cursor.fetchone()[0]

                # Kiểm tra kết quả và hiển thị thông báo
                if result == 1:
                    QMessageBox.information(self, "Thành công", "Đăng ký thành công!")
                    self.hide()
                    self.loginWindow = LoginWindow(user)  # Chuyển user name sang cửa sổ đăng nhập
                    self.loginWindow.show()
                else:
                    QMessageBox.warning(self, "Thất bại", "Đăng ký thất bại!")

        except mdb.connector.Error as err:
            print(f"Lỗi MySQL: {err}")
            QMessageBox.critical(self, "Lỗi", "Đã xảy ra lỗi khi thực thi.")

        finally:
            cursor.close()
            db.close()
        
app = QApplication([])
Window = LoginWindow()
Window.show()
app.exec()

