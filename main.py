import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QSizePolicy, QGridLayout, QLineEdit, QLabel, QScrollArea
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

def gridbutton_maker(text:str, width:int, height:int, row:int, col:int, rowspan:int, colspan:int, font:str, size:int, gridLayout, parent, number:bool, func):
    button = QPushButton(text, parent)
    button.setMinimumWidth(width)
    button.setMinimumHeight(height)
    button.setFont(QFont(font, size))

    gridLayout.addWidget(button, row, col, rowspan, colspan)
    if number:
        button.clicked.connect(lambda: func(text))
    elif number == None:
        pass
    else:
        button.clicked.connect(lambda: func(text))

    return button

def decimal_checker(num):   
    if int(num) == float(num):
        return int(num)
    else:
        return float(num)
    
class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout Demo")
        self.math1 = ""
        self.operator = ""
        self.math2 = ""

        # self.results = f"= {int(self.math1) * int(self.math2)}"
        self.calculator = QLabel("", self)
        self.calculator.setFont(QFont("Arial", 30))

        grid_layout = QGridLayout()

        grid_layout.addWidget(self.calculator, 0, 0, 1, 4)
        
        button_9 = gridbutton_maker("9", 70, 70, 2, 2, 1, 1, "Arial", 30, grid_layout, self, True, self.calculator_system)
        button_8 = gridbutton_maker("8", 70, 70, 2, 1, 1, 1, "Arial", 30, grid_layout, self, True, self.calculator_system)
        button_7 = gridbutton_maker("7", 70, 70, 2, 0, 1, 1, "Arial", 30, grid_layout, self, True, self.calculator_system)
        button_6 = gridbutton_maker("6", 70, 70, 3, 2, 1, 1, "Arial", 30, grid_layout, self, True, self.calculator_system)
        button_5 = gridbutton_maker("5", 70, 70, 3, 1, 1, 1, "Arial", 30, grid_layout, self, True, self.calculator_system)
        button_4 = gridbutton_maker("4", 70, 70, 3, 0, 1, 1, "Arial", 30, grid_layout, self, True, self.calculator_system)
        button_3 = gridbutton_maker("3", 70, 70, 4, 2, 1, 1, "Arial", 30, grid_layout, self, True, self.calculator_system)
        button_2 = gridbutton_maker("2", 70, 70, 4, 1, 1, 1, "Arial", 30, grid_layout, self, True, self.calculator_system)
        button_1 = gridbutton_maker("1", 70, 70, 4, 0, 1, 1, "Arial", 30, grid_layout, self, True, self.calculator_system)
        button_0 = gridbutton_maker("0", 70, 70, 5, 0, 1, 2, "Arial", 30, grid_layout, self, True, self.calculator_system)
        button_decimal = gridbutton_maker(".", 70, 70, 5, 2, 1, 1, "Arial", 30, grid_layout, self, True, self.calculator_system)
        button_equal = gridbutton_maker("=", 70, 70, 5, 3, 1, 1, "Arial", 30, grid_layout, self, None, None)
        button_plus = gridbutton_maker("+", 70, 70, 4, 3, 1, 1, "Arial", 30, grid_layout, self, False, self.operator_system)
        button_mines = gridbutton_maker("-", 70, 70, 3, 3, 1, 1, "Arial", 30, grid_layout, self, False, self.operator_system)
        button_times = gridbutton_maker("x", 70, 70, 2, 3, 1, 1, "Arial", 30, grid_layout, self, False, self.operator_system)
        button_divide = gridbutton_maker("/", 70, 70, 1, 3, 1, 1, "Arial", 30, grid_layout, self, False, self.operator_system)
        button_reset = gridbutton_maker("C", 70, 70, 1, 2, 1, 1, "Arial", 30, grid_layout, self, None, None)
        button_back = gridbutton_maker("Back", 70, 70, 1, 0, 1, 2, "Arial", 30, grid_layout, self, None, None)

        button_equal.setStyleSheet("background-color: #47b1e8;")

        button_equal.clicked.connect(self.results_input)
        button_reset.clicked.connect(self.reset)
        button_back.clicked.connect(self.back)

        self.setLayout(grid_layout)

    def results_input(self):
        if self.math1 != "" and self.math2 != "":
            match self.operator:
                case "+":
                    results = f"{float(self.math1) + float(self.math2)}"
                case "-":
                    results = f"{float(self.math1) - float(self.math2)}"
                case "x":
                    results = f"{float(self.math1) * float(self.math2)}"
                case "/":
                    results = f"{float(self.math1) / float(self.math2)}"
                    

            self.calculator.setText(f"{self.math1} {self.operator} {self.math2} = {decimal_checker(float(results))}")
    
    def calculator_system(self, value):
        if self.operator == "":
            math1S = self.math1 + value
            self.math1 = math1S
            self.calculator.setText(f"{self.math1}")
        else:
            math2S = self.math2 + value
            self.math2 = math2S
            self.calculator.setText(f"{self.math1} {self.operator} {self.math2}")

    def operator_system(self, value):
        if self.math1 != "" and self.math2 == "":
            match value:
                case "+":
                    self.operator = value
                    self.calculator.setText(f"{self.math1} {value}")
                case "-":
                    self.operator = value
                    self.calculator.setText(f"{self.math1} {value}")
                case "x":
                    self.operator = value
                    self.calculator.setText(f"{self.math1} {value}")
                case "/":
                    self.operator = value
                    self.calculator.setText(f"{self.math1} {value}")
    
    def reset(self):
        self.math1 = ""
        self.math2 = ""
        self.operator = ""
        self.calculator.setText("")
    
    def back(self):
        if self.math1 != "" and self.operator == "":
            removed1 = self.math1[:-1]
            self.math1 = removed1
            self.calculator.setText(f"{self.math1}")
        elif self.operator != "" and self.math2 != "":
            removed2 = self.math2[:-1]
            self.math2 = removed2
            self.calculator.setText(f"{self.math1} {self.operator} {self.math2}")
        

app = QApplication(sys.argv)
window = Widget()

window.show()
app.exec()