# Form implementation generated from reading ui file 'SDBH.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from  PyQt6 import QtCore,QtGui,QtWidgets,uic
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
import sys
import MySQLdb as mdb
#import pymysql
# code sử lý giao diện .UI
class DSBH(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1230, 878)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.hoadobanhang_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.hoadobanhang_2.setGeometry(QtCore.QRect(40, 60, 1121, 401))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.hoadobanhang_2.setFont(font)
        self.hoadobanhang_2.setObjectName("hoadobanhang_2")
        self.WidgetDSBH = QtWidgets.QTableWidget(parent=self.hoadobanhang_2)
        self.WidgetDSBH.setGeometry(QtCore.QRect(10, 30, 691, 351))
        self.WidgetDSBH.setColumnCount(7)
        self.WidgetDSBH.setObjectName("WidgetDSBH")
        self.WidgetDSBH.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.WidgetDSBH.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.WidgetDSBH.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.WidgetDSBH.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.WidgetDSBH.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.WidgetDSBH.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.WidgetDSBH.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.WidgetDSBH.setHorizontalHeaderItem(6, item)
        self.WidgetDSBH.horizontalHeader().setDefaultSectionSize(98)
        self.WidgetDSBH.horizontalHeader().setMinimumSectionSize(48)
        self.groupBox = QtWidgets.QGroupBox(parent=self.hoadobanhang_2)
        self.groupBox.setGeometry(QtCore.QRect(720, 20, 391, 371))
        self.groupBox.setObjectName("groupBox")
        self.btnSua_2 = QtWidgets.QPushButton(parent=self.groupBox)
        self.btnSua_2.setGeometry(QtCore.QRect(150, 200, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnSua_2.setFont(font)
        self.btnSua_2.setObjectName("btnSua_2")
        self.btnthem_2 = QtWidgets.QPushButton(parent=self.groupBox)
        self.btnthem_2.setGeometry(QtCore.QRect(30, 200, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnthem_2.setFont(font)
        self.btnthem_2.setObjectName("btnthem_2")
        self.btnxoa_2 = QtWidgets.QPushButton(parent=self.groupBox)
        self.btnxoa_2.setGeometry(QtCore.QRect(270, 200, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnxoa_2.setFont(font)
        self.btnxoa_2.setObjectName("btnxoa_2")
        self.btnbackMN_2 = QtWidgets.QPushButton(parent=self.groupBox)
        self.btnbackMN_2.setGeometry(QtCore.QRect(130, 290, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnbackMN_2.setFont(font)
        self.btnbackMN_2.setObjectName("btnbackMN_2")
        self.txtMaNV_1 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtMaNV_1.setGeometry(QtCore.QRect(162, 60, 211, 20))
        self.txtMaNV_1.setText("")
        self.txtMaNV_1.setObjectName("txtMaNV_1")
        self.txtNgayLap_1 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtNgayLap_1.setGeometry(QtCore.QRect(160, 90, 211, 20))
        self.txtNgayLap_1.setObjectName("txtNgayLap_1")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(30, 60, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_13 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(30, 90, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.txtMaHD_1 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtMaHD_1.setGeometry(QtCore.QRect(162, 30, 211, 20))
        self.txtMaHD_1.setObjectName("txtMaHD_1")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(30, 30, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(30, 120, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.txtTenKhach_1 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtTenKhach_1.setGeometry(QtCore.QRect(160, 120, 211, 20))
        self.txtTenKhach_1.setText("")
        self.txtTenKhach_1.setObjectName("txtTenKhach_1")
        self.label_15 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(30, 150, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.txtHTTT = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtHTTT.setGeometry(QtCore.QRect(160, 150, 211, 20))
        self.txtHTTT.setObjectName("txtHTTT")
        self.hoadobanhang_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.hoadobanhang_3.setGeometry(QtCore.QRect(40, 470, 1111, 291))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.hoadobanhang_3.setFont(font)
        self.hoadobanhang_3.setObjectName("hoadobanhang_3")
        self.WidgetDSBHCT = QtWidgets.QTableWidget(parent=self.hoadobanhang_3)
        self.WidgetDSBHCT.setGeometry(QtCore.QRect(10, 30, 681, 251))
        self.WidgetDSBHCT.setColumnCount(4)
        self.WidgetDSBHCT.setObjectName("WidgetDSBHCT")
        self.WidgetDSBHCT.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.WidgetDSBHCT.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.WidgetDSBHCT.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.WidgetDSBHCT.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.WidgetDSBHCT.setHorizontalHeaderItem(3, item)
        self.WidgetDSBHCT.horizontalHeader().setDefaultSectionSize(122)
        self.WidgetDSBHCT.horizontalHeader().setMinimumSectionSize(48)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.hoadobanhang_3)
        self.groupBox_2.setGeometry(QtCore.QRect(710, 20, 391, 261))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btnSua_3 = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.btnSua_3.setGeometry(QtCore.QRect(150, 200, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnSua_3.setFont(font)
        self.btnSua_3.setObjectName("btnSua_3")
        self.btnthem_3 = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.btnthem_3.setGeometry(QtCore.QRect(30, 200, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnthem_3.setFont(font)
        self.btnthem_3.setObjectName("btnthem_3")
        self.btnxoa_3 = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.btnxoa_3.setGeometry(QtCore.QRect(270, 200, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnxoa_3.setFont(font)
        self.btnxoa_3.setObjectName("btnxoa_3")
        self.txtMaSP_2 = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtMaSP_2.setGeometry(QtCore.QRect(162, 60, 211, 20))
        self.txtMaSP_2.setText("")
        self.txtMaSP_2.setObjectName("txtMaSP_2")
        self.txtSL = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtSL.setGeometry(QtCore.QRect(160, 90, 211, 20))
        self.txtSL.setObjectName("txtSL")
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(30, 60, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_16 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_16.setGeometry(QtCore.QRect(30, 90, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.txtMaHD_2 = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtMaHD_2.setGeometry(QtCore.QRect(162, 30, 211, 20))
        self.txtMaHD_2.setObjectName("txtMaHD_2")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(30, 30, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_17 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_17.setGeometry(QtCore.QRect(30, 120, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.txDonGia = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txDonGia.setGeometry(QtCore.QRect(160, 120, 211, 20))
        self.txDonGia.setText("")
        self.txDonGia.setObjectName("txDonGia")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 20, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1230, 26))
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
        self.hoadobanhang_2.setTitle(_translate("MainWindow", "Danh Sách Hóa Đơn"))
        item = self.WidgetDSBH.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mã Hóa Đơn"))
        item = self.WidgetDSBH.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Mã Nhân Viên"))
        item = self.WidgetDSBH.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ngày Lập"))
        item = self.WidgetDSBH.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "SĐT Khách"))
        item = self.WidgetDSBH.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Hình Thức Thanh Toán"))
        item = self.WidgetDSBH.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Tổng Tiền"))
        self.groupBox.setTitle(_translate("MainWindow", "Thao Tác"))
        self.btnSua_2.setText(_translate("MainWindow", "Sửa"))
        self.btnthem_2.setText(_translate("MainWindow", "Thêm mới"))
        self.btnxoa_2.setText(_translate("MainWindow", "Loại Bỏ"))
        self.btnbackMN_2.setText(_translate("MainWindow", "Thoát"))
        self.label_7.setText(_translate("MainWindow", "Mã Nhân Viên"))
        self.label_13.setText(_translate("MainWindow", "Ngày Lập"))
        self.label_5.setText(_translate("MainWindow", "Mã Hóa Đơn"))
        self.label_6.setText(_translate("MainWindow", "SDT Khách Hàng"))
        self.label_15.setText(_translate("MainWindow", "HT thanh toán"))
        self.hoadobanhang_3.setTitle(_translate("MainWindow", "Danh Sách Hóa Đơn Chi Tiết"))
        item = self.WidgetDSBHCT.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mã Hóa Đơn"))
        item = self.WidgetDSBHCT.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Mã Sản Phẩm"))
        item = self.WidgetDSBHCT.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Số Lượng"))
        item = self.WidgetDSBHCT.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Đơn Giá"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Thao Tác"))
        self.btnSua_3.setText(_translate("MainWindow", "Sửa"))
        self.btnthem_3.setText(_translate("MainWindow", "Thêm mới"))
        self.btnxoa_3.setText(_translate("MainWindow", "Loại Bỏ"))
        self.label_11.setText(_translate("MainWindow", "Mã Mã Sản Phẩm"))
        self.label_16.setText(_translate("MainWindow", "Số Lượng "))
        self.label_12.setText(_translate("MainWindow", "Mã Hóa Đơn"))
        self.label_17.setText(_translate("MainWindow", "Đơn Giá"))
        self.label.setText(_translate("MainWindow", "Quản Lý Bán Hàng"))
# code sử lý sự kiện .Py
class Banhang(QMainWindow, DSBH):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.loaddata()
        self.loaddata1()
        self.btnbackMN_2.clicked.connect(self.handle_exit)
        self.WidgetDSBH.cellClicked.connect(self.show_selected_data)
        self.WidgetDSBHCT.cellClicked.connect(self.show_selected_data_ct)
        self.btnbackMN_2.clicked.connect(QApplication.instance().exit)
        self.btnthem_3.clicked.connect(self.insert_data)
# code sử lý load data lên trang DSBH
    def loaddata(self):
        db= mdb.connect('localhost','root','','kinhdoanhmaytinh')
        query = db.cursor()
        query.execute("SELECT * FROM tblhdxuat")
        results = query.fetchall()
        #self.tableWidget.setRowCount(len(results))
        self.WidgetDSBH.setRowCount(len(results))
        tablerow =0
        for row in results: 
           self.WidgetDSBH.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
           self.WidgetDSBH.setItem(tablerow, 1, QTableWidgetItem(str(row[1])))
           self.WidgetDSBH.setItem(tablerow, 2, QTableWidgetItem(str(row[2])))
           self.WidgetDSBH.setItem(tablerow, 3, QTableWidgetItem(str(row[3])))
           self.WidgetDSBH.setItem(tablerow, 4, QTableWidgetItem(str(row[4])))
           self.WidgetDSBH.setItem(tablerow, 5, QTableWidgetItem(str(row[5])))
           #fself.WidgetDSBH.setItem(tablerow, 6, QTableWidgetItem(str(row[6])))
           #self.tableWidget.setItem(tablerow, 7, QTableWidgetItem(str(row[7])))
           #self.tableWidget.setItem(tablerow, 8, QTableWidgetItem(str(row[8])))
           #self.tableWidget.setItem(tablerow, 9, QTableWidgetItem(str(row[9])))
           tablerow += 1
# code sử lý load data lên trang DSBH chi tiết
    def loaddata1(self):
        db= mdb.connect('localhost','root','','kinhdoanhmaytinh')
        query = db.cursor()
        query.execute("SELECT * FROM tblctxuat")
        results = query.fetchall()
        #self.tableWidget.setRowCount(len(results))
        self.WidgetDSBHCT.setRowCount(len(results))
        tablerow =0
        for row in results: 
           self.WidgetDSBHCT.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
           self.WidgetDSBHCT.setItem(tablerow, 1, QTableWidgetItem(str(row[1])))
           self.WidgetDSBHCT.setItem(tablerow, 2, QTableWidgetItem(str(row[2])))
           self.WidgetDSBHCT.setItem(tablerow, 3, QTableWidgetItem(str(row[3])))
           #self.WidgetDSBH.setItem(tablerow, 4, QTableWidgetItem(str(row[4])))
           #self.WidgetDSBH.setItem(tablerow, 5, QTableWidgetItem(str(row[5])))
           #self.WidgetDSBH.setItem(tablerow, 6, QTableWidgetItem(str(row[6])))
           #self.tableWidget.setItem(tablerow, 7, QTableWidgetItem(str(row[7])))
           #self.tableWidget.setItem(tablerow, 8, QTableWidgetItem(str(row[8])))
           #self.tableWidget.setItem(tablerow, 9, QTableWidgetItem(str(row[9])))
           tablerow += 1
    def handle_exit(self):
        self.btnbackMN_2.clicked.connect(QApplication.instance().exit)
# show dữ liệu lên text box lên DSBH
    def show_selected_data(self, row, column):
        try:
            # Hiển thị dữ liệu từ hàng được chọn lên các QLineEdit
            self.txtMaHD_1.setText(self.WidgetDSBH.item(row, 0).text())
            self.txtMaNV_1.setText(self.WidgetDSBH.item(row, 1).text())
            self.txtNgayLap_1.setText(self.WidgetDSBH.item(row, 2).text())
            self.txtTenKhach_1.setText(self.WidgetDSBH.item(row,3).text())
            self.txtHTTT.setText(self.WidgetDSBH.item(row, 4).text())
            # self.txtSdtNCC.setText(self.tableWidget.item(row, 4).text())
            # self.txtSoLuong.setText(self.tableWidget.item(row, 5).text())
            # self.txtNVLap.setText(self.tableWidget.item(row, 6).text())
            # self.txtNgayNhap.setText(self.tableWidget.item(row, 7).text())
        except Exception as e:
            print(f"Error in show_selected_data: {e}")       
# show dữ liệu lên text box lên DSBH chi tiết
    def show_selected_data_ct(self, row, column):
        try:
            # Hiển thị dữ liệu từ hàng được chọn lên các QLineEdit
            self.txtMaHD_2.setText(self.WidgetDSBHCT.item(row, 0).text())
            self.txtMaSP_2.setText(self.WidgetDSBHCT.item(row, 1).text())
            self.txtSL.setText(self.WidgetDSBHCT.item(row, 2).text())
            self.txDonGia.setText(self.WidgetDSBHCT.item(row,3).text())
            #self.txtHTTT.setText(self.WidgetDSBH.item(row, 4).text())
            # self.txtSdtNCC.setText(self.tableWidget.item(row, 4).text())
            # self.txtSoLuong.setText(self.tableWidget.item(row, 5).text())
            # self.txtNVLap.setText(self.tableWidget.item(row, 6).text())
            # self.txtNgayNhap.setText(self.tableWidget.item(row, 7).text())
        except Exception as e:
            print(f"Error in show_selected_data: {e}")  

# code sử lý khi sửa thuộc tính các nút button
     # code xử lý thêm 1 trường dữ liệu mới
    def insert_data(self):
        sMaHDX = self.txtMaHD_2.text()
        sMaSP = self.txtMaSP_2.text()
        iSoLuong = int(self.txtSL.text())
        fDonGiaXuat = float(self.txDonGia.text())
        try:
            # Kết nối đến cơ sở dữ liệu
            db = mdb.connect('localhost', 'root', '', 'kinhdoanhmaytinh')
            query = db.cursor()
            # Thực thi câu lệnh SQL để thêm dữ liệu vào cơ sở dữ liệu
            query.callproc("InsertInto_tblctxuat", (sMaHDX, sMaSP, iSoLuong, fDonGiaXuat))
    
            db.commit()

            # Thông báo thành công và làm mới dữ liệu trên giao diện
            QMessageBox.information(self, "Thành công", "Thêm dữ liệu thành công!")
            self.loaddata1()  # Làm mới dữ liệu sau khi thêm
        except Exception as e:
            # Trong trường hợp có lỗi, rollback và hiển thị thông báo lỗi
            db.rollback()
            QMessageBox.warning(self, "Lỗi", f"Đã xảy ra lỗi: {str(e)}")
        finally:
            # Đóng kết nối với cơ sở dữ liệu
            db.close()
#     def update_DSBH(self):
#         db= mdb.connect('localhost','root','','kinhdoanhmaytinh')
#         query = db.cursor()
#         query.execute("update tblhdxuat set sMaHDX='"+txtMaHD_2+"',MaSP='"+masp+"',TenSP='"+tensp+"',soluong = '"+soluong+"',dongia ='"+dongia+"',tongtien = '"+tongtien+"',Baohanh = '"+baohanh+"'where MaHD = '"+mahd+"' ")
#         db.commit()
#         self.loaddata()
# #---------------------------------------------------------------------------------------------

