from  PyQt6 import QtCore,QtGui,QtWidgets,uic
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi

#from cdnmain import LoginWindow
import sys
import MySQLdb as mdb

class MenuT(QMainWindow):
    def __init__(self):
        super(MenuT, self).__init__()
        uic.loadUi('Menu.ui',self) 
        # code thoát chương trình   
        self.btn_exit.clicked.connect(QApplication.instance().exit)
       # self.btn_qlbh.clicked.connect(self.LoginWindow)  
        # code chuyển tab 
        # code tab bán hàng

    
app = QApplication (sys.argv) 
Widget = QtWidgets.QStackedWidget()
MenuT1 = MenuT() 
Widget.addWidget(MenuT1)  
Widget.setFixedHeight(600) 
Widget.setFixedWidth(800) 
Widget.show()
app.exec()