#!/usr/bin/env python
import math

from PyQt5.QtCore import (Qt)
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

        self.numVictory = 0
        self.numLosses = 0

        self.displayLosses = QLineEdit('0')
        self.displayVictory = QLineEdit('0')

        self.displayLosses.setReadOnly(True)
        self.displayVictory.setReadOnly(True)

        self.displayLosses.setAlignment(Qt.AlignCenter)
        self.displayVictory.setAlignment(Qt.AlignCenter)

        self.LossesLcd = QLCDNumber(3)
        self.LossesLcd.setSegmentStyle(QLCDNumber.Filled)

        font = self.displayLosses.font()
        font.setPointSize(font.pointSize() + 8)
        self.displayLosses.setFont(font)

        self.displayVictory.setFont(font)

        self.digitButtons = []

        self.victoryButton = self.createButton("Victory", "+",self.addVictoryOrLosses)
        self.lossesButton = self.createButton("Losses", "+",self.addVictoryOrLosses)

        self.lossesButton.setMinimumWidth(150)
        self.victoryButton.setMinimumWidth(150)
        self.LossesLcd.setMinimumHeight(100)

        # self.victoryDecreaseButton = self.createButton("-",self.self)
        # self.LosseDecreaseButton = self.createButton("-", self.self)

        mainLayout = QGridLayout()
        # mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addWidget(self.displayLosses, 0, 0, 1, 1)
        mainLayout.addWidget(self.displayVictory, 0, 1, 1, 1)
        mainLayout.addWidget(self.victoryButton, 1, 1, 1, 1)
        mainLayout.addWidget(self.lossesButton, 1, 0, 1, 1)
        mainLayout.addWidget(self.LossesLcd, 2, 0, 1, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("Objetives")


    def addVictoryOrLosses(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(1)

        # self.LossesLcd.value(operand)

        if clickedOperator == "Victory":
            self.numVictory = self.numVictory + 1
            self.displayVictory.setText(str(self.numVictory))

        if clickedOperator == "Losses":
            self.numLosses = self.numLosses + 1
            self.displayLosses.setText(str(self.numLosses))
            self.LossesLcd.display(str(self.numLosses))

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
