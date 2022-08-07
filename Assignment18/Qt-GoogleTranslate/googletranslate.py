from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *


class Translator(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('translate.ui', None)
        self.ui.show()

        self.words = []
        self.address = 'database.txt'
        self.load()

        self.ui.tra_btn.clicked.connect(self.txt_translate)

    def load(self):
        try:
            f = open(self.address, 'r')
            texts = f.read()
        except:
            print('Your file address is wrong.\nPlease check it.')

        f.close()

        list_of_texts = texts.strip().split('\n')

        for i in range(0, len(list_of_texts), 2):
            my_dict = {'english': list_of_texts[i], 'persian': list_of_texts[i + 1]}
            self.words.append(my_dict)



    def translate(self, model, word):
        if model == 1:  # english to persian
            for i in self.words:
                if i['english'] == word:
                    return i['persian']

        elif model == 2:  # persian to english
            for i in self.words:
                if i['persian'] == word:
                    return i['english']

        return False

    def english2persian(self, statement):
        words = statement.strip().split(' ')
        output = ''
        for word in words:
            if word == '':
                continue

            elif word == '.':
                output += ' '
                output += '.'

            elif word[0] == '.':
                word = word[1:]
                if self.translate(1, word) == False:
                    print(word, 'is not exist in Translate.txt')
                    output += ' '
                    output += word
                else:
                    output += ' '
                    output += '.'
                    output += self.translate(1, word)

            elif word[-1] == '.':
                word = word[:-1]
                if self.translate(1, word) == False:
                    print(word, 'is not exist in Translate.txt')
                    output += ' '
                    output += word
                else:
                    output += ' '
                    output += self.translate(1, word)
                    output += '.'

            elif '.' in word:
                for i in range(len(word)):
                    if word[i] == '.':
                        if self.translate(1, word[:i]) == False:
                            print(word[:i], 'is not exist in Translate.txt')
                            output += ' '
                            output += word[:i]
                        else:
                            output += ' '
                            output += self.translate(1, word[:i])

                        output += '.'

                        if self.translate(1, word[i + 1:]) == False:
                            print(word[i + 1:], 'is not exist in Translate.txt')
                            output += word[i + 1:]
                        else:
                            output += self.translate(1, word[i + 1:])

                        break

            else:
                if self.translate(1, word) == False:
                    print(word, 'is not exist in Translate.txt')
                    output += ' '
                    output += word
                else:
                    output += ' '
                    output += self.translate(1, word)

        return output.strip()

    def persian2english(self, statement):
        words = statement.strip().split(' ')
        output = ''
        for word in words:
            if word == '':
                continue

            elif word == '.':
                output += ' '
                output += '.'

            elif word[0] == '.':
                word = word[1:]
                if self.translate(2, word) == False:
                    print(word, 'is not exist in Translate.txt')
                    output += ' '
                    output += word
                else:
                    output += ' '
                    output += '.'
                    output += self.translate(2, word)

            elif word[-1] == '.':
                word = word[:-1]
                if self.translate(2, word) == False:
                    print(word, 'is not exist in Translate.txt')
                    output += ' '
                    output += word
                else:
                    output += ' '
                    output += self.translate(2, word)
                    output += '.'

            elif '.' in word:
                for i in range(len(word)):
                    if word[i] == '.':
                        if self.translate(2, word[:i]) == False:
                            print(word[:i], 'is not exist in Translate.txt')
                            output += ' '
                            output += word[:i]
                        else:
                            output += ' '
                            output += self.translate(2, word[:i])

                        output += '.'

                        if self.translate(2, word[i + 1:]) == False:
                            print(word[i + 1:], 'is not exist in Translate.txt')
                            output += word[i + 1:]
                        else:
                            output += self.translate(2, word[i + 1:])

                        break

            else:
                if self.translate(2, word) == False:
                    print(word, 'is not exist in Translate.txt')
                    output += ' '
                    output += word
                else:
                    output += ' '
                    output += self.translate(2, word)

        return output.strip()

    def txt_translate(self):
        if self.ui.combo_1.currentText() == 'English':
            self.ui.lineEdit_2.setText('')
            statement = self.ui.lineEdit.text()
            mean = self.english2persian(statement)
            self.ui.lineEdit_2.setText(mean)

        elif self.ui.combo_1.currentText() == 'Persian':
            self.ui.lineEdit_2.setText('')
            statement = self.ui.lineEdit.text()
            mean = self.persian2english(statement)
            self.ui.lineEdit_2.setText(mean)

        else:
            print('oops')


app = QApplication([])
window = Translator()
app.exec()