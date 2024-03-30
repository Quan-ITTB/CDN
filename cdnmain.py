from register import Ui_registerWindow
from login import Ui_LoginWindow
from home import Ui_HomeWindow
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from newmain import Ui_Home_Window
import sys
import MySQLdb as mdb
from DSBH import Banhang

data = "test"

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
        self.login_signal = Communicate()
        self.register_signal = Communicate()
        self.btnLoginHome.clicked.connect(self.emitLogin)
        self.btnRegisterHome.clicked.connect(self.emitRegister)
    def emitLogin(self):
        print("emit login")
        self.login_signal.dataChanged.emit("Home -> Login")
        self.hide()
    def emitRegister(self):
        print("emit Register")
        self.login_signal.dataChanged.emit("Home -> Register")
        self.hide()
        self.communicate.dataChanged.connect(self.receiveData)   
    def receiveData(self, data):
        print(f"Đã chạy vào receive 1 : ${data}")
        self.show() 
    def receiveData2(self, data):
        print(f"Đã chạy vào receive 2 : ${data}")
        self.show()

   
        self.label.setText(data)
   
class LoginWindow(QMainWindow, Ui_LoginWindow):
    def __init__(self, user = ""):
        super().__init__()
        self.setupUi(self)
        self.txtUsername.setText(user)
        
        self.login_success_signal = Communicate()
        self.hide()
        self.homeWindow = HomeWindow()
        self.homeWindow.show()
        self.btnLogin.clicked.connect(self.clickHandler)
        self.btnRegister.clicked.connect(self.showRegisterWindow)
    def receiveData(self, data):
        self.txtUsername.setText(data)
        print(f"Đã chạy vào receive  : ${data}")
        self.show()        
    def receiveData2(self, data):
        self.show()
        self.txtUsername.setText(data)
        print(f"Đã chạy vào receive 2 : ${data}")
        

    def clickHandler(self):
        db = mdb.connect('localhost','root','','cdn_btl')
        db = mdb.connect('localhost','root','','cdn_btl')
        query = db.cursor()
        try:
            user_name = self.txtUsername.text()
            password = self.txtPassword.text()
            query.callproc("prCheck_Login", (user_name, password))

            results = query.fetchone()
            if(results):
                print("emit Login -> Home")
                self.login_success_signal.dataChanged.emit("Login Success!")
                self.hide()
                # self.homeWindow.show()
            else:
                print("Login thất bại!")
                # global data 
                data = "Thất bại"
                # self.homeWindow = HomeWindow()
                # self.homeWindow.show()
                # self.homeWindow.label.setText(data)

        except mdb.Error as e:
            print("Error:", e)

        finally:
            # Đóng kết nối
            query.close()
            db.close()
        
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
        self.register_success_signal = Communicate()
        self.btnRegister.clicked.connect(self.clickHandler)  
    def receiveData(self, data):
        print(f"Đã chạy vào receive 1 : ${data}")
        self.show() 
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

        except mdb.Error as err:
            print(f"Lỗi MySQL: {err}")
            return False
  
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

        except mdb.Error as err:
            print(f"Lỗi MySQL: {err}")
            return False
  
    def clickHandler(self):
        username = self.txtUsername.text()
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        if self.checkUserExists(username):
            QMessageBox.warning(self, "Lỗi", "Tài khoản đã tồn tại!")
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
                self.register_success_signal.dataChanged.emit("Register -> Home")
                
            # Đóng kết nối
                query.close()
                db.close()

            except mdb.Error as err:
                print(f"Lỗi MySQL: {err}")
                QMessageBox.critical(self, "Lỗi", "Đã xảy ra lỗi khi thực thi.")
            try:
                # Kết nối đến cơ sở dữ liệu MySQL
                db= mdb.connect('localhost','root','','cdn_btl')
                query = db.cursor()

            # Gọi stored procedure để thêm người dùng
                query.callproc("sp_AddUser", (username, password))
                db.commit()

            # Hiển thị thông báo thành công
                QMessageBox.information(self, "Thành công", "Đã đăng ký tài khoản thành công!")
                self.loginWindow = LoginWindow(user=username)
                self.loginWindow.show()
            # Đóng kết nối
                query.close()
                db.close()

            except mdb.Error as err:
                print(f"Lỗi MySQL: {err}")
                QMessageBox.critical(self, "Lỗi", "Đã xảy ra lỗi khi thực thi.")
class MenuWindow(QMainWindow, Ui_Home_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
app = QApplication([])
login_window = LoginWindow()
menu_window = MenuWindow()
register_window = RegisterWindow()
home_window = HomeWindow()
login_window.login_success_signal.dataChanged.connect(home_window.receiveData)
register_window.register_success_signal.dataChanged.connect(login_window.receiveData2)

home_window.login_signal.dataChanged.connect(login_window.show)
home_window.register_signal.dataChanged.connect(register_window.receiveData)
menu_window.show()
app.exec()

