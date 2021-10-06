import os

from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from lib.share import SI
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import Dialog1


class win_login(object):

    def __init__(self):

        self.ui = QUiLoader().load('login.ui')
        self.ui2 = QUiLoader().load('login2.ui')
        self.ui.btn_login.clicked.connect(self.jump_to_demo1)
        self.ui.edt_password.returnPressed.connect(self.jump_to_demo1)

#目前还存在问题的登录页面（需要运行在虚拟机上的API）
    # def onsignin(self):
    #     username = self.ui.edt_username.text().strip()
    #     password = self.ui.edt_password.text().strip()
    #     s = requests.Session()
    #     url = "http://192.168.1.105/api/sign"
    #     res =s.post(url,json={
    #     "action" : "signin",
    #     "username" : username,
    #     "password" : password
    #     })
    #     resobj=res.json()
    #     if resobj['ret'] != 0 :
    #         QMessageBox.warning(
    #             self.ui,
    #             '登录失败',
    #             resobj['msg'])
    #         return
    #     SI.mainwin = win_main()
    #     SI.mainwin.ui.show()
    #     self.ui.edt_password.setText('')
    #     self.ui.hide()
    def jump_to_demo1(self):#这一块注意，是重点从主界面跳转到Demo1界面，主界面隐藏，如果关闭Demo界面，主界面进程会触发self.form.show()会再次显示主界面
        self.ui.hide()   #如果没有self.form.show()这一句，关闭Demo1界面后就会关闭程序
        os.system('python main.py')
        # self.ui2.show()
        #form1 = QtWidgets.QDialog()
        # ui = Dialog1.Ui_MainWindow()
        # ui.setupUi(form1)
        # form1.show()
        # form1.exec_()


class win_main:
    def __init__(self):
        self.ui = QUiLoader().load('main.ui')
        self.ui.actiontui.triggered.connect(self.onsignout)
 #   def onsignout(self):






app = QApplication([])
SI.loginwin = win_login()
SI.loginwin.ui.show()
app.exec_()