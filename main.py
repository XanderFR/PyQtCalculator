import sys
from PyQt6.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PyQt Calculator")

        self.currentInput = "0"
        self.previousInput = ""
        self.currentOperator = ""

        layout = QGridLayout()
        self.setLayout(layout)

        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.display, 0, 0, 1, 4)

        buttons = [QPushButton(str(i)) for i in range(10)]
        for i, button in enumerate(buttons):
            row, column = divmod(i, 3)
            layout.addWidget(button, row+1, column)

        for button in buttons:
            button.clicked.connect(self.numberButtonClicked)

        operators = ["+", "-", "*", "/"]
        operatorButtons = [QPushButton(op) for op in operators]
        for i, opButton in enumerate(operatorButtons):
            layout.addWidget(opButton, i+1, 3)

        for button in operatorButtons:
            button.clicked.connect(self.operatorButtonClicked)

        self.equalsButton = QPushButton("=")
        self.equalsButton.clicked.connect(self.calculate)
        self.clearButton = QPushButton("C")
        self.clearButton.clicked.connect(self.clear)

        layout.addWidget(self.equalsButton, 4, 1)
        layout.addWidget(self.clearButton, 4, 2)

    def numberButtonClicked(self):
        digit = self.sender().text()  # Get text of clicked number button
        if self.currentInput == "0":
            self.currentInput = digit
        else:
            self.currentInput += digit
        self.display.setText(self.currentInput)

    def operatorButtonClicked(self):
        operator = self.sender().text()  # Get text of clicked operator button
        if self.currentOperator == "":
            self.currentOperator = operator
            self.previousInput = self.currentInput
            self.currentInput = "0"
        else:
            self.calculate()
            self.currentOperator = operator
            self.previousInput = self.currentInput
            self.currentInput = "0"

    def calculate(self):
        if self.currentOperator == "+":
            result = str(float(self.previousInput) + float(self.currentInput))
        elif self.currentOperator == "-":
            result = str(float(self.previousInput) - float(self.currentInput))
        elif self.currentOperator == "*":
            result = str(float(self.previousInput) * float(self.currentInput))
        elif self.currentOperator == "/":
            if self.currentOperator == "0":
                result = "Error"
            else:
                result = str(float(self.previousInput) / float(self.currentInput))
        else:
            result = self.currentInput
        self.display.setText(result)
        self.currentInput = result
        self.currentOperator = ""

    def clear(self):
        self.currentInput = "0"
        self.previousInput = ""
        self.currentOperator = ""
        self.display.setText(self.currentInput)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
