# Form implementation generated from reading ui file 'agent.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AgentWindow(object):
    def setupUi(self, AgentWindow):
        AgentWindow.setObjectName("AgentWindow")
        AgentWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=AgentWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 150, 701, 391))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.btnShow = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnShow.setGeometry(QtCore.QRect(340, 80, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnShow.setFont(font)
        self.btnShow.setObjectName("btnShow")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 10, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        AgentWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=AgentWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        AgentWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=AgentWindow)
        self.statusbar.setObjectName("statusbar")
        AgentWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AgentWindow)
        QtCore.QMetaObject.connectSlotsByName(AgentWindow)

    def retranslateUi(self, AgentWindow):
        _translate = QtCore.QCoreApplication.translate
        AgentWindow.setWindowTitle(_translate("AgentWindow", "MainWindow"))
        self.btnShow.setText(_translate("AgentWindow", "Hiển thị"))
        self.label.setText(_translate("AgentWindow", "Danh sách nhân viên"))
