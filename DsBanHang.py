# Form implementation generated from reading ui file 'PhieuBaoHanh.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

# Khởi tạo trang lập phiếu bảo hành 
from PyQt6 import QtCore, QtGui, QtWidgets 
import sys
from  PyQt6 import QtCore,QtGui,QtWidgets,uic
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(725, 487)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 10, 391, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.hoadobanhang = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.hoadobanhang.setGeometry(QtCore.QRect(0, 90, 701, 501))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.hoadobanhang.setFont(font)
        self.hoadobanhang.setObjectName("hoadobanhang")
        self.label_2 = QtWidgets.QLabel(parent=self.hoadobanhang)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.mahd = QtWidgets.QLineEdit(parent=self.hoadobanhang)
        self.mahd.setGeometry(QtCore.QRect(130, 30, 113, 20))
        self.mahd.setObjectName("mahd")
        self.label_3 = QtWidgets.QLabel(parent=self.hoadobanhang)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.masp = QtWidgets.QLineEdit(parent=self.hoadobanhang)
        self.masp.setGeometry(QtCore.QRect(130, 60, 113, 20))
        self.masp.setObjectName("masp")
        self.tensp = QtWidgets.QLineEdit(parent=self.hoadobanhang)
        self.tensp.setGeometry(QtCore.QRect(130, 90, 113, 20))
        self.tensp.setText("")
        self.tensp.setObjectName("tensp")
        self.label_4 = QtWidgets.QLabel(parent=self.hoadobanhang)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.dongia = QtWidgets.QLineEdit(parent=self.hoadobanhang)
        self.dongia.setGeometry(QtCore.QRect(400, 60, 113, 20))
        self.dongia.setObjectName("dongia")
        self.label_6 = QtWidgets.QLabel(parent=self.hoadobanhang)
        self.label_6.setGeometry(QtCore.QRect(280, 60, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.tongtien = QtWidgets.QLineEdit(parent=self.hoadobanhang)
        self.tongtien.setGeometry(QtCore.QRect(400, 90, 113, 20))
        self.tongtien.setObjectName("tongtien")
        self.label_7 = QtWidgets.QLabel(parent=self.hoadobanhang)
        self.label_7.setGeometry(QtCore.QRect(280, 90, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.sua = QtWidgets.QPushButton(parent=self.hoadobanhang)
        self.sua.setGeometry(QtCore.QRect(570, 40, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.sua.setFont(font)
        self.sua.setObjectName("sua")
        self.them = QtWidgets.QPushButton(parent=self.hoadobanhang)
        self.them.setGeometry(QtCore.QRect(570, 80, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.them.setFont(font)
        self.them.setObjectName("them")
        self.xoa = QtWidgets.QPushButton(parent=self.hoadobanhang)
        self.xoa.setGeometry(QtCore.QRect(570, 120, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.xoa.setFont(font)
        self.xoa.setObjectName("xoa")
        self.exit = QtWidgets.QPushButton(parent=self.hoadobanhang)
        self.exit.setGeometry(QtCore.QRect(570, 150, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")
        self.listView = QtWidgets.QListView(parent=self.hoadobanhang)
        self.listView.setGeometry(QtCore.QRect(20, 200, 641, 291))
        self.listView.setObjectName("listView")
        self.label_8 = QtWidgets.QLabel(parent=self.hoadobanhang)
        self.label_8.setGeometry(QtCore.QRect(280, 120, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.dateEdit = QtWidgets.QDateEdit(parent=self.hoadobanhang)
        self.dateEdit.setGeometry(QtCore.QRect(400, 120, 110, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.label_9 = QtWidgets.QLabel(parent=self.hoadobanhang)
        self.label_9.setGeometry(QtCore.QRect(280, 150, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.tongtien_2 = QtWidgets.QLineEdit(parent=self.hoadobanhang)
        self.tongtien_2.setGeometry(QtCore.QRect(400, 150, 113, 20))
        self.tongtien_2.setObjectName("tongtien_2")
        self.label_10 = QtWidgets.QLabel(parent=self.hoadobanhang)
        self.label_10.setGeometry(QtCore.QRect(20, 120, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.soluong_2 = QtWidgets.QLineEdit(parent=self.hoadobanhang)
        self.soluong_2.setGeometry(QtCore.QRect(130, 120, 113, 20))
        self.soluong_2.setObjectName("soluong_2")
        self.label_11 = QtWidgets.QLabel(parent=self.hoadobanhang)
        self.label_11.setGeometry(QtCore.QRect(20, 150, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.soluong_3 = QtWidgets.QLineEdit(parent=self.hoadobanhang)
        self.soluong_3.setGeometry(QtCore.QRect(130, 150, 113, 20))
        self.soluong_3.setObjectName("soluong_3")
        self.label_12 = QtWidgets.QLabel(parent=self.hoadobanhang)
        self.label_12.setGeometry(QtCore.QRect(280, 30, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.dongia_2 = QtWidgets.QLineEdit(parent=self.hoadobanhang)
        self.dongia_2.setGeometry(QtCore.QRect(400, 30, 113, 20))
        self.dongia_2.setObjectName("dongia_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 725, 22))
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
        self.label.setText(_translate("MainWindow", "Quản Lý Bảo Hành Sản Phẩm"))
        self.hoadobanhang.setTitle(_translate("MainWindow", "Phiếu bảo hành"))
        self.label_2.setText(_translate("MainWindow", "Mã Phiếu"))
        self.label_3.setText(_translate("MainWindow", "Mã sản phẩm"))
        self.label_4.setText(_translate("MainWindow", "Tên sản phẩm"))
        self.label_6.setText(_translate("MainWindow", "Tình trạng lỗi"))
        self.label_7.setText(_translate("MainWindow", "Thời gian BH"))
        self.sua.setText(_translate("MainWindow", "Sửa"))
        self.them.setText(_translate("MainWindow", "Thêm mới"))
        self.xoa.setText(_translate("MainWindow", "Loại Bỏ"))
        self.exit.setText(_translate("MainWindow", "Thoát"))
        self.label_8.setText(_translate("MainWindow", "Ngày yêu cầu"))
        self.label_9.setText(_translate("MainWindow", "Nhân viên lập"))
        self.label_10.setText(_translate("MainWindow", "Tên KH"))
        self.label_11.setText(_translate("MainWindow", "SDT KH"))
        self.label_12.setText(_translate("MainWindow", "Số lượng"))
app = QApplication (sys.argv) 
Widget = QtWidgets.QStackedWidget()
phieubh = Ui_MainWindow() 
Widget.addWidget(phieubh)  
#Widget.setFixedHeight(500)
#Widget.setFixedWidth(800)
Widget.show()
app.exec()
