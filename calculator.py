



import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QWidget,QGridLayout,
                             QLineEdit, QPushButton,
                             QVBoxLayout)

WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40

class MyCalculatorWindow(QMainWindow):

    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        return self.display.text()

    def clearDsiplay(self):
        self.setDisplayText("")

    def _createButtons(self):
        self.buttonMap = {}
        buttonsLayout = QGridLayout()
        keyBoard = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="],
        ]

        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)
                self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                buttonsLayout.addWidget(self.buttonMap[key], row, col)

        self.generalLayout.addLayout(buttonsLayout)

    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)


    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Calculator")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createDisplay()
        self._createButtons()

def main():

    myCalculatorApp = QApplication([])
    mycalculatorWindow = MyCalculatorWindow()
    mycalculatorWindow.show()
    sys.exit(myCalculatorApp.exec())

if __name__ == "__main__":
    main()



# calculator_app = QApplication([])
# window = QWidget()
# window.setWindowTitle("My Calculator")
# window.setGeometry(100, 100, 400, 400)
# output_box = QLabel("<h1>Hello, World!</h1>", parent=window)
# output_box.move(60, 15)
# keypad_layout = QGridLayout()
# keypad_layout.addWidget(QPushButton("1"), 0,0)
# keypad_layout.addWidget(QPushButton("2"), 0,1)
# keypad_layout.addWidget(QPushButton("3"), 0,2)
# keypad_layout.addWidget(QPushButton("4"), 1,0)
# keypad_layout.addWidget(QPushButton("5"), 1,1)
# keypad_layout.addWidget(QPushButton("6"), 1,2)
# keypad_layout.addWidget(QPushButton("7"), 2,0)
# keypad_layout.addWidget(QPushButton("8"), 2,1)
# keypad_layout.addWidget(QPushButton("9"), 2,2)
# keypad_layout.addWidget(QPushButton("0"), 3,0,1,2)
# keypad_layout.addWidget(QPushButton("+"), 3,3)
# keypad_layout.addWidget(QPushButton("-"), 2,3)
# keypad_layout.addWidget(QPushButton("x"), 1,3)
# keypad_layout.addWidget(QPushButton("/"), 0,3)
# keypad_layout.addWidget(QPushButton("="), 3,2)
#
#
# window.setLayout(keypad_layout)
#
#
#
# window.show()
# sys.exit(calculator_app.exec())



# import sys
# from PyQt6.QtWidgets import (
#     QApplication,
#     QLabel,
#     QMainWindow,
#     QStatusBar,
#     QToolBar,
# )
#
# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__(parent=None)
#         self.setWindowTitle("QMainWindow")
#         self.setCentralWidget(QLabel("This is the central widget"))
#         self.createMenu()
#         self.createToolBar()
#         self.createStatusBar()
#
#     def createMenu(self):
#         menu = self.menuBar().addMenu("&Menu")
#         menu.addAction("&Exit", self.close)
#
#     def createToolBar(self):
#         tools = QToolBar()
#         tools.addAction("&Exit", self.close)
#         self.addToolBar(tools)
#
#     def createStatusBar(self):
#         status = QStatusBar()
#         status.showMessage("This is status bar")
#         self.setStatusBar(status)
#
# if __name__ == "__main__":
#     app = QApplication([])
#     window = Window()
#     window.show()
#     sys.exit(app.exec())
