# Form implementation generated from reading ui file 'DSHDN.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
import sys
import MySQLdb as mdb



class DSHDN(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1147, 797)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.hoadobanhang_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.hoadobanhang_2.setGeometry(QtCore.QRect(40, 40, 1121, 401))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.hoadobanhang_2.setFont(font)
        self.hoadobanhang_2.setObjectName("hoadobanhang_2")
        self.WidgetDSNH_3 = QtWidgets.QTableWidget(parent=self.hoadobanhang_2)
        self.WidgetDSNH_3.setGeometry(QtCore.QRect(10, 30, 691, 351))
        self.WidgetDSNH_3.setColumnCount(4)
        self.WidgetDSNH_3.setObjectName("WidgetDSNH_3")
        self.WidgetDSNH_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.WidgetDSNH_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.WidgetDSNH_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.WidgetDSNH_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.WidgetDSNH_3.setHorizontalHeaderItem(3, item)
        self.WidgetDSNH_3.horizontalHeader().setDefaultSectionSize(98)
        self.WidgetDSNH_3.horizontalHeader().setMinimumSectionSize(48)
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.hoadobanhang_2)
        self.groupBox_5.setGeometry(QtCore.QRect(720, 20, 391, 371))
        self.groupBox_5.setObjectName("groupBox_5")
        self.btnSua1 = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.btnSua1.setGeometry(QtCore.QRect(150, 200, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnSua1.setFont(font)
        self.btnSua1.setObjectName("btnSua1")
        self.btnthem1 = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.btnthem1.setGeometry(QtCore.QRect(30, 200, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnthem1.setFont(font)
        self.btnthem1.setObjectName("btnthem1")
        self.btnxoa1 = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.btnxoa1.setGeometry(QtCore.QRect(270, 200, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnxoa1.setFont(font)
        self.btnxoa1.setObjectName("btnxoa1")
        self.btnbackMN_1 = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.btnbackMN_1.setGeometry(QtCore.QRect(130, 290, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnbackMN_1.setFont(font)
        self.btnbackMN_1.setObjectName("btnbackMN_1")
        self.txtMaNV = QtWidgets.QLineEdit(parent=self.groupBox_5)
        self.txtMaNV.setGeometry(QtCore.QRect(162, 60, 211, 20))
        self.txtMaNV.setText("")
        self.txtMaNV.setObjectName("txtMaNV")
        self.txtNgayLap = QtWidgets.QLineEdit(parent=self.groupBox_5)
        self.txtNgayLap.setGeometry(QtCore.QRect(160, 90, 211, 20))
        self.txtNgayLap.setObjectName("txtNgayLap")
        self.label_23 = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label_23.setGeometry(QtCore.QRect(30, 60, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label_24.setGeometry(QtCore.QRect(30, 90, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.txtMaHD = QtWidgets.QLineEdit(parent=self.groupBox_5)
        self.txtMaHD.setGeometry(QtCore.QRect(162, 30, 211, 20))
        self.txtMaHD.setObjectName("txtMaHD")
        self.label_25 = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label_25.setGeometry(QtCore.QRect(30, 30, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label_26.setGeometry(QtCore.QRect(30, 120, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.txtTennhaPP = QtWidgets.QLineEdit(parent=self.groupBox_5)
        self.txtTennhaPP.setGeometry(QtCore.QRect(160, 120, 211, 20))
        self.txtTennhaPP.setText("")
        self.txtTennhaPP.setObjectName("txtTennhaPP")
        self.hoadobanhang_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.hoadobanhang_3.setGeometry(QtCore.QRect(40, 450, 1111, 291))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.hoadobanhang_3.setFont(font)
        self.hoadobanhang_3.setObjectName("hoadobanhang_3")
        self.WidgetDSNHCT_3 = QtWidgets.QTableWidget(parent=self.hoadobanhang_3)
        self.WidgetDSNHCT_3.setGeometry(QtCore.QRect(10, 30, 681, 251))
        self.WidgetDSNHCT_3.setColumnCount(4)
        self.WidgetDSNHCT_3.setObjectName("WidgetDSNHCT_3")
        self.WidgetDSNHCT_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.WidgetDSNHCT_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.WidgetDSNHCT_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.WidgetDSNHCT_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.WidgetDSNHCT_3.setHorizontalHeaderItem(3, item)
        self.WidgetDSNHCT_3.horizontalHeader().setDefaultSectionSize(122)
        self.WidgetDSNHCT_3.horizontalHeader().setMinimumSectionSize(48)
        self.groupBox_6 = QtWidgets.QGroupBox(parent=self.hoadobanhang_3)
        self.groupBox_6.setGeometry(QtCore.QRect(710, 20, 391, 261))
        self.groupBox_6.setObjectName("groupBox_6")
        self.btnSua2 = QtWidgets.QPushButton(parent=self.groupBox_6)
        self.btnSua2.setGeometry(QtCore.QRect(150, 200, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnSua2.setFont(font)
        self.btnSua2.setObjectName("btnSua2")
        self.btnthem2 = QtWidgets.QPushButton(parent=self.groupBox_6)
        self.btnthem2.setGeometry(QtCore.QRect(30, 200, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnthem2.setFont(font)
        self.btnthem2.setObjectName("btnthem2")
        self.btnxoa2 = QtWidgets.QPushButton(parent=self.groupBox_6)
        self.btnxoa2.setGeometry(QtCore.QRect(270, 200, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnxoa2.setFont(font)
        self.btnxoa2.setObjectName("btnxoa2")
        self.txtMaSP = QtWidgets.QLineEdit(parent=self.groupBox_6)
        self.txtMaSP.setGeometry(QtCore.QRect(162, 60, 211, 20))
        self.txtMaSP.setText("")
        self.txtMaSP.setObjectName("txtMaSP")
        self.txtSL_3 = QtWidgets.QLineEdit(parent=self.groupBox_6)
        self.txtSL_3.setGeometry(QtCore.QRect(160, 90, 211, 20))
        self.txtSL_3.setObjectName("txtSL_3")
        self.label_28 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_28.setGeometry(QtCore.QRect(30, 60, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_29.setGeometry(QtCore.QRect(30, 90, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.txtMaHD_5 = QtWidgets.QLineEdit(parent=self.groupBox_6)
        self.txtMaHD_5.setGeometry(QtCore.QRect(162, 30, 211, 20))
        self.txtMaHD_5.setObjectName("txtMaHD_5")
        self.label_30 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_30.setGeometry(QtCore.QRect(30, 30, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_31.setGeometry(QtCore.QRect(30, 120, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.txDonGia_3 = QtWidgets.QLineEdit(parent=self.groupBox_6)
        self.txDonGia_3.setGeometry(QtCore.QRect(160, 120, 211, 20))
        self.txDonGia_3.setText("")
        self.txDonGia_3.setObjectName("txDonGia_3")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 0, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1147, 21))
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
        item = self.WidgetDSNH_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mã Hóa Đơn"))
        item = self.WidgetDSNH_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Mã Nhân Viên"))
        item = self.WidgetDSNH_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ngày Lập"))
        item = self.WidgetDSNH_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Tên Nhà Cung Cấp"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Thao Tác"))
        self.btnSua1.setText(_translate("MainWindow", "Sửa"))
        self.btnthem1.setText(_translate("MainWindow", "Thêm mới"))
        self.btnxoa1.setText(_translate("MainWindow", "Loại Bỏ"))
        self.btnbackMN_1.setText(_translate("MainWindow", "Thoát"))
        self.label_23.setText(_translate("MainWindow", "Mã Nhân Viên"))
        self.label_24.setText(_translate("MainWindow", "Ngày Lập"))
        self.label_25.setText(_translate("MainWindow", "Mã Hóa Đơn"))
        self.label_26.setText(_translate("MainWindow", "Tên Nhà Cung Cấp"))
        self.hoadobanhang_3.setTitle(_translate("MainWindow", "Danh Sách Hóa Đơn Chi Tiết"))
        item = self.WidgetDSNHCT_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mã Hóa Đơn"))
        item = self.WidgetDSNHCT_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Mã Sản Phẩm"))
        item = self.WidgetDSNHCT_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Số Lượng"))
        item = self.WidgetDSNHCT_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Đơn Giá Nhập"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Thao Tác"))
        self.btnSua2.setText(_translate("MainWindow", "Sửa"))
        self.btnthem2.setText(_translate("MainWindow", "Thêm mới"))
        self.btnxoa2.setText(_translate("MainWindow", "Loại Bỏ"))
        self.label_28.setText(_translate("MainWindow", "Mã Mã Sản Phẩm"))
        self.label_29.setText(_translate("MainWindow", "Số Lượng "))
        self.label_30.setText(_translate("MainWindow", "Mã Hóa Đơn"))
        self.label_31.setText(_translate("MainWindow", "Đơn Giá Nhập"))
        self.label.setText(_translate("MainWindow", "Quản Lý Nhập Hàng"))
# code sử lý sự kiện .Py
class Nhaphang(QMainWindow, DSHDN):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnbackMN_1.clicked.connect(QApplication.instance().exit)
        self.btnthem1.clicked.connect(self.insertHDN)
        self.btnxoa1.clicked.connect(self.delete_data)
        self.btnthem2.clicked.connect(self.insertCTN)
        self.btnxoa2.clicked.connect(self.delete_data2)
        self.btnSua1.clicked.connect(self.updateHDN)
        self.btnSua2.clicked.connect(self.updateCTHDN)
        self.loaddata()
        self.loaddata1()
        self.WidgetDSNH_3.cellClicked.connect(self.show_selected_data)
        self.WidgetDSNHCT_3.cellClicked.connect(self.show_selected_data_ct)
        
# code sử lý load data lên trang DSNH
    def loaddata(self):
        db= mdb.connect('localhost','root','','kinhdoanhmaytinh')
        query = db.cursor()
        query.execute("SELECT * FROM tblhdnhap")
        results = query.fetchall()
        #self.tableWidget.setRowCount(len(results))
        self.WidgetDSNH_3.setRowCount(len(results))
        tablerow =0
        for row in results: 
           self.WidgetDSNH_3.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
           self.WidgetDSNH_3.setItem(tablerow, 1, QTableWidgetItem(str(row[1])))
           self.WidgetDSNH_3.setItem(tablerow, 2, QTableWidgetItem(str(row[2])))
           self.WidgetDSNH_3.setItem(tablerow, 3, QTableWidgetItem(str(row[3])))
           #self.WidgetDSNH_3.setItem(tablerow, 4, QTableWidgetItem(str(row[4])))
           #self.WidgetDSNH_3.setItem(tablerow, 5, QTableWidgetItem(str(row[5])))
           #self.WidgetDSBH.setItem(tablerow, 6, QTableWidgetItem(str(row[6])))
           #self.tableWidget.setItem(tablerow, 7, QTableWidgetItem(str(row[7])))
           #self.tableWidget.setItem(tablerow, 8, QTableWidgetItem(str(row[8])))
           #self.tableWidget.setItem(tablerow, 9, QTableWidgetItem(str(row[9])))
           tablerow += 1
# code sử lý load data lên trang DSNH chi tiết
    def loaddata1(self):
        db= mdb.connect('localhost','root','','kinhdoanhmaytinh')
        query = db.cursor()
        query.execute("SELECT * FROM tblctnhap")
        results = query.fetchall()
        #self.tableWidget.setRowCount(len(results))
        self.WidgetDSNHCT_3.setRowCount(len(results))
        tablerow =0
        for row in results: 
           self.WidgetDSNHCT_3.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
           self.WidgetDSNHCT_3.setItem(tablerow, 1, QTableWidgetItem(str(row[1])))
           self.WidgetDSNHCT_3.setItem(tablerow, 2, QTableWidgetItem(str(row[2])))
           self.WidgetDSNHCT_3.setItem(tablerow, 3, QTableWidgetItem(str(row[3])))
           #self.WidgetDSBH.setItem(tablerow, 4, QTableWidgetItem(str(row[4])))
           #self.WidgetDSBH.setItem(tablerow, 5, QTableWidgetItem(str(row[5])))
           #self.WidgetDSBH.setItem(tablerow, 6, QTableWidgetItem(str(row[6])))
           #self.tableWidget.setItem(tablerow, 7, QTableWidgetItem(str(row[7])))
           #self.tableWidget.setItem(tablerow, 8, QTableWidgetItem(str(row[8])))
           #self.tableWidget.setItem(tablerow, 9, QTableWidgetItem(str(row[9])))
           tablerow += 1
#code xử lý insert hóa đơn
    def insertHDN(self):
        mahd = self.txtMaHD.text()
        manv = self.txtMaNV.text()
        ngaylap = self.txtNgayLap.text()
        tennpp = self.txtTennhaPP.text()
        if not all([mahd, manv, ngaylap, tennpp]):
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return
        try:
            # Kết nối đến cơ sở dữ liệu
            db = mdb.connect('localhost', 'root', '', 'kinhdoanhmaytinh')
            query = db.cursor()
            # Thực thi câu lệnh SQL để thêm dữ liệu vào cơ sở dữ liệu
            query.callproc('InsertHDNhap', (mahd, manv, ngaylap, tennpp))
    
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
#code xử lý insert hóa đơn chi tiết
    def insertCTN(self):
        mahd = self.txtMaHD_5.text()
        manv = self.txtMaSP.text()
        ngaylap = self.txtSL_3.text()
        tennpp = self.txDonGia_3.text()
        if not all([mahd, manv, ngaylap, tennpp]):
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return
        try:
            # Kết nối đến cơ sở dữ liệu
            db = mdb.connect('localhost', 'root', '', 'kinhdoanhmaytinh')
            query = db.cursor()
            # Thực thi câu lệnh SQL để thêm dữ liệu vào cơ sở dữ liệu
            query.callproc('InsertCTNhap', (mahd, manv, ngaylap, tennpp))
    
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
# show dữ liệu lên text box lên DSNH
    def show_selected_data(self, row, column):
        try:
            # Hiển thị dữ liệu từ hàng được chọn lên các QLineEdit
            self.txtMaHD.setText(self.WidgetDSNH_3.item(row, 0).text())
            self.txtMaNV.setText(self.WidgetDSNH_3.item(row, 1).text())
            self.txtNgayLap.setText(self.WidgetDSNH_3.item(row, 2).text())
            self.txtTennhaPP.setText(self.WidgetDSNH_3.item(row,3).text())
        except Exception as e:
            print(f"Error in show_selected_data: {e}")       
# show dữ liệu lên text box lên DSNH chi tiết
    def show_selected_data_ct(self, row, column):
        try:
            # Hiển thị dữ liệu từ hàng được chọn lên các QLineEdit
            self.txtMaHD_5.setText(self.WidgetDSNHCT_3.item(row, 0).text())
            self.txtMaSP.setText(self.WidgetDSNHCT_3.item(row, 1).text())
            self.txtSL_3.setText(self.WidgetDSNHCT_3.item(row, 2).text())
            self.txDonGia_3.setText(self.WidgetDSNHCT_3.item(row,3).text())
        except Exception as e:
            print(f"Error in show_selected_data: {e}")  
#xóa hóa đơn nhập
    def delete_data(self):
        mahd = self.txtMaHD.text()
        if not mahd:
                QMessageBox.warning(self,"Error","Vui lòng nhập hóa đơn cần xóa")
                return
        reply = QMessageBox.question(self, 'Xác nhận xóa', 'Bạn có chắc chắn muốn xóa dữ liệu này?',
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply ==QMessageBox.StandardButton.Yes:
            try:
                db = mdb.connect('localhost', 'root', '', 'kinhdoanhmaytinh')
                query = db.cursor()
            # Tạo câu lệnh SQL để xóa dữ liệu từ bảng dựa trên mã hóa đơn
                query.callproc('DeleteHDNhap', [mahd])
  
            # Thông báo thành công
                QMessageBox.information(self, "Success", "xóa dữ liệu thành công!")

            # Sau khi xóa dữ liệu thành công, làm mới bảng
                self.loaddata()
                self.loaddata1()
            except Exception as e:
            # Trong trường hợp có lỗi, rollback và hiển thị thông báo lỗi
                db.rollback()
                QMessageBox.warning(self, "Error", f"Đã xảy ra lỗi: {str(e)}")
            finally:
            # Đóng kết nối với cơ sở dữ liệu
             db.close()
        else:
              QMessageBox.information(self, "Thông báo", "Hủy xóa dữ liệu!")
#xóa chi tiết hóa đơn nhập
    def delete_data2(self):
        masp = self.txtMaSP.text()
        if not masp:
                QMessageBox.warning(self,"Error","Vui lòng nhập hóa đơn cần xóa")
                return
        reply = QMessageBox.question(self, 'Xác nhận xóa', 'Bạn có chắc chắn muốn xóa dữ liệu này?',
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply ==QMessageBox.StandardButton.Yes:
            try:
                db = mdb.connect('localhost', 'root', '', 'kinhdoanhmaytinh')
                query = db.cursor()
            # Tạo câu lệnh SQL để xóa dữ liệu từ bảng dựa trên mã hóa đơn
                query.callproc('DeleteProductFromCTNhap', [masp])
  
            # Thông báo thành công
                QMessageBox.information(self, "Success", "xóa dữ liệu thành công!")

            # Sau khi xóa dữ liệu thành công, làm mới bảng
                self.loaddata1()
            except Exception as e:
            # Trong trường hợp có lỗi, rollback và hiển thị thông báo lỗi
                db.rollback()
                QMessageBox.warning(self, "Error", f"Đã xảy ra lỗi: {str(e)}")
            finally:
            # Đóng kết nối với cơ sở dữ liệu
             db.close()
        else:
              QMessageBox.information(self, "Thông báo", "Hủy xóa dữ liệu!")
#code xử lý update hóa đơn chi tiết
    def updateHDN(self):
        mahd = self.txtMaHD.text()
        manv = self.txtMaNV.text()
        ngaylap = self.txtNgayLap.text()
        tennpp = self.txtTennhaPP.text()
        try:
            # Kết nối đến cơ sở dữ liệu
            db = mdb.connect('localhost', 'root', '', 'kinhdoanhmaytinh')
            query = db.cursor()
            # Thực thi câu lệnh SQL để thêm dữ liệu vào cơ sở dữ liệu
            query.callproc('UpdateHDNhap', (mahd, manv, ngaylap, tennpp))
    
            db.commit()

            # Thông báo thành công và làm mới dữ liệu trên giao diện
            QMessageBox.information(self, "Thành công", "Sửa dữ liệu thành công!")
            self.loaddata()  # Làm mới dữ liệu sau khi thêm
        except Exception as e:
            # Trong trường hợp có lỗi, rollback và hiển thị thông báo lỗi
            db.rollback()
            QMessageBox.warning(self, "Lỗi", f"Đã xảy ra lỗi: {str(e)}")
        finally:
            # Đóng kết nối với cơ sở dữ liệu
            db.close()# #code xử lý update hóa đơn chi tiết
    def updateCTHDN(self):
        mahd = self.txtMaHD_5.text()
        masp = self.txtMaSP.text()
        soluong = self.txtSL_3.text()
        dongia = self.txDonGia_3.text()
        try:
            # Kết nối đến cơ sở dữ liệu
            db = mdb.connect('localhost', 'root', '', 'kinhdoanhmaytinh')
            query = db.cursor()
            # Thực thi câu lệnh SQL để thêm dữ liệu vào cơ sở dữ liệu
            query.callproc('UpdateCTNhap', (mahd, masp, soluong, dongia))
    
            db.commit()

            # Thông báo thành công và làm mới dữ liệu trên giao diện
            QMessageBox.information(self, "Thành công", "Sửa dữ liệu thành công!")
            self.loaddata1()  # Làm mới dữ liệu sau khi thêm
        except Exception as e:
            # Trong trường hợp có lỗi, rollback và hiển thị thông báo lỗi
            db.rollback()
            QMessageBox.warning(self, "Lỗi", f"Đã xảy ra lỗi: {str(e)}")
        finally:
            # Đóng kết nối với cơ sở dữ liệu
            db.close()#
#---------------------------------------------------------------------------------------------
