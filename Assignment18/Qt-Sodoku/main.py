import random
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
import qdarkgraystyle


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('user.ui')
        self.ui.setWindowTitle('Sudoku Game')
        self.game = [[None for i in range(9)] for j in range(9)]  # backend
        self.dark = 0
        for i in range(9):
            for j in range(9):
                tb = QLineEdit()
                tb.setStyleSheet('font-size: 18px')
                tb.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                tb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.game[i][j] = tb
                self.game[i][j].textChanged.connect(self.check_game)
                self.ui.my_grid.addWidget(tb, i, j)  # front end

        self.ui.show()
        self.ui.btn_newgame.clicked.connect(self.new_game)
        self.ui.btn_check.clicked.connect(self.check_game)
        self.ui.btn_darkmode.clicked.connect(self.dark_game)
        self.win = 1


    def dark_game(self):
        self.dark = 1
        self.ui.setStyleSheet('background: dark gray; color: white')
        for i in range(9):
            for j in range(9):
                self.game[i][j].setStyleSheet('background: gray; color: white')

    def check_game(self):
        self.win = 1
        for row in range(9):  # Check rows
            for i in range(9):
                for j in range(9):
                    if self.game[row][i].text() == self.game[row][j].text() and i != j and self.game[row][i].text() != '':
                        self.game[row][i].setStyleSheet('font-size :32 px; color: black; background-color :pink')
                        self.win = 0


        for col in range(9):  # Check colums
            for i in range(9):
                for j in range(9):
                    if self.game[i][col].text() == self.game[j][col].text() and i != j and self.game[i][col].text() != '':
                        self.game[i][col].setStyleSheet('font-size :32 px; color: black; background-color :pink')
                        self.win = 0

        for i in range(0, 3):
            for j in range(0, 3):
                for row in range(0, 3):
                    for col in range(0, 3):
                        if self.game[i][j].text() == self.game[row][col].text() and i != row and j != col and \
                                self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size :32 px; color: black; background-color :pink')
                            self.win = 0

        for i in range(3, 6):
            for j in range(0, 3):
                for row in range(3, 6):
                    for col in range(0,3):
                        if self.game[i][j].text() == self.game[row][col].text() and i != row and j != col and \
                                self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size :32 px; color: black; background-color :pink')
                            self.win = 0

        for i in range(6, 9):
            for j in range(0, 3):
                for row in range(6, 9):
                    for col in range(0, 3):
                        if self.game[i][j].text() == self.game[row][col].text() and i != row and j != col and \
                                self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size :32 px; color: black; background-color :pink')
                            self.win = 0

        for i in range(0, 3):
            for j in range(3, 6):
                for row in range(0, 3):
                    for col in range(3, 6):
                        if self.game[i][j].text() == self.game[row][col].text() and i != row and j != col and \
                                self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size :32 px; color: black; background-color :pink')
                            self.win = 0

        for i in range(3, 6):
            for j in range(3, 6):
                for row in range(3, 6):
                    for col in range(3, 6):
                        if self.game[i][j].text() == self.game[row][col].text() and i != row and j != col and \
                                self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size :32 px; color: black; background-color :pink')
                            self.win = 0

        for i in range(6, 9):
            for j in range(3, 6):
                for row in range(6, 9):
                    for col in range(3, 6):
                        if self.game[i][j].text() == self.game[row][col].text() and i != row and j != col and \
                                self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size :32 px; color: black; background-color :pink')
                            self.win = 0

        for i in range(6, 9):
            for j in range(0, 3):
                for row in range(6, 9):
                    for col in range(0, 3):
                        if self.game[i][j].text() == self.game[row][col].text() and i != row and j != col and \
                                self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size :32 px; color: black; background-color :pink')
                            self.win = 0

        for i in range(6, 9):
            for j in range(3, 6):
                for row in range(6, 9):
                    for col in range(3, 6):
                        if self.game[i][j].text() == self.game[row][col].text() and i != row and j != col and \
                                self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size :32 px; color: black; background-color :pink')
                            self.win = 0

        for i in range(6, 9):
            for j in range(6, 9):
                for row in range(6, 9):
                    for col in range(6, 9):
                        if self.game[i][j].text() == self.game[row][col].text() and i != row and j != col and \
                                self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size :32 px; color: black; background-color :pink')
                            self.win = 0
        for i in range(9):
            for j in range(9):
                if self.game[i][j].text() == '':
                    self.win = 0

        if self.win == 1:
            msgBox = QMessageBox()
            msgBox.setText('Congratulation! You Win')
            msgBox.exec()

    def new_game(self):

        for i in range(9):
            for j in range(9):
                self.game[i][j].setText('')
                if self.dark == 1:
                    # self.game[i][j].setStyleSheet('color : white')
                    self.game[i][j].setStyleSheet('background color: dark gray ; color: white')
        try:
            r = random.randint(1, 6)
            #r = 7
            datapath = f"data/s{r}.txt"
            f = open(datapath, 'r')

        except:
            msgBox = QMessageBox()
            msgBox.setText('Ooops. Cannot open file or file not exist')
            msgBox.exec()

        bigtext = f.read()
        rows = bigtext.split('\n')
        for i in range(9):
            flag = 0
            s = rows[i].split(' ')
            for j in range(9):
                if s[j] != '0':
                    self.game[i][j].setStyleSheet('font-size : 32 ; color:black')
                    self.game[i][j].setText(s[j])
                    self.game[i][j].setReadOnly(True)

                else:
                    self.game[i][j].setStyleSheet('font-size : 32 ; color: blue')
                    self.game[i][j].setReadOnly(False)


app = QApplication([])
# app.setStyleSheet(qdarkgraystyle.load_stylesheet())
window = MainWindow()
app.exec()
