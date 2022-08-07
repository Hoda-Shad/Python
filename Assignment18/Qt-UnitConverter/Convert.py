from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('conver.ui')
        self.ui.setWindowTitle('Converter')
        self.ui.show()
        # self.ui.cal_btn.clicked.connect(self.output)
        self.ui.maincombo.currentTextChanged.connect(self.unitChange)
        self.From = self.ui.comfrom.currentText()
        self.To = self.ui.comto.currentText()
        self.ui.cal_btn.clicked.connect(self.unit_converter)
        self.ui.maincombo.addItems(['Temperature', 'Weight', 'Digital Storage', 'Lenght'])


    def unitChange(self):
        self.ui.comfrom.clear()
        self.ui.comto.clear()
        # print(self.ui.maincombo.currentText())
        # if self.ui.maincombo.currentText() == 'None':
        #     self.ui.comfrom.clear()
        #     self.ui.comto.clear()

        if self.ui.maincombo.currentText() == 'Temperature':
            self.ui.comfrom.addItems(['°C', '°F', '°K'])
            self.ui.comto.addItems(['°C', '°F', '°K'])

        elif self.ui.maincombo.currentText() == 'Weight':
            self.ui.comfrom.addItems(['g', 'kg', 'T', 'P'])
            self.ui.comto.addItems(['g', 'kg', 'T', 'P'])

        elif self.ui.maincombo.currentText() == 'Digital Storage':
            self.ui.comfrom.addItems(['byte', 'bit', 'KByte', 'MByte', 'GByte', 'TByte'])
            self.ui.comto.addItems(['byte', 'bit', 'KByte', 'MByte', 'GByte', 'TByte'])


        elif self.ui.maincombo.currentText() == 'Lenght':
            self.ui.comfrom.addItems(['mm', 'cm', 'm', 'km', 'in'])
            self.ui.comto.addItems(['mm', 'cm', 'm', 'km', 'in'])

        # current_unit =self.ui.comfrom .currentText()
        # desired_unit = self.ui.comto.currentText()
        # quantity = self.ui.LineEdit_2

    def unit_converter(self):
        if self.ui.lineEdit_2.text() == '':
            msgBox = QMessageBox()
            msgBox.setText('Please Enter Input')
            msgBox.exec()
        else:
            if self.ui.maincombo.currentText() == 'Lenght':

                SI = {'mm': 0.001, 'cm': 0.01, 'm': 1.0, 'km': 1000., 'in': 0.17}
                num = int(self.ui.lineEdit_2.text()) * SI[self.ui.comfrom.currentText()] / SI[self.ui.comto.currentText()]
                self.ui.lineEdit_4.setText(str(num))

            elif self.ui.maincombo.currentText() == 'Weight':
                print('t')
                SI = {'kg':1000, 'g': 1.0, 'T': 1000000, 'P': 453}
                num = int(self.ui.lineEdit_2.text()) * SI[self.ui.comfrom.currentText()] / SI[self.ui.comto.currentText()]
                self.ui.lineEdit_4.setText(str(num))

            elif self.ui.maincombo.currentText() == 'Digital Storage':
                SI = {'byte': 1, 'bit': 0.125 , 'KByte': 1000, 'MByte': 1000000,'GByte':1000000000, 'TByte':1000000000000}
                num = int(self.ui.lineEdit_2.text()) * SI[self.ui.comfrom.currentText()] / SI[self.ui.comto.currentText()]
                self.ui.lineEdit_4.setText(str(num))

            elif self.ui.maincombo.currentText() == 'Temperature':
                SI = { '°C':1, '°F':-17.22, '°K':-272.15}
                num = int(self.ui.lineEdit_2.text()) * SI[self.ui.comfrom.currentText()] / SI[self.ui.comto.currentText()]
                self.ui.lineEdit_4.setText(str(num))



app = QApplication([])
window = MainWindow()
app.exec()
