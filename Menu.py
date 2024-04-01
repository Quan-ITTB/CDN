# Form implementation generated from reading ui file 'Menu.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from  PyQt6 import QtCore,QtGui,QtWidgets,uic
from PyQt6.QtWidgets import *
from DSBH import Banhang
from nhanvien import Ui_AgentWindow
from DSHDN import Nhaphang
from BaoHanh import Baohanh
from PyQt6.uic import loadUi

import sys
import MySQLdb as mdb

# Code sử lý giao diện của File Menu.ui khi chuyển qua
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Home")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 10, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 70, 551, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btn_qlnv = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_qlnv.setGeometry(QtCore.QRect(30, 350, 141, 71))
        self.btn_qlnv.setObjectName("btn_qlnv")
        self.btn_qlbh = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_qlbh.setGeometry(QtCore.QRect(220, 350, 141, 71))
        self.btn_qlbh.setObjectName("btn_qlbh")
        self.btn_qlnh = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_qlnh.setGeometry(QtCore.QRect(410, 350, 141, 71))
        self.btn_qlnh.setObjectName("btn_qlnh")
        self.btn_qlbhanh = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_qlbhanh.setGeometry(QtCore.QRect(600, 350, 141, 71))
        self.btn_qlbhanh.setObjectName("btn_qlbhanh")
        self.btn_exit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(332, 467, 101, 41))
        self.btn_exit.setObjectName("btn_exit")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 130, 281, 191))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("logo.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Xin Chào "))
        self.label_2.setText(_translate("MainWindow", "Cửa Hàng Kinh Doanh Máy Tính An Phát"))
        self.btn_qlnv.setText(_translate("MainWindow", "Quản Lý Nhân Viên"))
        self.btn_qlbh.setText(_translate("MainWindow", "Quản Lý Bán Hàng"))
        self.btn_qlnh.setText(_translate("MainWindow", "Quản Lý Nhập Hàng"))
        self.btn_qlbhanh.setText(_translate("MainWindow", "Quản Lý Bảo Hành"))
        self.btn_exit.setText(_translate("MainWindow", "Thoát"))
# code sử lý sự kiện để hiện file menu

class MenuTong(QMainWindow,Ui_MainWindow ):
        def __init__(self):
                super().__init__()
                self.setupUi(self) 
        # code thoát chương trình 
                self.btn_exit.clicked.connect(QApplication.instance().exit)
        # xử lý sự kiện khi click vào DS Bán hàng trang đó sẽ hiện lên
                self.btn_qlbh.clicked.connect(self.show_DSBH) 
                self.btn_qlnv.clicked.connect(self.show_DSNV) 
        # xử lý sự kiện khi click vào DS Bán hàng trang đó sẽ hiện lên
                self.btn_qlnh.clicked.connect(self.show_DSNH)      
        # xử lý sự kiện khi click vào DS Bảo hành trang đó sẽ hiện lên
                self.btn_qlbhanh.clicked.connect(self.show_DSBaoHanh) 
                self.dsnv_window = NhanVien()
# code tab bán hàng
        def show_DSBH(self):
                # Tạo một instance của trang DSBH
                self.dsbh_window = Banhang()
                # Hiển thị trang DSBH
                self.dsbh_window.show()
                # self.dsbh_window.closeEvent.connect(self.show_Menu)   
        def show_Menu(self):
                self.show()
        def show_DSNV(self):
                if not self.dsnv_window.isVisible():  # Kiểm tra xem cửa sổ Home_Window đang không hiển thị
                        self.dsnv_window.show()     
        # code tab nhập hàng hàng
        def show_DSNH(self):
                # Tạo một instance của trang DSBH
                self.dsnh_window = Nhaphang()
                self.dsnh_window.show()
                # Hiển thị trang DSBH
                # code tab bảo hành 
        def show_DSBaoHanh(self):
                # Tạo một instance của trang DSBH
                self.dsbaohanh_window = Baohanh()
                # Hiển thị trang DSBH
                self.dsbaohanh_window.show()     
class NhanVien(QMainWindow, Ui_AgentWindow):
        def __init__(self):
                super().__init__()
                self.setupUi(self) 
                self.loaddata()
                self.WidgetDSNV.cellClicked.connect(self.click_cell)
                
        def loaddata(self):
                db= mdb.connect('localhost','root','','kinhdoanhmaytinh')
                query = db.cursor()
                query.execute("SELECT * FROM tblNhanvien")
                results = query.fetchall()
                self.WidgetDSNV.setRowCount(len(results))
                tablerow =0
                for row in results: 
                        self.WidgetDSNV.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
                        self.WidgetDSNV.setItem(tablerow, 1, QTableWidgetItem(str(row[1])))
                        self.WidgetDSNV.setItem(tablerow, 2, QTableWidgetItem(str(row[2])))
                        self.WidgetDSNV.setItem(tablerow, 3, QTableWidgetItem(str(row[3])))
                        self.WidgetDSNV.setItem(tablerow, 4, QTableWidgetItem(str(row[4])))
                        self.WidgetDSNV.setItem(tablerow, 5, QTableWidgetItem(str(row[5])))
                        self.WidgetDSNV.setItem(tablerow, 6, QTableWidgetItem(str(row[6])))
                        self.WidgetDSNV.setItem(tablerow, 7, QTableWidgetItem(str(row[7])))
                        self.WidgetDSNV.setItem(tablerow, 8, QTableWidgetItem(str(row[8])))
                        tablerow += 1
        def click_cell(self, row, column):
                db= mdb.connect('localhost','root','','kinhdoanhmaytinh')
                query = db.cursor()
                query.execute("SELECT * FROM tblNhanvien")
                results = query.fetchall()
                self.WidgetDSNV.setRowCount(len(results))
                self.txt_ma.setText(self.WidgetDSNV.item(row, 0).text())
                self.txt_ten.setText(self.WidgetDSNV.item(row, 1).text())
                self.txt_sdt.setText(self.WidgetDSNV.item(row, 5).text())
                # self.txt_ngaysinh.setDate(self.WidgetDSNV.item(row, 2).text())
                if str(self.WidgetDSNV.item(row, 3).text()) == "Nam" :
                        self.rb_nam.isChecked = True
                        self.rb_nu.isChecked = False
                else:
                        self.rb_nu.isChecked = True
                        self.rb_nam.isChecked = False
                self.txt_hsl.setText(self.WidgetDSNV.item(row, 6).text())
                self.txt_luong.setText(self.WidgetDSNV.item(row, 7).text())
                # self.txt_ngayvaolam.setText(self.WidgetDSNV.item(row, 8).text())
app = QApplication (sys.argv) 
Widget = QtWidgets.QStackedWidget()
MenuT1 = MenuTong() 
Widget.addWidget(MenuT1)  
Widget.setFixedHeight(600) 
Widget.setFixedWidth(800) 
Widget.show()
app.exec()

#test