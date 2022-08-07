from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
import string
from random import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('pass.ui')
        self.ui.setWindowTitle('Password Generator')
        self.ui.show()
        self.ui.standardgenerate.clicked.connect(self.password_generator)
        self.ui.standardgenerate2.clicked.connect(self.extra_password_generator)
        self.ui.standardgenerate3.clicked.connect(self.super_password_generator)


    def password_generator(self):
        self.ui.lineEdit_2.setText('')
        self.ui.lineEdit_3.setText('')
        self.ui.lineEdit1.setText('')
        char = string.digits + string.punctuation + string.ascii_lowercase + string.ascii_uppercase
        password = ''
        for i in range (8):
            password += choice(char)
        self.ui.lineEdit1.setText(password)


    def extra_password_generator(self):
        self.ui.lineEdit_2.setText('')
        self.ui.lineEdit_3.setText('')
        self.ui.lineEdit1.setText('')
        char = string.digits + string.punctuation + string.ascii_lowercase + string.ascii_uppercase
        password = ''
        for i in range (12):
            password += choice(char)
        self.ui.lineEdit_2.setText(password)

    def super_password_generator(self):
        self.ui.lineEdit_2.setText('')
        self.ui.lineEdit_3.setText('')
        self.ui.lineEdit1.setText('')
        char = string.digits + string.punctuation + string.ascii_lowercase + string.ascii_uppercase
        password = ''
        for i in range (20):
            password += choice(char)
        self.ui.lineEdit_3.setText(password)

app = QApplication([])
# app.setStyleSheet(qdarkgraystyle.load_stylesheet())
window = MainWindow()
app.exec()


app = QApplication([])
window = MainWindow()
app.exec()