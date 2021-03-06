# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(876, 897)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/新前缀/165.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    \n"
"    background-color: rgb(207, 224, 247);\n"
"    \n"
"}")
        MainWindow.setIconSize(QtCore.QSize(100, 50))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:2, fx:0.5, fy:0.5, stop:0 rgba(207, 224, 247), stop:1 rgba(252, 252, 252, 255));\n"
"\n"
"    \n"
"    \n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(16, 0, 0, 0)
        self.verticalLayout_4.setSpacing(7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 4))
        self.tabWidget.setMaximumSize(QtCore.QSize(302, 10000))
        font = QtGui.QFont()
        font.setFamily("百度综艺简体")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget{    \n"
"font: 11pt \"百度综艺简体\";\n"
"\n"
"    background-color: rgb(190, 43, 46);\n"
"border-radius: 1px;\n"
"border:1px groove gray;\n"
"border-style: outset;\n"
"    color: rgb(253, 253, 253);\n"
"\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_zc = QtWidgets.QWidget()
        self.tab_zc.setObjectName("tab_zc")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_zc)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.zc = QtWidgets.QListWidget(self.tab_zc)
        self.zc.setMinimumSize(QtCore.QSize(200, 0))
        self.zc.setMaximumSize(QtCore.QSize(300, 10000))
        self.zc.setStyleSheet("QListView{\n"
" font: 11pt \"微软雅黑\";\n"
" background-color: rgb(252, 252, 252);\n"
"border-radius: 5px;\n"
"border:2px groove gray;\n"
"border-style: outset;\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.zc.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.zc.setObjectName("zc")
        self.verticalLayout_2.addWidget(self.zc)
        self.tabWidget.addTab(self.tab_zc, "")
        self.tab_yc = QtWidgets.QWidget()
        self.tab_yc.setObjectName("tab_yc")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_yc)
        self.verticalLayout.setObjectName("verticalLayout")
        self.yc = QtWidgets.QListWidget(self.tab_yc)
        self.yc.setStyleSheet("QListView{\n"
" font: 11pt \"微软雅黑\";\n"
" background-color: rgb(252, 252, 252);\n"
"border-radius: 5px;\n"
"border:2px groove gray;\n"
"border-style: outset;\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.yc.setObjectName("yc")
        self.verticalLayout.addWidget(self.yc)
        self.tabWidget.addTab(self.tab_yc, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setMinimumSize(QtCore.QSize(600, 300))
        self.label_1.setMaximumSize(QtCore.QSize(600, 400))
        self.label_1.setStyleSheet("QLabel{\n"
" font: 11pt \"微软雅黑\";\n"
" background-color: rgb(252, 252, 252);\n"
"border-radius: 5px;\n"
"border:2px groove gray;\n"
"border-style: outset;\n"
"color:rgb(163, 202, 235)\n"
"}")
        self.label_1.setObjectName("label_1")
        self.verticalLayout_3.addWidget(self.label_1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet("QPushButton\n"
"\n"
"{\n"
"    font: 10pt \"百度综艺简体\";\n"
"    \n"
"    background-color: rgb(66, 93, 138);\n"
"border-radius:10px;\n"
"border:2px groove gray;\n"
"border-style: outset;\n"
"    color: rgb(252, 252, 252);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(390, 300))
        self.label_2.setMaximumSize(QtCore.QSize(600, 400))
        self.label_2.setStyleSheet("QLabel{\n"
" font: 11pt \"微软雅黑\";\n"
" background-color: rgb(252, 252, 252);\n"
"border-radius: 5px;\n"
"border:2px groove gray;\n"
"border-style: outset;\n"
"color:rgb(163, 202, 235)\n"
"}")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 876, 26))
        self.menubar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.menubar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menubar.setStyleSheet("QMenuBar{\n"
"    background-color: rgb(207, 224, 247);\n"
"    \n"
"    color: rgb(45, 96, 151);\n"
"}\n"
"")
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setStyleSheet("QMenu{\n"
"        \n"
"    font: 10pt \"百度综艺简体\";\n"
"    \n"
"    background-color: rgb(66, 93, 138);\n"
"border-radius:3px;\n"
"border:2px groove gray;\n"
"border-style: outset;\n"
"    color: rgb(252, 252, 252);\n"
"}")
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("百度综艺简体")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.menu_2.setFont(font)
        self.menu_2.setStyleSheet("QMenu{\n"
"    font: 10pt \"百度综艺简体\";\n"
"    \n"
"    background-color: rgb(66, 93, 138);\n"
"border-radius:3px;\n"
"border:2px groove gray;\n"
"border-style: outset;\n"
"    color: rgb(252, 252, 252);\n"
"}")
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("百度综艺简体")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.menu_3.setFont(font)
        self.menu_3.setStyleSheet("QMenu{\n"
"font: 10pt \"百度综艺简体\";\n"
"    \n"
"    background-color: rgb(66, 93, 138);\n"
"border-radius:3px;\n"
"border:2px groove gray;\n"
"border-style: outset;\n"
"    color: rgb(252, 252, 252);\n"
"}")
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("百度综艺简体")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.menu_4.setFont(font)
        self.menu_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menu_4.setStyleSheet("QMenu{\n"
"    font: 10pt \"百度综艺简体\";\n"
"    \n"
"    background-color: rgb(66, 93, 138);\n"
"border-radius:3px;\n"
"border:2px groove gray;\n"
"border-style: outset;\n"
"    color: rgb(252, 252, 252);\n"
"}")
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("百度综艺简体")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.menu_5.setFont(font)
        self.menu_5.setToolTipDuration(6)
        self.menu_5.setStyleSheet("QMenu{\n"
"    font: 10pt \"百度综艺简体\";\n"
"    \n"
"    background-color: rgb(66, 93, 138);\n"
"border-radius:3px;\n"
"border:2px groove gray;\n"
"border-style: outset;\n"
"    color: rgb(252, 252, 252);\n"
"}")
        self.menu_5.setObjectName("menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("QStatusBar{\n"
"        background-color: rgb(207, 224, 247);\n"
"    \n"
"}")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setStyleSheet("QToolBar{\n"
"    background-color: rgb(207, 224, 247);\n"
"    }")
        self.toolBar_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.BottomToolBarArea, self.toolBar_2)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMouseTracking(False)
        self.toolBar.setToolTipDuration(-1)
        self.toolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setStyleSheet("QToolBar{\n"
"    background-color: rgb(207, 224, 247);\n"
"    \n"
"}")
        self.toolBar.setMovable(True)
        self.toolBar.setAllowedAreas(QtCore.Qt.AllToolBarAreas)
        self.toolBar.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar.setIconSize(QtCore.QSize(35, 35))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.upload = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/新前缀/线性上传文件图标.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.upload.setIcon(icon1)
        font = QtGui.QFont()
        font.setFamily("百度综艺简体")
        self.upload.setFont(font)
        self.upload.setObjectName("upload")
        self.action1 = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/新前缀/面性播放.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action1.setIcon(icon2)
        self.action1.setObjectName("action1")
        self.action1_2 = QtWidgets.QAction(MainWindow)
        self.action1_2.setCheckable(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/新前缀/未标题-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action1_2.setIcon(icon3)
        self.action1_2.setObjectName("action1_2")
        self.actiontui = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/新前缀/线性搜索图标.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actiontui.setIcon(icon4)
        self.actiontui.setObjectName("actiontui")
        self.actionban = QtWidgets.QAction(MainWindow)
        self.actionban.setObjectName("actionban")
        self.fx = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/新前缀/线性电子技术图标.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fx.setIcon(icon5)
        self.fx.setObjectName("fx")
        self.menu.addAction(self.upload)
        self.menu.addSeparator()
        self.menu_3.addAction(self.action1)
        self.menu_3.addAction(self.action1_2)
        self.menu_4.addAction(self.actiontui)
        self.menu_4.addAction(self.actionban)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.toolBar.addAction(self.upload)
        self.toolBar.addAction(self.action1)
        self.toolBar.addAction(self.action1_2)
        self.toolBar.addAction(self.fx)
        self.toolBar.addAction(self.actiontui)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "软包装检测"))
        self.tabWidget.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.zc.setSortingEnabled(False)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_zc), _translate("MainWindow", "正常"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_yc), _translate("MainWindow", "异常"))
        self.label_1.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_2.setText(_translate("MainWindow", "点击生成热点图"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "测试"))
        self.menu_3.setTitle(_translate("MainWindow", "运行"))
        self.menu_4.setTitle(_translate("MainWindow", "关于"))
        self.menu_5.setTitle(_translate("MainWindow", "分析"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.upload.setText(_translate("MainWindow", "上传文件"))
        self.upload.setIconText(_translate("MainWindow", "上传文件"))
        self.action1.setText(_translate("MainWindow", "开始检测"))
        self.action1_2.setText(_translate("MainWindow", "中止检测"))
        self.actiontui.setText(_translate("MainWindow", "退出"))
        self.actionban.setText(_translate("MainWindow", "版本信息"))
        self.fx.setText(_translate("MainWindow", "数据分析"))
import pic_rc
