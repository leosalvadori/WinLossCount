#!/usr/bin/env python
import math

from PyQt5.QtWidgets import (QApplication, QGridLayout, QLayout, QLineEdit,
        QSizePolicy, QToolButton, QWidget, QLCDNumber)

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
    NumDigitButtons = 2

    def __init__(self, parent=None):
        super(Objetives, self).__init__(parent)

        paletteLosses = QPalette()
        paletteVictory = QPalette()

        paletteLosses.setColor(paletteLosses.WindowText, QColor(255, 000, 000))
        paletteVictory.setColor(paletteVictory.WindowText, QColor(000, 255, 000))

        self.numVictory = 0
        self.numLosses = 0

        self.lossesLcd = QLCDNumber(3)
        self.lossesLcd.setSegmentStyle(QLCDNumber.Filled)
        self.lossesLcd.setPalette(paletteLosses)

        self.victoryLcd = QLCDNumber(3)
        self.victoryLcd.setSegmentStyle(QLCDNumber.Filled)
        self.victoryLcd.setPalette(paletteVictory)

        self.digitButtons = []

        self.victoryButton = self.createButton("Victory", "+",self.addVictoryOrLosses)
        self.lossesButton = self.createButton("Losses", "+",self.addVictoryOrLosses)
        self.victoryDecreaseButton = self.createButton("VD","-",self.addVictoryOrLosses)
        self.losseDecreaseButton = self.createButton("LD","-",self.addVictoryOrLosses)

        self.lossesButton.setMinimumWidth(150)
        self.victoryButton.setMinimumWidth(150)

        self.losseDecreaseButton.setMaximumWidth(30)
        self.victoryDecreaseButton.setMaximumWidth(30)

        self.lossesLcd.setMinimumHeight(100)
        self.victoryLcd.setMinimumHeight(100)

        mainLayout = QGridLayout()

        mainLayout.addWidget(self.lossesLcd, 0, 2, 1, 1)
        mainLayout.addWidget(self.victoryLcd, 0, 0, 1, 1)
        mainLayout.addWidget(self.victoryButton, 1, 0, 1, 1)
        mainLayout.addWidget(self.victoryDecreaseButton, 1, 1, 1, 1)
        mainLayout.addWidget(self.lossesButton, 1, 2, 1, 1)
        mainLayout.addWidget(self.losseDecreaseButton, 1, 3, 1, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("Objetives")

    def addVictoryOrLosses(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        # clickedOp = clickedButton.op()
        operand = float(1)

        if clickedOperator == "Victory": #or clickedOperator == "VD":
            self.numVictory = self.numVictory + 1
            self.victoryLcd.display(str(self.numVictory))

        if clickedOperator == "Losses":
            self.numLosses = self.numLosses + 1
            self.lossesLcd.display(str(self.numLosses))

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
