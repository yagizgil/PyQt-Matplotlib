from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys
import screen as scr

class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setUI()

        self.setWindowTitle("PyQt Matplotlib")
        self.setMinimumSize(QSize(200,200))
        self.show()

    def setUI(self):
        s = scr.Screen()

        self.setCentralWidget(s)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec())