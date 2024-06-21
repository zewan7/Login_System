from PySide6.QtWidgets import QApplication, QWidget,QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QLabel,QLineEdit,QGraphicsLayout,QGridLayout,QFormLayout
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader
from Ui_zh111 import Ui_widget
from Ui_register import Ui_Form
import sys


class Mywindow(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_widget()
        self.ui.setupUi(self)
        self.ui.pushButton_register.clicked.connect(self.register)


    def register(self):
        sendwindow = MySendWindow()
        sendwindow.show()
        self.close()
        

class MySendWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.register_ui = Ui_Form()
        self.register_ui.setupUi(self)

   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mywindow()
    window.show()
    sys.exit(app.exec())





