from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
import sys
import re
import MySQLdb as mdb

class NhapHang(QMainWindow):
    def __init__(self):
        super(NhapHang, self).__init__()
        uic.loadUi('DSHDN.ui', self)   
        self.loaddata()
        self.loaddata1()
    # code sử lý load data lên trang DSBH
    def loaddata(self):
        db= mdb.connect('localhost','root','','kinhdoanhmaytinh')
        query = db.cursor()
        query.execute("SELECT * FROM tblhdnhap")
        results = query.fetchall()
        #self.tableWidget.setRowCount(len(results))
        self.WidgetDSBH.setRowCount(len(results))
        tablerow =0
        for row in results: 
           self.WidgetDSBH.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
           self.WidgetDSBH.setItem(tablerow, 1, QTableWidgetItem(str(row[1])))
           self.WidgetDSBH.setItem(tablerow, 2, QTableWidgetItem(str(row[2])))
           self.WidgetDSBH.setItem(tablerow, 3, QTableWidgetItem(str(row[3])))
           #self.WidgetDSBH.setItem(tablerow, 4, QTableWidgetItem(str(row[4])))
           #self.WidgetDSBH.setItem(tablerow, 5, QTableWidgetItem(str(row[5])))
           #fself.WidgetDSBH.setItem(tablerow, 6, QTableWidgetItem(str(row[6])))
           #self.tableWidget.setItem(tablerow, 7, QTableWidgetItem(str(row[7])))
           #self.tableWidget.setItem(tablerow, 8, QTableWidgetItem(str(row[8])))
           #self.tableWidget.setItem(tablerow, 9, QTableWidgetItem(str(row[9])))
           tablerow += 1
# code sử lý load data lên trang DSBH chi tiết
    def loaddata1(self):
        db= mdb.connect('localhost','root','','kinhdoanhmaytinh')
        query = db.cursor()
        query.execute("SELECT * FROM tblctnhap")
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
# app = QApplication(sys.argv) 
# Widget = QtWidgets.QStackedWidget()
# nhaphang_show = NhapHang() 
# nhaphang_show.show() 
# Widget.addWidget(nhaphang_show)  
# Widget.setFixedHeight(800) 
# Widget.setFixedWidth(1500) 
# Widget.show()
# app.exec()