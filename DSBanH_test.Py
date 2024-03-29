from  PyQt6 import QtCore,QtGui,QtWidgets,uic
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
import sys
import MySQLdb as mdb

class DSBH(QMainWindow):
    def __init__(self):
        super(DSBH, self).__init__()
        uic.loadUi('DSBanH.ui',self)
        self.loaddata()
        # code thoát chương trình   
        #self.btn_exit.clicked.connect(QApplication.instance().exit)
        # code chuyển tab 
        # code tab bán hàng
     # Ẩn trang hiện tại đi 

    def loaddata(self):
        db= mdb.connect('localhost','root','','cdn_btl')
        query = db.cursor()
        query.execute("SELECT * FROM hoadonban_giatri")
        results = query.fetchall()
        #self.tableWidget.setRowCount(len(results))
        self.WidgetBanhang.setRowCount(len(results))
        tablerow =0
        for row in results: 
           self.WidgetBanhang.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
           self.WidgetBanhang.setItem(tablerow, 1, QTableWidgetItem(str(row[1])))
           self.WidgetBanhang.setItem(tablerow, 2, QTableWidgetItem(str(row[2])))
           self.WidgetBanhang.setItem(tablerow, 3, QTableWidgetItem(str(row[3])))
           self.WidgetBanhang.setItem(tablerow, 4, QTableWidgetItem(str(row[4])))
           #self.tableWidget.setItem(tablerow, 5, QTableWidgetItem(str(row[5])))
           #self.tableWidget.setItem(tablerow, 6, QTableWidgetItem(str(row[6])))
           #self.tableWidget.setItem(tablerow, 7, QTableWidgetItem(str(row[7])))
           #self.tableWidget.setItem(tablerow, 8, QTableWidgetItem(str(row[8])))
           #self.tableWidget.setItem(tablerow, 9, QTableWidgetItem(str(row[9])))
           tablerow += 1
    # code trở lại trang menu
# Giao diện menu
  
app = QApplication (sys.argv) 
Widget = QtWidgets.QStackedWidget()
DSBH1 = DSBH() 
Widget.addWidget(DSBH1)  
Widget.setFixedHeight(600) 
Widget.setFixedWidth(800) 
Widget.show()
app.exec()