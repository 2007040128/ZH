import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QListWidget, QHBoxLayout, QSplitter, QListWidgetItem
from PyQt5 import QtCore
from PyQt5 import QtGui
from PySide2.QtCore import QStringListModel
from PySide2.QtGui import QPixmap
from PySide2.QtUiTools import QUiLoader
from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView, QMessageBox

import sys
from PyQt5.QtCore import QStringListModel

from login2_ui import Ui_MainWindow
a=str()
g=str("g")
flag=1
class Window_main(Ui_MainWindow,QWidget):
    def __init__(self, *args, obj=None, **kwargs):
        super(Window_main, self).__init__(*args, **kwargs)
        # self.ui2.setupUi(self)
        self.ui2 = QUiLoader().load('login2.ui')
        self.ui2.upload.triggered.connect(self.open)
        self.ui2.pushButton_2.clicked.connect(self.show_re)
        self.ui2.fx.triggered.connect(self.shujv)
        self.timer = QBasicTimer()
        self.step = 0

        self.tabWidget = QtWidgets.QTabWidget()
        self.tab_zc = QtWidgets.QWidget()
        self.tab_yc = QtWidgets.QWidget()
        self.yc = QListWidget(self.tab_yc)
        self.zc = QListWidget(self.tab_zc)
        # self.tabWidget.currentChanged.connect(self.open2)
        self.ui2.tabWidget.currentChanged['int'].connect(self.tabfun)

        self.file_paths = []  # 文件列表
        self.file_index = 0	  # 文件索引

        self.ui2.yc.itemClicked.connect(self.show_yc)
        self.ui2.zc.itemClicked.connect(self.show_zc)

    def show_yc(self):
        # self.ui2.label_1.setGeometry(1,1,468,268)
        item=self.ui2.yc.selectedItems()[0]
        self.ui2.label_2.setText(item.text())
        global a
        a = item.text()[0]
        print(a)
        pix = QPixmap('./anormaly' + item.text())
        self.ui2.label_1.setPixmap(pix)
        self.ui2.label_1.setScaledContents(True)
        global flag
        flag==1
    def show_zc(self):
        # self.ui2.label_1.setGeometry(1,1,468,268)
        path = './good'
        mylist = os.listdir(path)
        pix = QPixmap('./good/'+mylist[0])
        self.ui2.label_1.setPixmap(pix)
        self.ui2.label_1.setScaledContents(True)
        self.ui2.label_2.clear()

    def show_re(self):
        global flag
        if flag == 1:
            path = './ours_gradient_maps/ours_test'
            mylist = os.listdir(path)
            # print(mylist[0][0])
            for i in mylist:
                print(a)
                print(i[0])
                if a in i[0]:
                    if g in i[7]:
                        print(i[7])
                        pix = QPixmap('./ours_gradient_maps/ours_test/'+i)
            self.ui2.label_2.setPixmap(pix)
            self.ui2.label_2.setScaledContents(True)
            print("34567")
        else:
            QMessageBox.about(self, "提示", "该图片为正常图片")



    def open(self):
        os.system('python upload.py')

    def tabfun(self,index):
        print("tabfun click" + "  " + str(index))
        if (index == 0):
            print("click 0")
            global flag
            flag=0
            self.deleteitem_zc()
            self.du_zc()
        else:
            print("click 1")
            flag = 1
            self.deleteitem_yc()
            self.du_yc()

    def shujv(self):
        os.system('python fx.py')

    def du_yc(self):
        path='./anormaly'
        mylist=os.listdir(path)
        self.file_paths.clear()
        for root, dirs, files in os.walk(path, topdown=False):
            for file in files:
                self.file_paths.append(os.path.join(root, file))
        # text=QListWidgetItem(self.file_paths[0])
        # print(type(text))
        # print(self.file_paths[0])
        for i in range(len(mylist)):
            self.ui2.yc.addItem(mylist[i])
            # print(mylist[i])
        if len(self.file_paths) <= 0:
            return
    def du_zc(self):
        path='./good'
        # path='E:/python/xxq/qtwj/NF/dataset_N/ours_class/test/good'
        mylist=os.listdir(path)
        self.file_paths.clear()
        for root, dirs, files in os.walk(path, topdown=False):
            for file in files:
                self.file_paths.append(os.path.join(root, file))
        # text=QListWidgetItem(self.file_paths[0])
        # print(type(text))
        # print(self.file_paths[0])
        for i in range(len(mylist)):
            self.ui2.zc.addItem(mylist[i])
        if len(self.file_paths) <= 0:
            return


    def deleteitem_zc(self):
        self.ui2.yc.clear()
    def deleteitem_yc(self):
        self.ui2.zc.clear()





    # def onStart(self):
    #     if self.timer.isActive():
    #         self.timer.stop()
    #         self.ui2.pushButton.setText('Start')
    #     else:
    #         self.timer.start(100, self)
    #         self.ui2.pushButton.setText('Stop')



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myWin = Window_main()
    myWin.ui2.show()
    sys.exit(app.exec_())

