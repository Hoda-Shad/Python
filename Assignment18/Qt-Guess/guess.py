import random

from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('guess.ui')
        self.ui.show()
        self.ui.setWindowTitle('Guess Game')
        self.ui.check_btn.clicked.connect(self.a)
        self.ui.new_btn.clicked.connect(self.b)
        self.num = random.randint(0, 100)


    def a(self):
        guess_num = int(self.ui.lineEdit.text())
        if self.num > guess_num :
            msgBox = QMessageBox()
            msgBox.setText('برو بالاتر')
            msgBox.exec()

        elif self.num < guess_num:
            msgBox = QMessageBox()
            msgBox.setText('برو پایین تر')
            msgBox.exec()
        else:
            msgBox = QMessageBox()
            msgBox.setText('برنده شدی')
            msgBox.exec()
            self.ui.lineEdit.setText('')

    def b(self):
        self.ui.lineEdit.setText('')

app = QApplication([])
win = MainWindow()
app.exec()