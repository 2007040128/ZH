from PyQt5.QtWidgets import QPushButton, QDialog, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class MsgBox(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.Tool)
        self.resize(560, 420)
        self.setWindowTitle('检测中~~~')  # 窗口名称
        label = QLabel(self)
        movie = QMovie("E:/python/xxq/qtwj/my/runabao/0.gif")  # gif文件地址
        label.setMovie(movie)
        movie.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = MsgBox()
    demo.show()
    sys.exit(app.exec_())
