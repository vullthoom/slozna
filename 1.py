# a = [1, 1, True, False, 'True', False, [12, 3], [12, 3]]
# c = 0
# b = a.copy()

# for i in a:
#     b.remove(i)
#     for z in b:
#         if i is z:
#             c = c + 1
# d = len(a) - c
# print(f'Дубликатов: {c}\nОригинальных: {d}')

# open()
# file = open('./slozna/slozna/act.txt')
# # r  только чтение файла
# # w  только для записи, создаст новый фаил, если такого нет
# # a  добавляет
# print(file.read())
# file.close()

# with open('./slozna/slozna/act.txt', encoding='utf-8') as file:
#     # print(file.readline())
#     # print(file.readline())
#     # print(file.read(3))
#     for line in file:
#         print(line, end='')

# with open('./slozna/slozna/ac.txt', 'w', encoding='utf-8') as file:
#     file.write('Veridis Quo')
#     file.write('\nOlo')

# with open('./slozna/slozna/ac.txt', 'a', encoding='utf-8') as file:
#     file.write('\nInion')
    
# with open('./slozna/slozna/ac.txt', encoding='utf-8') as file:
#     # print(file.readlines())
#     print(file.read())
# file.readable()
from PyQt5.QtWidgets import QApplication, QLineEdit, QListWidgetItem, QStyle, QWidget, QLabel, QPushButton, QSpinBox, QListWidget, QTreeWidget, QTreeWidgetItem
from PyQt5.QtGui import QIcon, QKeyEvent
from PyQt5.QtCore import QPoint, QSize, QEvent
import sys
import os
from datetime import date, time

a = {'2021-11-07': 10}
b = 3
c = 0
# for i in range(10):
#     a.append({f'{date.today()}': i})
print(len('dict_items([('))


# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setup()
#         self.one()
#         self.tree()

#     def setup(self):
#         self.setWindowTitle('0')
#         self.setFixedSize(300, 150)

#         self.listwidget = QTreeWidget(self)
#         self.listwidget.setHeaderHidden(True)
#         self.listwidget.setGeometry(0, 0, 300, 150)
#         # self.listitem = QTreeWidgetItem(self.listwidget)
#         # self.listitem.setText(0, '1')
#         # self.listitem1 = QTreeWidgetItem(self.listitem)
#         # self.listitem1.setText(0, '2')
#         # self.listwidget.addTopLevelItem(self.listitem1)
#         # self.listitem = QTreeWidgetItem('1',self.listwidget)
#         # print(type(self.listitem))

#     def one(self):
#         self.listitem = QTreeWidgetItem(self.listwidget)
#         self.listitem.setText(0, '1')
#         self.listitem1 = QTreeWidgetItem(self.listitem)
#         self.listitem1.setText(0, '2')
#         # self.listitem.setHidden(True)
#         self.listwidget.setItemWidget


    # def tree(self):
    #     z = set()
    #     v = []
    #     for b in a:
    #         for c in b.keys():
    #             z.add(c)
    #     print(len(z))
    #     if len(z) > 1:
    #         for x in len(z):
    #             locals()['num_%s' % x] = QTreeWidgetItem(self.listwidget)
    #             locals()['num_%s' % x].setText(0, f'{z.pop()}')
    #     else:
    #         num_1 = QTreeWidgetItem(self.listwidget)
    #         num_1.setText(0, f'{z.pop()}')
        # for i in a.keys()




# app = QApplication(sys.argv)
# window = Window()
# window.show()
# sys.exit(app.exec())