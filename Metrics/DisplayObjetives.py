#!/usr/bin/env python
import math

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter, QPalette
from PyQt5.QtWidgets import (QApplication, QGridLayout, QLayout, QLineEdit,
        QSizePolicy, QToolButton, QWidget, QLCDNumber, QGroupBox, QHBoxLayout, QPushButton)

class Button(QToolButton):
    def __init__(self, text, op, parent=None):
        super(Button,self).__init__(parent)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Objetives(QWidget):
    NumButtons = 3

    def __init__(self, parent=None):
        super(Objetives, self).__init__(parent)

        self.createDisplay()
        self.createDisplayAverage()
        self.createButtons()

        self.numVictory = 0
        self.numLosses = 0

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.displayLCD)
        mainLayout.addWidget(self.horizontalGroupBox)
        mainLayout.addWidget(self.displayLCDAverage)

        self.setLayout(mainLayout)

        self.setWindowTitle("Objetives")

    def createButtons(self):
        self.horizontalGroupBox = QGroupBox("")
        layout = QGridLayout()

        self.victoryButton = self.createButton("Victory", "+",self.addVictoryOrLosses)
        self.lossesButton = self.createButton("Losses", "+",self.addVictoryOrLosses)
        self.victoryDecreaseButton = self.createButton("DV","-",self.addVictoryOrLosses)
        self.losseDecreaseButton = self.createButton("DL","-",self.addVictoryOrLosses)

        self.lossesButton.setMinimumWidth(150)
        self.victoryButton.setMinimumWidth(150)

        self.losseDecreaseButton.setMaximumHeight(20)
        self.victoryDecreaseButton.setMaximumHeight(20)

        layout.addWidget(self.victoryButton, 0, 0, 1, 1)
        layout.addWidget(self.lossesButton, 0, 2, 1, 1)
        layout.addWidget(self.victoryDecreaseButton, 1, 0, 1, 1)
        layout.addWidget(self.losseDecreaseButton, 1, 2, 1, 1)

        self.horizontalGroupBox.setLayout(layout)

    def createDisplayAverage(self):
        self.displayLCDAverage = QGroupBox("Average")
        layout = QHBoxLayout()

        paletteLosses = QPalette()
        paletteVictory = QPalette()

        paletteLosses.setColor(paletteLosses.WindowText, QColor(255, 000, 000))
        paletteVictory.setColor(paletteVictory.WindowText, QColor(000, 255, 000))

        self.lossesLcdAv = QLCDNumber(5)
        self.lossesLcdAv.setSegmentStyle(QLCDNumber.Filled)
        self.lossesLcdAv.setPalette(paletteLosses)

        self.victoryLcdAv = QLCDNumber(5)
        self.victoryLcdAv.setSegmentStyle(QLCDNumber.Filled)
        self.victoryLcdAv.setPalette(paletteVictory)

        self.lossesLcdAv.setMinimumHeight(100)
        self.victoryLcdAv.setMinimumHeight(100)

        self.lossesLcdAv.setMinimumWidth(150)
        self.victoryLcdAv.setMinimumWidth(150)

        layout.addWidget(self.victoryLcdAv)
        layout.addWidget(self.lossesLcdAv)

        self.displayLCDAverage.setLayout(layout)

    def createDisplay(self):
        self.displayLCD = QGroupBox("")
        layout = QHBoxLayout()

        paletteLosses = QPalette()
        paletteVictory = QPalette()

        paletteLosses.setColor(paletteLosses.WindowText, QColor(255, 000, 000))
        paletteVictory.setColor(paletteVictory.WindowText, QColor(000, 255, 000))

        self.lossesLcd = QLCDNumber(3)
        self.lossesLcd.setSegmentStyle(QLCDNumber.Filled)
        self.lossesLcd.setPalette(paletteLosses)

        self.victoryLcd = QLCDNumber(3)
        self.victoryLcd.setSegmentStyle(QLCDNumber.Filled)
        self.victoryLcd.setPalette(paletteVictory)

        self.lossesLcd.setMinimumHeight(100)
        self.victoryLcd.setMinimumHeight(100)

        self.lossesLcd.setMinimumWidth(150)
        self.victoryLcd.setMinimumWidth(150)

        layout.addWidget(self.victoryLcd)
        layout.addWidget(self.lossesLcd)

        self.displayLCD.setLayout(layout)

    def addVictoryOrLosses(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(1)

        if clickedOperator == "Victory":
            self.numVictory = self.numVictory + 1
            self.victoryLcd.display(str(self.numVictory))

        if clickedOperator == "DV":
            self.numVictory = self.numVictory - 1
            self.victoryLcd.display(str(self.numVictory))

        if clickedOperator == "Losses":
            self.numLosses = self.numLosses + 1
            self.lossesLcd.display(str(self.numLosses))

        if clickedOperator == "DL":
            self.numLosses = self.numLosses - 1
            self.lossesLcd.display(str(self.numLosses))

        self.calculateAverage()

    def calculateAverage(self):
        total = self.numVictory + self.numLosses

        self.victoryLcdAv.display(str(int(self.numVictory / total * 100)))
        self.lossesLcdAv.display(str(int(self.numLosses / total * 100)))

    def createButton(self, text, op, member):
        button = Button(text,op)
        button.clicked.connect(member)
        return button

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    obj = Objetives()
    obj.show()
    sys.exit(app.exec_())
