import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):  # 메인윈도우 생성
    def __init__(self):
        super().__init__()  #부모클래스인 QMainWindow의 생성자를 실행

        self.setWindowTitle("연습프로그램v1.0")
        self.setGeometry(300,300,500,500)
        self.setWindowIcon(QIcon("icon/google.png"))

        self.btn = QPushButton("연습버튼", self)
        self.btn.move(100, 100)
        self.btn.resize(100, 50)

        self.label = QLabel("메시지창", self)
        self.label.move(100, 300)

        self.lineEdit = QLineEdit("텍스트입력",self)
        self.lineEdit.move(100,400)

        self.btn2 = QPushButton("출력버튼", self)
        self.btn2.move(200,400)

        self.btn.clicked.connect(self.btnClick)
        # 버튼이 클릭되는 이벤트가 일어나면 연결된 함수가 실행됨
        self.btn2.clicked.connect(self.btnClick2)

    def btnClick(self):
        print("연습버튼이 클릭되었습니다!!")
        self.label.clear() # 레이블지우기
        self.label.setText("연습버튼이 클릭!")

    def btnClick2(self):
        inputText = self.lineEdit.text()  # 사용자가 lineEdit에 입력한 텍스트 가져오기
        print(inputText)
        self.label.clear()  # 레이블지우기
        self.label.setText(inputText)



app = QApplication(sys.argv)
win = MyWindow()
win.show()

app.exec_()  # 무한루프