import sys
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from Gui import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.Button_number0.clicked.connect(lambda: self.press_key("0"))
        self.uic.Button_number1.clicked.connect(lambda: self.press_key("1"))
        self.uic.Button_number2.clicked.connect(lambda: self.press_key("2"))
        self.uic.Button_number3.clicked.connect(lambda: self.press_key("3"))
        self.uic.Button_number4.clicked.connect(lambda: self.press_key("4"))
        self.uic.Button_number5.clicked.connect(lambda: self.press_key("5"))
        self.uic.Button_number6.clicked.connect(lambda: self.press_key("6"))
        self.uic.Button_number7.clicked.connect(lambda: self.press_key("7"))
        self.uic.Button_number8.clicked.connect(lambda: self.press_key("8"))
        self.uic.Button_number9.clicked.connect(lambda: self.press_key("9"))
        self.uic.Button_dot.clicked.connect(lambda: self.press_key("."))
        self.uic.Button_permission.clicked.connect(lambda: self.press_key("%"))
        self.uic.Button_add.clicked.connect(lambda: self.press_key("+"))
        self.uic.Button_sub.clicked.connect(lambda: self.press_key("-"))
        self.uic.Button_mul.clicked.connect(lambda: self.press_key("x"))
        self.uic.Button_devision.clicked.connect(lambda: self.press_key("/"))
        self.uic.Button_Del.clicked.connect(lambda: self.press_key("Del"))
        self.uic.Button_AC.clicked.connect(lambda: self.press_key("AC"))
        self.uic.Button_Equal.clicked.connect(lambda: self.Equal())
    
    def Equal(self):
        bt = self.uic.Screen_CAL.text()
        bt = bt.replace("x", "*")
        res = eval(bt)
        self.uic.Screen_CAL.setText(str(res))
    def press_key(self,key):
        if key == 'AC':
            self.uic.Screen_CAL.setText("")
        elif key == 'Del':
            copy = self.uic.Screen_CAL.text()[:-1]
            self.uic.Screen_CAL.setText(copy)
        else:   
            copy = self.uic.Screen_CAL.text()
            self.uic.Screen_CAL.setText("{:s}{:s}".format(copy,key))
    def show(self):
        # command to run
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())