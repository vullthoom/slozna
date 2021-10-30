from PyQt5.QtWidgets import QApplication, QLineEdit, QStyle, QWidget, QLabel, QPushButton, QSpinBox, QListWidget
from PyQt5.QtGui import QIcon, QKeyEvent
from PyQt5.QtCore import QPoint, QSize, QEvent
import sys
import os
from styles import BACKGROUND_COLOR, TITLE_FONT, SUBTITLE_FONT, StyleButton
from datetime import date

# основные цвета:
#08457e темный
#499EEC светлый
# формат изображений svg
# QSpinBox QPushButton {...}

budget = ''
day = 1
money = ''
waste = ''
wastes = []

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setup()


    def setup(self):
        self.resize(300, 400)
        self.setFixedSize(300, 400)
        self.setStyleSheet(BACKGROUND_COLOR)

        self.setWindowTitle('Survive')
        self.setWindowIcon(QIcon(os.path.dirname(__file__) + '/icons/app_icon.png'))
        

        self.top_label = QLabel('На сегодня', self)
        self.top_label.setGeometry(0, 41, 300, 35)
        self.top_label.setFont(SUBTITLE_FONT)
        self.top_label.setStyleSheet('color: #499EEC; padding-left: 10px; border-bottom: 1px solid #499EEC;')

        self.money_label = QLabel(f'{money}', self)
        self.money_label.setGeometry(0, 15, 300, 26)
        # self.money_label.setMargin(10)
        self.money_label.setFont(TITLE_FONT)
        self.money_label.setStyleSheet('color: #499EEC; padding-left: 15px;')

        self.waste_label = QLabel(f'Потрачено:\n{waste}', self)
        self.waste_label.setGeometry(0, 80, 300, 80)
        self.waste_label.setFont(TITLE_FONT)
        self.waste_label.setStyleSheet('color: #499EEC; padding-left: 5px;')
        
        self.zeroButton = QPushButton('0', self)
        self.zeroButton.setGeometry(1, 340, 151, 56)
        self.zeroButton.setStyleSheet(StyleButton.baseButton())
        self.zeroButton.clicked.connect(lambda: self.buttonClick('0'))

        self.dotButton = QPushButton('.', self)
        self.dotButton.setGeometry(153, 340, 75, 56)
        self.dotButton.setStyleSheet(StyleButton.baseButton())
        self.dotButton.clicked.connect(lambda: self.buttonClick('.'))

        self.enterButton = QPushButton('\uE751', self)
        self.enterButton.setGeometry(229, 226, 70, 170)
        self.enterButton.setStyleSheet(StyleButton.enterButton())
        self.enterButton.clicked.connect(lambda: self.buttonClick('\uE751'))

        self.deleteButton = QPushButton('\uE750', self)
        self.deleteButton.setGeometry(229, 169, 70, 56)
        self.deleteButton.setStyleSheet(StyleButton.deleteButton())
        self.deleteButton.clicked.connect(lambda: self.buttonClick('\uE750'))

        self.oneButton = QPushButton('1', self)
        self.oneButton.setGeometry(1, 283, 75, 56)
        self.oneButton.setStyleSheet(StyleButton.baseButton())
        self.oneButton.clicked.connect(lambda: self.buttonClick('1'))

        self.twoButton = QPushButton('2', self)
        self.twoButton.setGeometry(77, 283, 75, 56)
        self.twoButton.setStyleSheet(StyleButton.baseButton())
        self.twoButton.clicked.connect(lambda: self.buttonClick('2'))

        self.treeButton = QPushButton('3', self)
        self.treeButton.setGeometry(153, 283, 75, 56)
        self.treeButton.setStyleSheet(StyleButton.baseButton())
        self.treeButton.clicked.connect(lambda: self.buttonClick('3'))

        self.fourButton = QPushButton("4", self)
        self.fourButton.setGeometry(1, 226, 75, 56)
        self.fourButton.setStyleSheet(StyleButton.baseButton())
        self.fourButton.clicked.connect(lambda: self.buttonClick('4'))

        self.fiveButton = QPushButton("5", self)
        self.fiveButton.setGeometry(77, 226, 75, 56)
        self.fiveButton.setStyleSheet(StyleButton.baseButton())
        self.fiveButton.clicked.connect(lambda: self.buttonClick('5'))

        self.sixButton = QPushButton("6", self)
        self.sixButton.setGeometry(153, 226, 75, 56)
        self.sixButton.setStyleSheet(StyleButton.baseButton())
        self.sixButton.clicked.connect(lambda: self.buttonClick('6'))

        self.sevenButton = QPushButton("7", self)
        self.sevenButton.setGeometry(1, 169, 75, 56)
        self.sevenButton.setStyleSheet(StyleButton.baseButton())
        self.sevenButton.clicked.connect(lambda: self.buttonClick('7'))

        self.eightButton = QPushButton("8", self)
        self.eightButton.setGeometry(77, 169, 75, 56)
        self.eightButton.setStyleSheet(StyleButton.baseButton())
        self.eightButton.clicked.connect(lambda: self.buttonClick('8'))

        self.nineButton = QPushButton("9", self)
        self.nineButton.setGeometry(153, 169, 75, 56)
        self.nineButton.setStyleSheet(StyleButton.baseButton())
        self.nineButton.clicked.connect(lambda: self.buttonClick('9'))
        # self.nineButton.keyPressEvent(QKeyEvent(QEvent.KeyPress, 9))
# \uE115
        self.settingsButton = QPushButton('', self)
        self.settingsButton.setGeometry(270, 0, 30, 30)
        self.settingsButton.setIcon(QIcon(os.path.dirname(__file__) + '/icons/settings.png'))
        self.settingsButton.setIconSize(QSize(25, 25))
        self.settingsButton.setStyleSheet(StyleButton.settings())
        self.settingsButton.clicked.connect(self.settingsClick)
        self.settingsButton.pressed.connect(self.settings_press_icon)




        self.budget_label = QLabel('Бюджет', self)
        self.budget_label.setGeometry(395, 15, 120, 30)
        self.budget_label.setFont(TITLE_FONT)
        self.budget_label.setStyleSheet('color: #499EEC;')

        self.budget_edit = QLineEdit(f'{budget}', self)
        self.budget_edit.setGeometry(310, 55, 280, 40)
        self.budget_edit.setFont(TITLE_FONT)
        self.budget_edit.setStyleSheet('color: #499EEC; border: 1px solid #499EEC; font-size: 40px;')
        self.budget_edit.textChanged.connect(self.budget_change)

        
        self.day_label = QLabel('Дней:', self)
        self.day_label.setGeometry(375, 105, 95, 30)
        self.day_label.setFont(TITLE_FONT)
        self.day_label.setStyleSheet('color: #499EEC;')

        self.day_spin = QSpinBox(self)
        self.day_spin.setGeometry(470, 105, 55, 30)
        self.day_spin.setRange(1, 31)
        self.day_spin.setFont(TITLE_FONT)
        self.day_spin.setStyleSheet(StyleButton.day_spin_style())
        self.day_spin.valueChanged.connect(self.day_change)
        
# \uF71A
        self.backButton = QPushButton('',self)
        self.backButton.setGeometry(310, 10, 30, 30)
        self.backButton.setIcon(QIcon(os.path.dirname(__file__) + '/icons/back.png'))
        self.backButton.setIconSize(QSize(30, 30))
        self.backButton.setStyleSheet(StyleButton.apply_back())
        self.backButton.clicked.connect(self.backClick)
        self.backButton.pressed.connect(self.back_press_icon)

# \uE8FB
        self.applyButton = QPushButton('', self)
        self.applyButton.setGeometry(560, 10, 30, 30)
        self.applyButton.setIcon(QIcon(os.path.dirname(__file__) + '/icons/apply.png'))
        self.applyButton.setIconSize(QSize(30, 30))
        self.applyButton.setStyleSheet(StyleButton.apply_back())
        self.applyButton.clicked.connect(self.applyClick)
        self.applyButton.pressed.connect(self.apply_press_icon)

        self.listwidget = QListWidget(self)
        self.listwidget.setGeometry(310, 140, 280, 250)
        self.listwidget.setFont(SUBTITLE_FONT)
        self.listwidget.setStyleSheet('color: #499EEC; border: 1px solid #499EEC;')
        # self.listwidget.itemChanged(wastes)


        self.line = QLabel('', self)
        self.line.setGeometry(300, 0, 1, 400)
        self.line.setStyleSheet('border: 1px solid #499EEC')


    def settings_press_icon(self):
        self.settingsButton.setIcon(QIcon(os.path.dirname(__file__) + '/icons/settings1.png'))
        

    def buttonClick(self, char):
        global waste
        global money
        if char == '\uE750':
            waste = waste[:-1]
        elif char == '\uE751':
            try:
                if waste > 0:
                    wastes.append(f'{date.today()} : {round(float(waste))}')
                    money -= float(waste)
                    self.listwidget.insertItem(0, wastes[-1])
                    self.money_label.setText(f'{round(money, 2)}')
                else:
                    pass
            except (ValueError, TypeError):
                pass
            finally:
                waste = ''
        else:
            waste += char
        self.waste_label.setText(f'Потрачено:\n{waste}')

    def settingsClick(self):
        self.settingsButton.setIcon(QIcon(os.path.dirname(__file__) + '/icons/settings.png'))
        self.setFixedSize(600, 400)
        self.settingsButton.hide()

    def back_press_icon(self):
        self.backButton.setIcon(QIcon(os.path.dirname(__file__) + '/icons/back1.png'))

    def apply_press_icon(self):
        self.applyButton.setIcon(QIcon(os.path.dirname(__file__) + '/icons/apply1.png'))

    def day_change(self):
        global day
        day = self.day_spin.value()

    def budget_change(self):
        global budget
        budget = self.budget_edit.text()

    def backClick(self):
        self.backButton.setIcon(QIcon(os.path.dirname(__file__) + '/icons/back.png'))
        global budget
        global day
        budget = ''
        day = 1
        self.setFixedSize(300, 400)
        self.settingsButton.show()

    def applyClick(self):
        global budget
        global money
        global day
        try:
            budget = float(budget)            
            money = budget / day
            budget = ''
            day = 1
            self.money_label.setText(f'{round(money, 2)}')
            self.setFixedSize(300, 400)
            self.settingsButton.show()
        except ValueError:
            self.budget_edit.setText('Ошибка ввода')
            self.budget_edit.selectAll()
        finally:
            self.applyButton.setIcon(QIcon(os.path.dirname(__file__) + '/icons/apply.png'))

    def keyPressEvent(self, event):
        if 48 <= event.key() <=57:
            # цифра
            self.buttonClick(chr(event.key()))
        elif event.key() == 46:
            # точка
            self.buttonClick('.')
        elif event.key() == 16777219:
            # delete
            self.buttonClick('\uE750')
        elif event.key() == 16777220:
            # enter
            self.buttonClick('\uE751')


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())