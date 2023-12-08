import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):  # 메인윈도우 생성
    def __init__(self):
        super().__init__()  #부모클래스인 QMainWindow의 생성자를 실행

        self.setWindowTitle("연습프로그램v1.0")
        self.setGeometry(300,300,500,500)
        self.setWindowIcon(QIcon("icon/google.png"))


app = QApplication(sys.argv)
win = MyWindow()
win.show()

app.exec_()