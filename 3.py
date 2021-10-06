
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QHBoxLayout, QTabWidget, QFrame, QSplitter
from PyQt5.QtCore import  Qt
from PyQt5.QtWidgets import  QWidget, QListWidget, QSplitter, QFrame


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        self.tabwidget = QTabWidget()

        self.tab_yc = QWidget()
        self.tab_zc = QWidget()

        self.tabwidget.addTab(self.tab_yc, "异常")
        self.tabwidget.addTab(self.tab_zc, "正常")

        self.yc = QListWidget()

        self.lw_tab_yc_SplitterH = QSplitter(Qt.Horizontal)
        self.lw_tab_yc_SplitterH.addWidget(self.yc)


        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.lw_tab_yc_SplitterH)
        self.tab_yc.setLayout(hbox1)

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.tabwidget)
        self.setLayout(self.hbox)

        for i in range(6):
            text = 'Item {}'.format(i)
            self.yc.addItem(text)  # 添加项目

        self.yc.itemClicked.connect(self.g)
        print(type(self.yc))

    def g(self):
        print('dddd')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
