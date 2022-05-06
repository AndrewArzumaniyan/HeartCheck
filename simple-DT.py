#подключаем модуль с направляющими линиями
from PyQt5.QtCore import Qt
#подключаем необходимые виджеты
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton, QVBoxLayout

from random import randint

app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle('Winner')
but = QPushButton('Generation')
text = QLabel('Put and you will know who is the winner')
winner = QLabel('?')
line = QVBoxLayout()

line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(winner, alignment=Qt.AlignCenter)
line.addWidget(but, alignment=Qt.AlignCenter)

main_win.setLayout(line)

def show_winner():
  number = randint(0,99)
  winner.setText(str(number))
  text.setText('Winner')

but.clicked.connect(show_winner)

main_win.show()
app.exec_()
