import math

import PySide6
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from functools import partial

class HelloWorld(QMainWindow):
    def __init__(self):
        super().__init__()

        self.flag_sub = False
        self.flag_sum = False
        self.flag_div = False
        self.flag_mul = False
        self.flag_sumf = False

        loader = QUiLoader()
        self.ui = loader.load('user.ui', None)
        self.ui.show()
        self.ui.setWindowTitle('Calculator')
        self.btn_number_list = [self.ui.btn_0, self.ui.btn_1, self.ui.btn_2, self.ui.btn_3, self.ui.btn_4,
                                self.ui.btn_5, self.ui.btn_6, self.ui.btn_7, self.ui.btn_8, self.ui.btn_9]
        for i in range(10):
            self.btn_number_list[i].clicked.connect((partial(self.btn_numbers, i)))

        # self.ui.btn_0.clicked.connect(self.function_0)
        # self.ui.btn_1.clicked.connect(self.function_1)
        # self.ui.btn_2.clicked.connect(self.function_2)
        # self.ui.btn_3.clicked.connect(self.function_3)
        # self.ui.btn_4.clicked.connect(self.function_4)
        # self.ui.btn_5.clicked.connect(self.function_5)
        # self.ui.btn_6.clicked.connect(self.function_6)
        # self.ui.btn_7.clicked.connect(self.function_7)
        # self.ui.btn_8.clicked.connect(self.function_8)
        # self.ui.btn_9.clicked.connect(self.function_9)
        self.ui.btn_sum.clicked.connect(self.sum)
        self.ui.btn_mul.clicked.connect(self.mul)
        self.ui.btn_div.clicked.connect(self.div)
        self.ui.btn_sub.clicked.connect(self.sub)
        self.ui.btn_equal.clicked.connect(self.equal)
        self.ui.btn_clear.clicked.connect(self.clear)
        self.ui.btn_sin.clicked.connect(self.sin)
        self.ui.btn_cos.clicked.connect(self.cos)
        self.ui.btn_tan.clicked.connect(self.tan)
        self.ui.btn_cot.clicked.connect(self.cot)
        self.ui.btn_percent.clicked.connect(self.percent)
        self.ui.btn_plus_2.clicked.connect(self.plmi)
        self.ui.btn_dot.clicked.connect(self.dot)
        self.ui.btn_rev.clicked.connect(self.rev)
        self.ui.btn_factorial.clicked.connect(self.fact)
        self.ui.btn_log.clicked.connect(self.log)
        self.ui.btn_sqrt.clicked.connect(self.sqrt)

    def sqrt(self):

        self.num1 = int(self.ui.textbox.text())
        self.num1 = math.sqrt(self.num1)
        self.ui.textbox.setText(str(self.num1))


    def log(self):
        self.num1 = math.log(int(self.ui.textbox.text()))
        self.ui.textbox.setText(str(self.num1))

    def fact(self):
        self.num1 = math.factorial(int(self.ui.textbox.text()))
        self.ui.textbox.setText(str(self.num1))

    def rev(self):
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText(str(float(1 / self.num1)))

    def sum(self):
            self.num1 = float(self.ui.textbox.text())
            self.ui.textbox.setText('')
            self.flag_sum = True
    #
    # def sumf(self):
    #     self.num1 = int(self.ui.textbox.text())
    #     self.num1 = self.num1.split('.')
    #     self.ui.textbox.setText('')

    def sub(self):
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.flag_sub = True

    def div(self):
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.flag_div = True

    def mul(self):
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText('')
        self.flag_mul = True

    def sin(self):
        a = math.radians(float(self.ui.textbox.text()))
        self.ui.textbox.setText(str(math.sin(a)))

    def cos(self):
        a = math.radians(float(self.ui.textbox.text()))
        self.ui.textbox.setText(str(math.cos(a)))

    def tan(self):
        a = math.radians(float(self.ui.textbox.text()))
        self.ui.textbox.setText(str(math.tan(a)))

    def cot(self):
        a = math.radians(float(self.ui.textbox.text()))
        self.ui.textbox.setText(str(math.cot(a)))


    def percent(self):
        self.num1 = float(self.ui.textbox.text())
        self.num1 /= 100
        self.ui.textbox.setText(str(self.num1))

    def dot(self):
        for word in self.ui.textbox.text():
            if word == '.':
                break
            else:
                self.ui.textbox.setText(self.ui.textbox.text() + '.')

    def equal(self):
        self.num2 = float(self.ui.textbox.text())

        # if self.flag_sumf:
        #     self.num2 = self.num2.split('.')
        #     result = self.num1 [1] + self.num2 [1] + '.' + self.num1 [0] + self.num2 [0]
        #     self.ui.textbox.setText(str(result))

        if self.flag_sum:
            result = self.num1 + self.num2
            self.ui.textbox.setText(str(result))

        elif self.flag_sub:
            result = self.num1 - self.num2
            self.ui.textbox.setText(str(result))

        elif self.flag_div:
            result = self.num1 // self.num2
            self.ui.textbox.setText(str(result))

        elif self.flag_mul:
            result = self.num1 * self.num2
            self.ui.textbox.setText(str(result))

    def plmi(self):
            self.num1 = float(self.ui.textbox.text())
            self.num1 *= -1
            self.ui.textbox.setText(str(self.num1))

            # try:
            #     self.ui.textbox.setText(str(int(self.ui.textbox.text()) * -1))
            # except:
            #     try:
            #         self.ui.textbox.setText(str(float(self.ui.textbox.text()) * -1))
            #     except:
            #         pass

    def clear(self):
        self.ui.textbox.setText('')


    def btn_numbers(self, i):
        if self.ui.textbox.text() == '' or self.ui.textbox.text() == '0' :
            self.ui.textbox.setText(str(i))
        else:
            self.ui.textbox.setText(str(self.ui.textbox.text()) + str(i))



    # def function_1(self):
    #     self.ui.textbox.setText(self.ui.textbox.text() + '1')
    #
    # def function_2(self):
    #     self.ui.textbox.setText(self.ui.textbox.text() + '2')
    #
    # def function_3(self):
    #     self.ui.textbox.setText(self.ui.textbox.text() + '3')
    #
    # def function_4(self):
    #     self.ui.textbox.setText(self.ui.textbox.text() + '4')
    #
    # def function_5(self):
    #     self.ui.textbox.setText(self.ui.textbox.text() + '5')
    #
    # def function_6(self):
    #     self.ui.textbox.setText(self.ui.textbox.text() + '6')
    #
    # def function_7(self):
    #     self.ui.textbox.setText(self.ui.textbox.text() + '7')
    #
    # def function_8(self):
    #     self.ui.textbox.setText(self.ui.textbox.text() + '8')
    #
    # def function_9(self):
    #     self.ui.textbox.setText(self.ui.textbox.text() + '9')


app = QApplication([''])
window = HelloWorld()

app.exec()
