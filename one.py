from PyQt5.QtWidgets import QApplication, QLineEdit, QListWidgetItem, QStyle, QWidget, QLabel, QPushButton, QSpinBox, QListWidget
from PyQt5.QtGui import QIcon, QKeyEvent
from PyQt5.QtCore import QPoint, QSize, QEvent
import sys
import os
from styles import BACKGROUND_COLOR, TITLE_FONT, SUBTITLE_FONT, StyleButton
from datetime import date
from settings import save_data, use_data, clear_all, clear_moneys_and_budgets, clear_wastes_history
import settings as s

# основные цвета:
#08457e темный
#499EEC светлый

wind = True

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        use_data()
        self.setup()
        self.open_and_update_app()


    def setup(self):
# Настройки окна
        self.setWindowTitle('Survive')
        self.setWindowIcon(QIcon(os.path.dirname(__file__) + '/icons/app_icon.png'))
        self.setFixedSize(600, 397)
        self.setStyleSheet(BACKGROUND_COLOR)

# Главное окно:
    # Label:
        self.money_label = QLabel(f'{s.money}', self)
        self.money_label.setGeometry(0, 15, 270, 26)
        self.money_label.setFont(TITLE_FONT)
        self.money_label.setStyleSheet('color: #499EEC; padding-left: 10px;')

        self.top_label = QLabel('На сегодня', self)
        self.top_label.setGeometry(0, 41, 300, 35)
        self.top_label.setFont(SUBTITLE_FONT)
        self.top_label.setStyleSheet('color: #499EEC; padding-left: 10px; border-bottom: 1px solid #499EEC;')

        self.waste_label = QLabel(f'Потрачено:\n{s.waste}', self)
        self.waste_label.setGeometry(0, 80, 300, 80)
        self.waste_label.setFont(TITLE_FONT)
        self.waste_label.setStyleSheet('color: #499EEC; padding-left: 5px;')
        
    # Кнопки:
        # Точка
        self.dotButton = QPushButton('.', self)
        self.dotButton.setGeometry(153, 340, 75, 56)
        self.dotButton.setStyleSheet(StyleButton.baseButton())
        self.dotButton.clicked.connect(lambda: self.buttonClick('.'))

        # Ноль
        self.zeroButton = QPushButton('0', self)
        self.zeroButton.setGeometry(1, 340, 151, 56)
        self.zeroButton.setStyleSheet(StyleButton.baseButton())
        self.zeroButton.clicked.connect(lambda: self.buttonClick('0'))

        # Один
        self.oneButton = QPushButton('1', self)
        self.oneButton.setGeometry(1, 283, 75, 56)
        self.oneButton.setStyleSheet(StyleButton.baseButton())
        self.oneButton.clicked.connect(lambda: self.buttonClick('1'))

        # Два
        self.twoButton = QPushButton('2', self)
        self.twoButton.setGeometry(77, 283, 75, 56)
        self.twoButton.setStyleSheet(StyleButton.baseButton())
        self.twoButton.clicked.connect(lambda: self.buttonClick('2'))

        # Три
        self.treeButton = QPushButton('3', self)
        self.treeButton.setGeometry(153, 283, 75, 56)
        self.treeButton.setStyleSheet(StyleButton.baseButton())
        self.treeButton.clicked.connect(lambda: self.buttonClick('3'))

        # Четыре
        self.fourButton = QPushButton("4", self)
        self.fourButton.setGeometry(1, 226, 75, 56)
        self.fourButton.setStyleSheet(StyleButton.baseButton())
        self.fourButton.clicked.connect(lambda: self.buttonClick('4'))

        # Пять
        self.fiveButton = QPushButton("5", self)
        self.fiveButton.setGeometry(77, 226, 75, 56)
        self.fiveButton.setStyleSheet(StyleButton.baseButton())
        self.fiveButton.clicked.connect(lambda: self.buttonClick('5'))

        # Шесть
        self.sixButton = QPushButton("6", self)
        self.sixButton.setGeometry(153, 226, 75, 56)
        self.sixButton.setStyleSheet(StyleButton.baseButton())
        self.sixButton.clicked.connect(lambda: self.buttonClick('6'))

        # Семь
        self.sevenButton = QPushButton("7", self)
        self.sevenButton.setGeometry(1, 169, 75, 56)
        self.sevenButton.setStyleSheet(StyleButton.baseButton())
        self.sevenButton.clicked.connect(lambda: self.buttonClick('7'))

        # Восемь
        self.eightButton = QPushButton("8", self)
        self.eightButton.setGeometry(77, 169, 75, 56)
        self.eightButton.setStyleSheet(StyleButton.baseButton())
        self.eightButton.clicked.connect(lambda: self.buttonClick('8'))

        # Девять
        self.nineButton = QPushButton("9", self)
        self.nineButton.setGeometry(153, 169, 75, 56)
        self.nineButton.setStyleSheet(StyleButton.baseButton())
        self.nineButton.clicked.connect(lambda: self.buttonClick('9'))

        # Enter
        self.enterButton = QPushButton('\uE751', self)
        self.enterButton.setGeometry(229, 226, 70, 170)
        self.enterButton.setStyleSheet(StyleButton.enterButton())
        self.enterButton.clicked.connect(lambda: self.buttonClick('\uE751'))

        # Delete
        self.deleteButton = QPushButton('\uE750', self)
        self.deleteButton.setGeometry(229, 169, 70, 56)
        self.deleteButton.setStyleSheet(StyleButton.deleteButton())
        self.deleteButton.clicked.connect(lambda: self.buttonClick('\uE750'))

        # Настройки(\uE115)
        self.settingsButton = QPushButton('', self)
        self.settingsButton.setGeometry(270, 0, 30, 30)
        self.settingsButton.setIcon(QIcon(os.path.dirname(__file__) + '/icons/settings.png'))
        self.settingsButton.setIconSize(QSize(25, 25))
        self.settingsButton.setStyleSheet(StyleButton.settings())
        self.settingsButton.clicked.connect(self.settingsClick)
        self.settingsButton.pressed.connect(self.settings_press_icon)


# Второе окно:
    # Бюджет
        self.budget_label = QLabel('Бюджет', self)
        self.budget_label.setGeometry(95, 15, 120, 30)
        self.budget_label.setFont(TITLE_FONT)
        self.budget_label.setStyleSheet('color: #499EEC;')

        self.budget_edit = QLineEdit(f'{s.budget}', self)
        self.budget_edit.setGeometry(10, 55, 280, 40)
        self.budget_edit.setFont(TITLE_FONT)
        self.budget_edit.setStyleSheet('color: #499EEC; border: 1px solid #499EEC; font-size: 40px;')
        self.budget_edit.textChanged.connect(self.budget_change)

        # self.budget_edit = QLabel(f'{s.budget}', self)
        # self.budget_edit.setGeometry(10, 55, 280, 40)
        # self.budget_edit.setFont(TITLE_FONT)
        # self.budget_edit.setStyleSheet('color: #499EEC; border: 1px solid #499EEC; font-size: 40px;')

    # Дни    
        self.day_label = QLabel('Дней:', self)
        self.day_label.setGeometry(75, 115, 95, 30)
        self.day_label.setFont(TITLE_FONT)
        self.day_label.setStyleSheet('color: #499EEC;')

        self.day_spin = QSpinBox(self)
        self.day_spin.setGeometry(170, 115, 55, 30)
        self.day_spin.setRange(1, 31)
        self.day_spin.setFont(TITLE_FONT)
        self.day_spin.setStyleSheet(StyleButton.day_spin_style())
        self.day_spin.valueChanged.connect(self.day_change)

    # Кнопки:
        # Назад(\uF71A)
        self.backButton = QPushButton('',self)
        self.backButton.setGeometry(10, 10, 30, 30)
        self.backButton.setIcon(QIcon(os.path.dirname(__file__) + '/icons/back.png'))
        self.backButton.setIconSize(QSize(30, 30))
        self.backButton.setStyleSheet(StyleButton.apply_and_back())
        self.backButton.clicked.connect(self.backClick)
        self.backButton.pressed.connect(self.back_press_icon)

        # Подтвердить(\uE8FB) 
        self.applyButton = QPushButton('', self)
        self.applyButton.setGeometry(260, 10, 30, 30)
        self.applyButton.setIcon(QIcon(os.path.dirname(__file__) + '/icons/apply.png'))
        self.applyButton.setIconSize(QSize(30, 30))
        self.applyButton.setStyleSheet(StyleButton.apply_and_back())
        self.applyButton.clicked.connect(clear_all)
        self.applyButton.pressed.connect(self.apply_press_icon)

        self.budget_label.hide()
        self.budget_edit.hide()
        self.day_label.hide()
        self.day_spin.hide()
        self.backButton.hide()
        self.applyButton.hide()
        




# Боковое окно:
    # История трат
        self.history_waste = QLabel('История трат', self)
        self.history_waste.setGeometry(360, 10, 200, 30)
        self.history_waste.setFont(TITLE_FONT)
        self.history_waste.setStyleSheet('color: #499EEC;')

        self.listwidget = QListWidget(self)
        self.listwidget.setGeometry(310, 50, 280, 340)
        self.listwidget.setFont(SUBTITLE_FONT)
        self.listwidget.setStyleSheet('color: #499EEC; border: 1px solid #499EEC;')
        # self.listwidget.setStyleSheet(StyleButton.list_widget())

    # История бюджета
        self.history_budget = QLabel('История', self)
        self.history_budget.setGeometry(395, 10, 200, 30)
        self.history_budget.setFont(TITLE_FONT)
        self.history_budget.setStyleSheet('color: #499EEC;')
        self.history_budget.hide()

    # Кнопки
        # Очистить последнее
        self.clear_last = QPushButton('',self)
        self.clear_last.setGeometry(310, 10, 30, 30)
        self.clear_last.setIcon(QIcon(os.path.dirname(__file__) + '/icons/last_clear.png'))
        self.clear_last.setIconSize(QSize(30, 30))
        self.clear_last.setStyleSheet(StyleButton.apply_and_back())
        self.clear_last.clicked.connect(self.clear_lastClick)
        self.clear_last.pressed.connect(self.clear_last_icon)
        self.clear_last.setToolTip('Удалить последнее')

        # ПОчистить все
        self.clear_all = QPushButton('', self)
        self.clear_all.setGeometry(560, 10, 30, 30)
        self.clear_all.setIcon(QIcon(os.path.dirname(__file__) + '/icons/all_clear.png'))
        self.clear_all.setIconSize(QSize(30, 30))
        self.clear_all.setStyleSheet(StyleButton.apply_and_back())
        self.clear_all.clicked.connect(self.clear_allClick)
        self.clear_all.pressed.connect(self.clear_all_icon)
        self.clear_all.setToolTip('Очистить историю')





# Разделитель
        self.line = QLabel('', self)
        self.line.setGeometry(300, 0, 1, 169)
        self.line.setStyleSheet('border: 1px solid #499EEC')


# Функции:
    # Иконки:
    def settings_press_icon(self):
        self.settingsButton.setIcon(QIcon(os.path.dirname(__file__) + '/icons/settings1.png'))
    
    def back_press_icon(self):
        self.backButton.setIcon(QIcon(os.path.dirname(__file__) + '/icons/back1.png'))

    def apply_press_icon(self):
        self.applyButton.setIcon(QIcon(os.path.dirname(__file__) + '/icons/apply1.png'))

    def clear_all_icon(self):
        self.clear_all.setIcon(QIcon(os.path.dirname(__file__) + '/icons/all_clear1.png'))

    def clear_last_icon(self):
        self.clear_last.setIcon(QIcon(os.path.dirname(__file__) + '/icons/last_clear1.png'))


    # Кнопки:

    def keyPressEvent(self, event):
        global wind
        print(event.key(), wind)
        if 48 <= event.key() <=57:
            # цифра
            self.buttonClick(chr(event.key()))
        elif event.key() == 46:
            # точка
            self.buttonClick('.')
        elif event.key() == 16777219:
            # delete
            self.buttonClick('\uE750')
        elif event.key() == 16777220 or event.key() == 16777221:
            # enter
            self.buttonClick('\uE751')
        elif event.key() == 16777216:
            # esc
            self.backClick()


    def buttonClick(self, char):
        global wind
        if wind:
            if char == '\uE750':
                s.waste = s.waste[:-1]
            elif char == '\uE751':
                try:
                    s.waste = float(s.waste)
                    if float(s.waste) > 0:
                        s.wastes.append({f'{date.today()}': round(s.waste, 2)})
                        s.money -= float(s.waste)
                        self.listwidget.insertItem(0, f'{str(s.wastes[-1].items())[14:24]}:{str(s.wastes[-1].items())[26:-3]}')
                        self.money_label.setText(f'{round(s.money, 2)}')
                        save_data()
                    else:
                        pass
                except (ValueError, TypeError):
                    pass
                finally:
                    s.waste = ''
            else:
                s.waste += char
            self.waste_label.setText(f'Потрачено:\n{s.waste}')
        else:
            if char == '\uE750':
                s.budget = s.budget[:-1]
            elif char == '\uE751':
                self.applyClick()
            else:
                s.budget += char
            self.budget_edit.setText(f'{s.budget}')

    def settingsClick(self):
        global wind
        wind = False
        self.settingsButton.setIcon(QIcon(os.path.dirname(__file__) + '/icons/settings.png'))
        self.changeover()
        self.listwidget.clear()
        for i in s.budgets:
            self.listwidget.insertItem(0, i)
        

    def backClick(self):
        global wind
        wind = True
        self.backButton.setIcon(QIcon(os.path.dirname(__file__) + '/icons/back.png'))
        s.budget = ''
        self.budget_edit.setText('')
        s.day = 1
        self.day_spin.setValue(1)
        self.changeover_back()
        self.listwidget.clear()
        for i in s.wastes:
            was = f'{str(i.items())[14:24]}:{str(i.items())[26:-3]}'
            self.listwidget.insertItem(0, was)

            

    def applyClick(self):
        try:
            s.budget = float(s.budget)     
            s.money = round((s.budget / s.day), 2)
            self.money_label.setText(f'{round(s.money, 2)}')
            s.moneys = s.money
            s.days = str(s.day)
            if int(s.days[-1]) == 1:
                s.budgets.append(f'{date.today()}: Бюджет {s.budget} на {s.days} день')
            elif 4 >= int(s.days[-1]) >= 2:
                s.budgets.append(f'{date.today()}: Бюджет {s.budget} на {s.days} дня')
            else:
                s.budgets.append(f'{date.today()}: Бюджет {s.budget} на {s.days} дней')
            self.listwidget.insertItem(0, s.budgets[-1])
            save_data()
        except ValueError:
            error1.show()
        finally:
            self.applyButton.setIcon(QIcon(os.path.dirname(__file__) + '/icons/apply.png'))
            s.budget = ''
            self.budget_edit.setText('')
            s.day = 1
            self.day_spin.setValue(1)
    

    def clear_lastClick(self):
        global wind
        self.clear_last.setIcon(QIcon(os.path.dirname(__file__) + '/icons/last_clear.png'))
        if wind:
            s.wastes.pop()
            self.listwidget.clear()
            for i in s.wastes:
                was = f'{str(i.items())[14:24]}:{str(i.items())[26:-3]}'
                self.listwidget.insertItem(0, was)
        else:
            s.budgets.pop()
            self.listwidget2.clear()
            for i in s.budgets:
                self.listwidget.insertItem(0, i)
        save_data()




    def clear_allClick(self):
        global wind
        self.clear_all.setIcon(QIcon(os.path.dirname(__file__) + '/icons/all_clear.png'))
        if wind:
            clear_wastes_history()
            self.listwidget.clear()
        else:
            clear_moneys_and_budgets()
            self.listwidget.clear()
        save_data()


    # Интерактивные элементы:
    def day_change(self):
        s.day = self.day_spin.value()

    def budget_change(self):
        s.budget = self.budget_edit.text()

    def open_and_update_app(self):
        if len(s.history) == 0:
            s.history.append(f'{date.today()}')
        else:
            if s.history[-1] != f'{date.today()}':
                s.days -= 1
                s.money += s.moneys
                self.money_label.setText(f'{round(s.money, 2)}')
                s.history.append(f'{date.today()}')
                save_data()
            else:
                pass
        if len(s.wastes) > 0:
            for i in s.wastes:
                was = f'{str(i.items())[14:24]}:{str(i.items())[26:-3]}'
                self.listwidget.insertItem(0, was)
        else:
            pass


    def changeover(self):
        self.settingsButton.hide()
        self.money_label.hide()
        self.waste_label.hide()
        self.top_label.hide()
        self.history_waste.hide()

        self.budget_label.show()
        self.day_label.show()
        self.day_spin.show()
        self.backButton.show()
        self.applyButton.show()
        self.history_budget.show()
        self.budget_edit.show()
        self.budget_edit.setFocus()

    def changeover_back(self):
        self.settingsButton.show()
        self.money_label.show()
        self.top_label.show()
        self.history_waste.show()
        self.waste_label.show()
        self.waste_label.setFocus()

        self.budget_label.hide()
        self.budget_edit.hide()
        self.day_label.hide()
        self.day_spin.hide()
        self.backButton.hide()
        self.applyButton.hide()
        self.history_budget.hide()


class ErrorWimdow(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setWindowTitle('Error')
        self.setWindowIcon(QIcon(os.path.dirname(__file__) + '/icons/error.png'))
        self.setFixedSize(300, 150)
        self.setStyleSheet(BACKGROUND_COLOR)

        self.error = QLabel('Неверный символ', self)
        self.error.setGeometry(35, 0, 300, 150)
        self.error.setFont(TITLE_FONT)
        self.error.setStyleSheet('color: #499EEC;')

        self.show()






app = QApplication(sys.argv)
window = MainWindow()
error1 = ErrorWimdow()
window.show()
error1.show()
error1.hide()
sys.exit(app.exec())