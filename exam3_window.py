import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        """
        super().__는 부모 클래스의 생성자를 호출할때사용
        """
        self.setWindowTitle("Study for stock")
        self.setGeometry(300,400,300,300)
        button1 = QPushButton('click me',self)
        button1.move(100,100)
        button1.clicked.connect(self.button1_clicked)

    def button1_clicked(self):
        QMessageBox.about(self,"window","clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec_()