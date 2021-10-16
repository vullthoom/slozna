from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QFont
import sys

# основные цвета:
#08457e темный
#499EEC светлый

money = 273
waste = ''
wastes = []
BACKGROUND_COLOR = 'background-color: #08457e;'
TITILE_FONT = 'Eurofurence'
TITILE_FONT_SIZE = 23
SUBTITLE_FONT = 'Eurofurence'
SUBTITLE_FONT_SIZE = 15

class StyleButton:
    def baseButton():
        return '''
        QPushButton {
            background-color: #08457e;
            font-size: 25px;
            font-family: 'Eurofurence', sans-serif;
            color: #499EEC;
            border: 1px solid #499EEC;
            border-radius: 5px;
        }
        QPushButton:hover:pressed {
            background-color: #499EEC;
            color: #08457e;
            border: 1px solid #08457e;
        }
        '''

    def enterButton():
        return '''
        QPushButton {
            background-color: #499EEC;
            font-weight: 500;
            font-size: 40px;
            padding-top: 80px;
            color: #08457e;
            border: 1px solid #499EEC;
            border-radius: 5px;
        }
        QPushButton:hover:pressed {
            background-color: #08457e;
            color: #499EEC;
            border: 1px solid #499EEC;
        }
        '''

    def deleteButton():
        return '''
        QPushButton {
            background-color: #2B2B2B;
            font-size: 25px;
            padding-top: 5px;
            color: #499EEC;
            border: 1px solid #499EEC;
            border-radius: 5px;
        }
        QPushButton:hover:pressed {
            background-color: #499EEC;
            color: #2B2B2B;
            border: 1px solid #499EEC;
        }
        '''

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setup()


    def setup(self):
        self.resize(300, 400)
        self.setMinimumSize(300, 400)
        self.setMaximumSize(300, 400)
        self.setStyleSheet(BACKGROUND_COLOR)
        titile_font = QFont(TITILE_FONT, TITILE_FONT_SIZE, QFont.Weight.Bold)
        subtitle_font = QFont(SUBTITLE_FONT, SUBTITLE_FONT_SIZE, QFont.Weight.Normal)

        self.setWindowTitle('Survive')

        self.top_label = QLabel('На сегодня', self)
        self.top_label.setGeometry(0, 41, 300, 35)
        self.top_label.setFont(subtitle_font)
        self.top_label.setStyleSheet('color: #499EEC; padding-left: 10px; border-bottom: 1px solid #499EEC;')

        self.money_label = QLabel(f'{money}', self)
        self.money_label.setGeometry(0, 15, 300, 26)
        # self.money_label.setMargin(10)
        self.money_label.setFont(titile_font)
        self.money_label.setStyleSheet('color: #499EEC; padding-left: 15px;')

        self.waste_label = QLabel(f'Потрачено:\n{waste}', self)
        self.waste_label.setGeometry(0, 80, 300, 80)
        self.waste_label.setFont(titile_font)
        self.waste_label.setStyleSheet('color: #499EEC; padding-left: 10px;')
        
        self.zeroButton = QPushButton('0', self)
        self.zeroButton.setGeometry(1, 340, 151, 56)
        self.zeroButton.setStyleSheet(StyleButton.baseButton())
        self.zeroButton.clicked.connect(lambda: self.ButtonClick('0'))

        self.dotButton = QPushButton('.', self)
        self.dotButton.setGeometry(153, 340, 75, 56)
        self.dotButton.setStyleSheet(StyleButton.baseButton())
        self.dotButton.clicked.connect(lambda: self.ButtonClick('.'))

        self.enterButton = QPushButton('\uE751', self)
        self.enterButton.setGeometry(229, 226, 70, 170)
        self.enterButton.setStyleSheet(StyleButton.enterButton())
        self.enterButton.clicked.connect(lambda: self.ButtonClick('\uE751'))

        self.deleteButton = QPushButton('\uE750', self)
        self.deleteButton.setGeometry(229, 169, 70, 56)
        self.deleteButton.setStyleSheet(StyleButton.deleteButton())
        self.deleteButton.clicked.connect(lambda: self.ButtonClick('\uE750'))

        self.oneButton = QPushButton('1', self)
        self.oneButton.setGeometry(1, 283, 75, 56)
        self.oneButton.setStyleSheet(StyleButton.baseButton())
        self.oneButton.clicked.connect(lambda: self.ButtonClick('1'))

        self.twoButton = QPushButton('2', self)
        self.twoButton.setGeometry(77, 283, 75, 56)
        self.twoButton.setStyleSheet(StyleButton.baseButton())
        self.twoButton.clicked.connect(lambda: self.ButtonClick('2'))

        self.treeButton = QPushButton('3', self)
        self.treeButton.setGeometry(153, 283, 75, 56)
        self.treeButton.setStyleSheet(StyleButton.baseButton())
        self.treeButton.clicked.connect(lambda: self.ButtonClick('3'))

        self.fourButton = QPushButton("4", self)
        self.fourButton.setGeometry(1, 226, 75, 56)
        self.fourButton.setStyleSheet(StyleButton.baseButton())
        self.fourButton.clicked.connect(lambda: self.ButtonClick('4'))

        self.fiveButton = QPushButton("5", self)
        self.fiveButton.setGeometry(77, 226, 75, 56)
        self.fiveButton.setStyleSheet(StyleButton.baseButton())
        self.fiveButton.clicked.connect(lambda: self.ButtonClick('5'))

        self.sixButton = QPushButton("6", self)
        self.sixButton.setGeometry(153, 226, 75, 56)
        self.sixButton.setStyleSheet(StyleButton.baseButton())
        self.sixButton.clicked.connect(lambda: self.ButtonClick('6'))

        self.sevenButton = QPushButton("7", self)
        self.sevenButton.setGeometry(1, 169, 75, 56)
        self.sevenButton.setStyleSheet(StyleButton.baseButton())
        self.sevenButton.clicked.connect(lambda: self.ButtonClick('7'))

        self.eightButton = QPushButton("8", self)
        self.eightButton.setGeometry(77, 169, 75, 56)
        self.eightButton.setStyleSheet(StyleButton.baseButton())
        self.eightButton.clicked.connect(lambda: self.ButtonClick('8'))

        self.nineButton = QPushButton("9", self)
        self.nineButton.setGeometry(153, 169, 75, 56)
        self.nineButton.setStyleSheet(StyleButton.baseButton())
        self.nineButton.clicked.connect(lambda: self.ButtonClick('9'))

    def ButtonClick(self, char):
        global waste
        global money
        if char == '\uE750':
            waste = waste[:-1]
        elif char == '\uE751':
            wastes.append(float(waste))
            money -= float(waste)
            waste = ''
            self.money_label.setText(f'{money}')
        else:
            waste += char
        self.waste_label.setText(f'Потрачено:\n{waste}')
        



app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())