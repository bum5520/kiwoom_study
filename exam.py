import sys
from PyQt4.QtGui import *

app = QApplication(sys.argv)
label = QLabel("Hello PyQt")
label.show()
app.exec_()