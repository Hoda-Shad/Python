from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from functools import partial
import random


class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.equal = None
        loader = QUiLoader()
        self.ui = loader.load('user.ui')
        self.ui.setWindowTitle('Tic Tac Toe')
        self.ui.show()
        self.player = 'X'

        self.game = [[self.ui.btn_1, self.ui.btn_2, self.ui.btn_3],
                     [self.ui.btn_4, self.ui.btn_5, self.ui.btn_6],
                     [self.ui.btn_7, self.ui.btn_8, self.ui.btn_9]]

        self.ui.btn_10.clicked.connect(self.initialize_new)
        self.ui.btn_13.clicked.connect(self.about)

        # self.ui.scoreboard.clicked.connect(self.update_score_board)
        # self.ui.lcd = QLCDNumber(self.score_1)
        # print(self.ui.lcd)

        for i in range(3):
            for j in range(3):
                self.game[i][j].setText('')
                self.game[i][j].clicked.connect(partial(self.play, i, j))
                self.game[i][j].setStyleSheet('color:black; background-color: rgb(220, 220, 220)')

    def about(self):
        msgBox = QMessageBox()
        msgBox.setText('TicTacToe is written by Hoda Shad! Enjoy😊')
        msgBox.exec()
        # self.about()


    def play(self, i, j):

        if self.game[i][j].text() == '':
            if self.player == 'X':
                self.game[i][j].setText('X')
                self.player = 'O'
                self.game[i][j].setStyleSheet('color:green; background-color:lightgreen')
            elif self.player == 'O':
                if self.ui.btn_12.isChecked():
                    i = random.randint(0, 2)
                    j = random.randint(0, 2)
                    if self.game[i][j].text() == '':
                        self.game[i][j].setText('O')
                        self.player = 'X'
                        self.game[i][j].setStyleSheet('color:lighblue; background-color:darkblue')
                elif self.ui.btn_11.isChecked():
                    if self.player == 'O':
                        self.game[i][j].setText('O')
                        self.player = 'X'
                        self.game[i][j].setStyleSheet('color:lighblue; background-color:darkblue')


        self.check()

    def check(self):

        for i in range(3):
            if self.game[i][0].text() == 'X' and self.game[i][1].text() == 'X' and self.game[i][2].text() == 'X':

                self.score_1 += 1
                msgBox = QMessageBox()
                msgBox.setText('Player 1 wins!')
                msgBox.exec()
                self.equal = 0

            if self.game[i][0].text() == 'O' and self.game[i][1].text() == 'O' and self.game[i][2].text() == 'O':
                self.score_2 += 1
                msgBox = QMessageBox()
                msgBox.setText('Player 2 wins!')
                msgBox.exec()
                self.equal = 0

            if self.game[0][i].text() == 'X' and self.game[1][i].text() == 'X' and self.game[2][i].text() == 'X':
                self.score_1 += 1
                msgBox = QMessageBox()
                msgBox.setText('Player 1 wins!')
                msgBox.exec()
                self.equal = 0

            if self.game[0][i].text() == 'O' and self.game[1][i].text() == 'O' and self.game[2][i].text() == 'O':
                self.score_2 += 1
                msgBox = QMessageBox()
                msgBox.setText('Player 2 wins!')
                msgBox.exec()
                self.equal = 0

        if (self.game[0][0].text() == 'X' and self.game[1][1].text() == 'X' and self.game[2][2].text() == 'X') or (
                self.game[2][0].text() == 'X' and self.game[0][2].text() == 'X' and self.game[1][1].text() == 'X'):
            self.score_1 += 1
            msgBox = QMessageBox()
            msgBox.setText('Player 1 wins!')
            msgBox.exec()
            self.equal = 0

        if (self.game[0][0].text() == 'O' and self.game[1][1].text() == 'O' and self.game[2][2].text() == 'O') or (
                self.game[2][0].text() == 'O' and self.game[0][2].text() == 'O' and self.game[1][1].text() == 'O'):
            self.score_2 += 1
            msgBox = QMessageBox()
            msgBox.setText('Player 2 wins!')
            msgBox.exec()
            self.equal = 0

        if self.equal == 1:
            msgBox = QMessageBox()
            msgBox.setText('Equal!')
            msgBox.exec()

        self.ui.btn_14.setText(f' Score of player1 \n{self.score_1}')
        self.ui.btn_15.setText(f' Score of player2 \n{self.score_2}')
    def initialize_new(self):
        for i in range(3):
            for j in range(3):
                self.game[i][j].setText('')
                self.game[i][j].setStyleSheet('color:black; background-color: rgb(220, 220, 220)')
        self.score_1 = 0
        self.score_2 = 0



app = QApplication([])
window = TicTacToe()
app.exec()
