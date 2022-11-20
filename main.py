# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QPushButton
from ds1054z import DS1054Z
import sys


# signals_slots.py

"""Signals and slots example."""

import sys
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

def convert(data):
    f = open('1.jpg', 'wb')
    f.write(data)
    f.close()

def start_read():
    scope = DS1054Z('192.168.0.182')
    bitmapa = scope.display_data
    print("Connected to: ", scope.idn)
    ident = scope.idn
    channels = str(scope.displayed_channels)
    print("Currently displayed channels: ", str(scope.displayed_channels))

    return ident,channels, bitmapa

def greet():
    if msgLabel.text():
        msgLabel.setText("")
    else:
        ident, channels, bitmapa = start_read()
        msgLabel.setText(ident)
        chnLabel.setText(channels[2:-2])
        convert(bitmapa)
        pixmap = QPixmap("1.jpg")
        label.setPixmap(pixmap)

app = QApplication([])
window = QWidget()
window.resize(200,500)
window.setWindowTitle("Signals and slots")
layout = QVBoxLayout()

button = QPushButton("Greet")
button.setGeometry(200, 150, 100, 400)
button.clicked.connect(greet)

layout.addWidget(button)
msgLabel = QLabel("")
layout.addWidget(msgLabel)
chnLabel = QLabel("")
layout.addWidget(chnLabel)

label = QLabel("")
layout.addWidget(label)



window.setLayout(layout)
window.setFixedWidth(850)
window.show()
sys.exit(app.exec())



# Press the green button in the gutter to run the script.
