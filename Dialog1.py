# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(678, 518)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/biao.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 678, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.upload = QtWidgets.QAction(MainWindow)
        self.upload.setObjectName("upload")
        self.action1 = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../image/1 (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action1.setIcon(icon1)
        self.action1.setObjectName("action1")
        self.action1_2 = QtWidgets.QAction(MainWindow)
        self.action1_2.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../image/2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action1_2.setIcon(icon2)
        self.action1_2.setObjectName("action1_2")
        self.actiontui = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../cankao/hyDM/images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actiontui.setIcon(icon3)
        self.actiontui.setObjectName("actiontui")
        self.actionban = QtWidgets.QAction(MainWindow)
        self.actionban.setObjectName("actionban")
        self.menu.addAction(self.upload)
        self.menu_3.addAction(self.action1)
        self.menu_3.addAction(self.action1_2)
        self.menu_4.addAction(self.actiontui)
        self.menu_4.addAction(self.actionban)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.toolBar.addAction(self.action1)
        self.toolBar.addAction(self.action1_2)
        self.toolBar.addAction(self.actiontui)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "软包装检测"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "测试"))
        self.menu_3.setTitle(_translate("MainWindow", "运行"))
        self.menu_4.setTitle(_translate("MainWindow", "关于"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.upload.setText(_translate("MainWindow", "上传文件"))
        self.action1.setText(_translate("MainWindow", "开始检测"))
        self.action1_2.setText(_translate("MainWindow", "中止检测"))
        self.actiontui.setText(_translate("MainWindow", "退出"))
        self.actionban.setText(_translate("MainWindow", "版本信息"))

# class Ui_Dialog1(object):
#     def setupUi(self, Dialog1):
#         Dialog1.setObjectName("Dialog1")
#         Dialog1.resize(400, 300)
#         self.dialog=Dialog1
#         self.pushButton = QtWidgets.QPushButton(Dialog1)
#         self.pushButton.setGeometry(QtCore.QRect(140, 140, 75, 23))
#         self.pushButton.setObjectName("pushButton")
#
#         self.retranslateUi(Dialog1)
#         QtCore.QMetaObject.connectSlotsByName(Dialog1)
#
#     def retranslateUi(self, Dialog1):
#         _translate = QtCore.QCoreApplication.translate
#         Dialog1.setWindowTitle(_translate("Dialog1", "Dialog"))
#         self.pushButton.setText(_translate("Dialog1", "Jump to main"))
#         self.pushButton.clicked.connect(self.jump_to_main)
#
#     def jump_to_main(self):
#         self.dialog.close()
