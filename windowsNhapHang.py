from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
import sys
import re
import MySQLdb as mdb

class PhieuNhapkho(QMainWindow):
    def __init__(self):
        super(PhieuNhapkho, self).__init__()
        uic.loadUi('PhieuNhapkho.ui', self)   
        self.loaddata()
        self.tableWidget.cellClicked.connect(self.show_selected_data)
        self.xoa.clicked.connect(self.delete_data)
        self.them.clicked.connect(self.insert_data)

        self.setWindowTitle("Validate Input")
        self.setGeometry(100, 100, 400, 200)

        self.txtMaPhieu.textChanged.connect(self.validate_input)

    def validate_input(self, text):
        # Kiểm tra nếu text không phải là số
        sender = self.sender()  # Xác định đối tượng gửi sự kiện
        text = sender.text()  # Lấy văn bản từ QLineEdit
        if self.contains_special_chars(text):
            self.label_5.setText("Lỗi: Vui lòng không nhập kí tự đặc biệt!")
            self.label_5.setVisible(True)  # Hiển thị label_error
        else:
            self.label_5.setVisible(False)  # Ẩn label_error khi nhập đúng
#hàm kiểm tra kí tự đặc biệt
    def contains_special_chars(self, text):
        # Kiểm tra xem có ký tự đặc biệt nào trong chuỗi không
        special_chars = re.compile("[@_!#$%^&*()<>?/\|}{~:]")
        return special_chars.search(text) is not None
    def loaddata(self):
        #kết nối đến cơ sở dữ liệu
        db = mdb.connect('localhost', 'root', '', 'login_qtpy6')
        query = db.cursor()
        query.execute("SELECT * FROM  hanghoa")
        results = query.fetchall()
        self.tableWidget.setRowCount(len(results))
        tablerow = 0
        for row in results: 
            self.tableWidget.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(tablerow, 1, QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(tablerow, 2, QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(tablerow, 3, QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(tablerow, 4, QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(tablerow, 5, QTableWidgetItem(str(row[5])))
            self.tableWidget.setItem(tablerow, 6, QTableWidgetItem(str(row[6])))
            self.tableWidget.setItem(tablerow, 7, QTableWidgetItem(str(row[7])))
            tablerow += 1

        # Đóng kết nối với cơ sở dữ liệu
        db.close()
        
#thêm hàng hóa vào trong kho
    def insert_data(self):
        mahd = self.txtMaPhieu.text()
        masp = self.txtMaSP.text()
        tensp = self.txtTenSP.text()
        tenNCC = self.txtTenNCC.text()
        sdtNCC = self.txtSdtNCC.text()
        sl = self.txtSoLuong.text()
        nv = self.txtNVLap.text()
        ngaynhap_date = self.NgayNhap.date()  # Lấy giá trị ngày nhập từ Date Edit
        ngaynhap = ngaynhap_date.toString()  # Chuyển đổi thành định dạng datetime
        if not all([mahd, masp, tensp, tenNCC, sdtNCC, sl, nv, ngaynhap_date]):
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return
        if not all([mahd.isdigit(), sdtNCC.isdigit(), sl.isdigit()]):
             QMessageBox.warning(self, "Lỗi", "Vui lòng chỉ nhập số trong mã hóa đơn số điện thoại và số lượng!")
             return
        try:
            # Kết nối đến cơ sở dữ liệu
            db = mdb.connect('localhost', 'root', '', 'login_qtpy6')
            query = db.cursor()
            # Thực thi câu lệnh SQL để thêm dữ liệu vào cơ sở dữ liệu
            query.execute("INSERT INTO hanghoa value('"+mahd+"','"+masp+"','"+tensp+"','"+tenNCC+"','"+sdtNCC+"','"+sl+"','"+nv+"','"+ngaynhap+"')")
            db.commit()

            # Thông báo thành công và làm mới dữ liệu trên giao diện
            QMessageBox.information(self, "Thành công", "Thêm dữ liệu thành công!")
            self.loaddata()  # Làm mới dữ liệu sau khi thêm
        except Exception as e:
            # Trong trường hợp có lỗi, rollback và hiển thị thông báo lỗi
            db.rollback()
            QMessageBox.warning(self, "Lỗi", f"Đã xảy ra lỗi: {str(e)}")
        finally:
            # Đóng kết nối với cơ sở dữ liệu
            db.close()
#Xóa dữ liệu
    def delete_data(self):
        mahd = self.txtMaPhieu.text()
        if not mahd:
                QMessageBox.warning(self,"Error","Vui lòng nhập hóa đơn cần xóa")
                return
        reply = QMessageBox.question(self, 'Xác nhận xóa', 'Bạn có chắc chắn muốn xóa dữ liệu này?',
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply ==QMessageBox.StandardButton.Yes:
            try:
                db = mdb.connect('localhost', 'root', '', 'login_qtpy6')
                query = db.cursor()
            # Tạo câu lệnh SQL để xóa dữ liệu từ bảng dựa trên mã hóa đơn
                query.execute("DELETE FROM hanghoa WHERE MaPhieu = %s", (mahd,))

            # Lưu các thay đổi vào cơ sở dữ liệu
                db.commit()

            # Thông báo thành công
                QMessageBox.information(self, "Success", "xóa dữ liệu thành công!")

            # Sau khi xóa dữ liệu thành công, làm mới bảng
                self.loaddata()
            except Exception as e:
            # Trong trường hợp có lỗi, rollback và hiển thị thông báo lỗi
                db.rollback()
                QMessageBox.warning(self, "Error", f"Đã xảy ra lỗi: {str(e)}")
            finally:
            # Đóng kết nối với cơ sở dữ liệu
             db.close()
        else:
              QMessageBox.information(self, "Thông báo", "Hủy xóa dữ liệu!")

# hiển thị thông tin lên bảng
    def show_selected_data(self, row, column):
        try:
            # Hiển thị dữ liệu từ hàng được chọn lên các QLineEdit
            self.txtMaPhieu.setText(self.tableWidget.item(row, 0).text())
            self.txtMaSP.setText(self.tableWidget.item(row, 1).text())
            self.txtTenSP.setText(self.tableWidget.item(row, 2).text())
            self.txtTenNCC.setText(self.tableWidget.item(row, 3).text())
            self.txtSdtNCC.setText(self.tableWidget.item(row, 4).text())
            self.txtSoLuong.setText(self.tableWidget.item(row, 5).text())
            self.txtNVLap.setText(self.tableWidget.item(row, 6).text())
            self.txtNgayNhap.setText(self.tableWidget.item(row, 7).text())
        except Exception as e:
            print(f"Error in show_selected_data: {e}")

app = QApplication(sys.argv) 
Widget = QtWidgets.QStackedWidget()
phieunk = PhieuNhapkho() 
phieunk.show() 
Widget.addWidget(phieunk)  
Widget.setFixedHeight(800) 
Widget.setFixedWidth(1000) 
Widget.show()
app.exec()