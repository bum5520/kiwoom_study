import sys
from PyQt4.QtGui import *

app = QApplication(sys.argv)
button = QPushButton("Quit")
button.show()
app.exec_()