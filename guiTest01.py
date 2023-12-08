import sys

from PyQt5.QtWidgets import *

win = QApplication(sys.argv)  # QApplication 객체 생성

btn01 = QPushButton("연습버튼")
btn01.show()

label01 = QLabel("HelloWorld!!1")
label01.show()

win.exec_()  # win을 무한루프



