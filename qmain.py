from agent import Ui_AgentWindow
from PyQt6.QtWidgets import *
import MySQLdb as mdb

# chương trình hiển thị danh sách nhân viên từ mysql

# thiết lập giao diện Cửa sổ Hiển thị nhân viên từ thiết kế
class AgentWindow(QMainWindow, Ui_AgentWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # gán hàm clickHandler cho sự kiện ấn nút Hiển thị  
        self.btnShow.clicked.connect(self.clickHandler)  
    # xử lý sự kiện ấn nút Hiển thị    
    def clickHandler(self):
        try:
            # kết nối đến database
            db = mdb.connect('localhost','root','','login_app')  
            # tạo con trỏ để truy vấn dữ liệu
            query = db.cursor() 
            # truy vấn dữ liệu
            query.execute("select * from agent_list")   
            # Lấy tất cả các hàng từ kết quả truy vấn
            rows = query.fetchall() 
            # Thiết lập số hàng và cột cho QTableWidget
            self.tableWidget.setRowCount(len(rows)) 
            self.tableWidget.setColumnCount(len(rows[0])) 
            # Lấy tên cột từ mô tả trường dữ liệu
            column_names = [i[0] for i in query.description]
            # Thiết lập tiêu đề cột
            self.tableWidget.setHorizontalHeaderLabels(column_names)
            # Hiển thị dữ liệu lấy được lên QTableWidget
            for i, row in enumerate(rows):
                for j, cell in enumerate(row):
                    item = QTableWidgetItem(str(cell))
                    self.tableWidget.setItem(i, j, item)

            # Đóng con trỏ và kết nối
            query.close()
            db.close()
        #xử lý ngoại lệ, hiển thị hộp thoại nếu lỗi
        except db.connector.Error as error:
            QMessageBox.information(self,"Thất bại","Lỗi khi kết nối đến cơ sở dữ liệu {error}")

# Khởi tạo đối tượng và hiển thị cửa sổ 
app = QApplication([])
Window = AgentWindow()
Window.show()
app.exec()

