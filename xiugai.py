from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

import window4
class myDialog(window4.Ui_MainWindow):
    def __init__(self,Dialog):
        super().setupUi(Dialog)
    def __init__(self):
        self.ui2 = QUiLoader().load('window4.ui')
        self.ui2.pushButton_2.clicked.connect(self.msg)