import os
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PySide2.QtUiTools import QUiLoader
from threading import Thread
from threading import Timer
import threading
import time
import ctypes
import inspect
from jiazai import MsgBox
from window4_ui import Ui_MainWindow


class Window_main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(Window_main, self).__init__(*args, **kwargs)
        self.setupUi(self)  # 必须调用自动生成的两个方法
        self.retranslateUi(self)
        self.ui = QUiLoader().load('window4.ui')

        self.pushButton.clicked.connect(self.msg)
        self.pushButton_2.clicked.connect(self.tiao)
        self.listView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listView.customContextMenuRequested[QtCore.QPoint].connect(self.rightMenuShow)
        self.listView.setContextMenuPolicy(Qt.CustomContextMenu)  # 右键菜单
        self.listView.customContextMenuRequested[QtCore.QPoint].connect(self.rightMenuShow)
        self.listView.doubleClicked.connect(self.clicked)
        self.listView.clicked.connect(self.clicked)



        self.label.setPixmap(QPixmap("./images/python.jpg"))
        self.label.setScaledContents(True)  # 将显示图像大小自动调整为Qlabel大小。

        self.setWindowTitle("软包装检测系统")


    def rightMenuShow(self):
        rightMenu = QtWidgets.QMenu(self.listView)
        removeAction = QtWidgets.QAction(u"Delete", self,
                                         triggered=self.removeimage)  # triggered 为右键菜单点击后的激活事件。这里slef.close调用的是系统自带的关闭事件。
        rightMenu.addAction(removeAction)
        rightMenu.exec_(QtGui.QCursor.pos())

    def clicked(self, qModelIndex):
        # QMessageBox.information(self, "QListView", "你选择了: "+ imgName[qModelIndex.row()])
        global path
        self.label.setPixmap(QPixmap(imgName[qModelIndex.row()]))
        path = imgName[qModelIndex.row()]

    def msg(self):
        global imgName
        imgName,directory = QtWidgets.QFileDialog.getOpenFileNames(self, "选取多个文件", "./",
                                                           "All Files (*);;Text Files (*.txt)")
        print(imgName)

        slm = QStringListModel()
        slm.setStringList(imgName)
        self.listView.setModel(slm)


    def removeimage(self):
        selected = self.listView.selectedIndexes()
        itemmodel = self.listView.model()
        for i in selected:
            itemmodel.removeRow(i.row())

    def tiao(self): 
        self.close()
        # self.ui2.show()
        # self.myWin.ui.hide()
        #os.system('python main.py')
        thread = Thread(target=self.threadSend)
        thread.start()
        # thread.run()
        os.system('python F:/python/python/xxq/qtwj/NF/previous_test.py')
        stop_thread(thread)
        # thread.join(self, timeout=True)
        print("34567")
    def threadSend(self):
            os.system('python jiazai.py')
            print("694631")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mywin = Window_main()  # 实例化一个应用对象
    mywin.show()  # 让窗口在桌面上显示出来。控件在内存里创建，之后才能在显示器上显示出来。
    sys.exit(app.exec_())  # 确保主循环安全退出

def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)

def _async_raise(tid, exctype):
   """raises the exception, performs cleanup if needed"""
   tid = ctypes.c_long(tid)
   if not inspect.isclass(exctype):
       exctype = type(exctype)
   res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
   if res == 0:
       raise ValueError("invalid thread id")
   elif res != 1:
       # """if it returns a number greater than one, you're in trouble,
       # and you should call it again with exc=NULL to revert the effect"""
       ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
       raise SystemError("PyThreadState_SetAsyncExc failed")
