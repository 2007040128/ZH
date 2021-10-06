# import matplotlib
# import numpy as np
#
# matplotlib.use('Qt5Agg')
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from PyQt5 import QtCore, QtWidgets,QtGui
# import matplotlib.pyplot as plt
# import sys
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton
# from PyQt5.QtCore import QBasicTimer
# from pyecharts import options as opts
# from pyecharts.charts import Pie
# from pyecharts.faker import Faker
#
# def _translate(param, param1):
#     pass
#
#
# class My_Main_window(QtWidgets.QMainWindow):
#     def __init__(self,parent=None):
#         super(My_Main_window,self).__init__(parent)
#
#         # 重新调整大小
#         self.resize(800, 659)
#         # 添加菜单中的按钮
#
#         self.menu = QtWidgets.QMenu("展示")
#         self.menu.setStyleSheet("QMenu{\n"
#                                 "    background-color: rgb(66, 93, 138);\n"
#                                 "    color: rgb(252, 252, 252)  ;\n"
#                                 "}")
#         font = QtGui.QFont()
#         font.setFamily("百度综艺简体")
#         self.menu.setFont(font)
#         self.menu_action = QtWidgets.QAction("绘制",self.menu)
#         self.menu_action2 = QtWidgets.QAction("绘制2", self.menu)
#         self.menu_action3 = QtWidgets.QAction("绘制3", self.menu)
#         self.menu.addAction(self.menu_action)
#         self.menu.addAction(self.menu_action2)
#         self.menu.addAction(self.menu_action3)
#         self.menuBar().addMenu(self.menu)
#         # 添加事件
#         self.menu_action.triggered.connect(self.plot_)
#         self.menu_action2.triggered.connect(self.plot_2)
#         self.menu_action3.triggered.connect(self.plot_3)
#         self.setCentralWidget(QtWidgets.QWidget())
#
#
#     # 绘图方法
#     def plot_(self):
#         # 清屏
#         plt.cla()
#         # 获取绘图并绘制
#         fig, ax = plt.subplots()
#         #ax.set_title("linear prediction"
#         plt.title('linear prediction')
#
#         ax.set_xlim([-1,6])
#         ax.set_ylim([-1,6])
#
#         ax.plot([0,1,2,3,4,5],'o-',color="#A5CEEF")
#         cavans = FigureCanvas(fig)
#         # 将绘制好的图像设置为中心 Widget
#         self.setCentralWidget(cavans)
#
#     def plot_2(self):
#         plt.cla()
#
#         labels = "good","anormaly"
#         sizes = [50,50]
#         explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
#
#         fig, ax1 = plt.subplots()
#         ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#                 shadow=True, startangle=90,colors=['#75CCE8','#A5DEE5'])
#         ax1.axis('equal')
#         cavans = FigureCanvas(fig)
#         # 将绘制好的图像设置为中心 Widget
#         self.setCentralWidget(cavans)
#
#
#
#
#     def plot_3(self):
#         plt.cla()
#         # np.random.seed(19680801)
#         # # example data
#         # mu = 50 # mean of distribution
#         # sigma = 15  # standard deviation of distribution
#         # x = mu
#         #
#         # num_bins = 10
#         #
#         # fig, ax = plt.subplots()
#         #
#         # # the histogram of the data
#         # n, bins, patches = ax.hist(x, num_bins, density=True)
#         #
#         # ax.set_xlabel('Smarts')
#         # ax.set_ylabel('Probability density')
#         # ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')
#
#         # # Tweak spacing to prevent clipping of ylabel
#
#         fig, ax = plt.subplots()
#         bars = plt.bar( ['r0c0','r0c1','r0c2','r1c0','r1c1','r1c2','r2c0','r2c1','r2c2'],[0,0,0,0,1,0,0,1,0],color='#BEF2E5')
#
#         ax.set_title("Defect statistics of different patches")
#         fig.tight_layout()
#         cavans = FigureCanvas(fig)
#         # 将绘制好的图像设置为中心 Widget
#         self.setCentralWidget(cavans)
#
# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     main_window = My_Main_window()
#     main_window.show()
#     app.exec()

import matplotlib
import numpy as np

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtCore, QtWidgets,QtGui

import sys
from PyQt5.QtCore import *

from PyQt5.QtWebEngineWidgets import *



class My_Main_window(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(My_Main_window,self).__init__(parent)

        # 重新调整大小
        self.resize(800, 600)
        # 添加菜单中的按钮
        self.setWindowTitle("数据分析")  # 设置窗口名
        self.setWindowIcon(QtGui.QIcon("./165.png"))
        self.menu = QtWidgets.QMenu("Show")
        self.menu.setStyleSheet("QMenu{\n"
                                "    background-color: rgb(66, 93, 138);\n"
                                "    color: rgb(252, 252, 252)  ;\n"
                                "}")
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.menu.setFont(font)
        font.setPointSize(11)
        self.menu_action = QtWidgets.QAction("Statistics",self.menu)
        self.menu_action2 = QtWidgets.QAction("linear prediction", self.menu)
        self.menu_action3 = QtWidgets.QAction("Defect statistics of different patches", self.menu)
        self.menu.addAction(self.menu_action)
        self.menu.addAction(self.menu_action2)
        self.menu.addAction(self.menu_action3)
        self.menuBar().addMenu(self.menu)
        # 添加事件
        self.menu_action.triggered.connect(self.plot_)
        self.menu_action2.triggered.connect(self.plot_2)
        self.menu_action3.triggered.connect(self.plot_3)
        self.setCentralWidget(QtWidgets.QWidget())

    def plot_(self):
        import pyecharts.options as opts
        from pyecharts.charts import Pie

        x_data = ["good", "anormaly"]
        y_data = [2, 2]
        data_pair = [list(z) for z in zip(x_data, y_data)]
        data_pair.sort(key=lambda x: x[1])

        (
            Pie(init_opts=opts.InitOpts(width="1600px", height="800px", bg_color="#2c343c"))
                .add(
                series_name="Statistics",
                data_pair=data_pair,
                # collor=['#a18cd1','#fbc2eb'],
                rosetype="radius",
                radius="45%",
                center=["25%", "40%"],
                label_opts=opts.LabelOpts(is_show=False, position="center"),
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="Statistics",
                    pos_left="22%",

                    pos_top="50",
                    title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
                ),
                legend_opts=opts.LegendOpts(is_show=False),
            )
                .set_series_opts(
                tooltip_opts=opts.TooltipOpts(
                    trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
                ),
                label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
            )
                .render("Statistics.html")
        )
        self.browser = QWebEngineView()
        # 加载外部的web界面
        self.browser.load(QUrl('file:///F:/python/python/xxq/qtwj/my/runabao/Statistics.html'))
        self.setCentralWidget(self.browser)



    def plot_2(self):
        from pyecharts import options as opts
        from pyecharts.charts import Line
        from pyecharts.commons.utils import JsCode

        x_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        background_color_js = (
            "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
            "[{offset: 0, color: '#c86589'}, {offset: 1, color: '#06a7ff'}], false)"
        )
        area_color_js = (
            "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
            "[{offset: 0, color: '#eb64fb'}, {offset: 1, color: '#3fbbff0d'}], false)"
        )

        c = (
            Line(init_opts=opts.InitOpts(bg_color=JsCode(background_color_js)))
                .add_xaxis(xaxis_data=x_data)
                .add_yaxis(
                series_name="注册总量",
                y_axis=y_data,
                is_smooth=True,
                is_symbol_show=True,
                symbol="circle",
                symbol_size=6,
                linestyle_opts=opts.LineStyleOpts(color="#fff"),
                label_opts=opts.LabelOpts(is_show=True, position="top", color="white"),
                itemstyle_opts=opts.ItemStyleOpts(
                    color="red", border_color="#fff", border_width=3
                ),
                tooltip_opts=opts.TooltipOpts(is_show=False),
                areastyle_opts=opts.AreaStyleOpts(color=JsCode(area_color_js), opacity=1),
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="linear prediction",
                    pos_bottom="10%",
                    pos_left="center",
                    title_textstyle_opts=opts.TextStyleOpts(color="#fff", font_size=16),
                ),
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    boundary_gap=False,
                    axislabel_opts=opts.LabelOpts(margin=30, color="#ffffff63"),
                    axisline_opts=opts.AxisLineOpts(is_show=False),
                    axistick_opts=opts.AxisTickOpts(
                        is_show=True,
                        length=25,
                        linestyle_opts=opts.LineStyleOpts(color="#ffffff1f"),
                    ),
                    splitline_opts=opts.SplitLineOpts(
                        is_show=True, linestyle_opts=opts.LineStyleOpts(color="#ffffff1f")
                    ),
                ),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    position="right",
                    axislabel_opts=opts.LabelOpts(margin=20, color="#ffffff63"),
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(width=2, color="#fff")
                    ),
                    axistick_opts=opts.AxisTickOpts(
                        is_show=True,
                        length=15,
                        linestyle_opts=opts.LineStyleOpts(color="#ffffff1f"),
                    ),
                    splitline_opts=opts.SplitLineOpts(
                        is_show=True, linestyle_opts=opts.LineStyleOpts(color="#ffffff1f")
                    ),
                ),
                legend_opts=opts.LegendOpts(is_show=False),
            )
                .render("linear prediction.html")
        )
        self.browser = QWebEngineView()
        # 加载外部的web界面
        self.browser.load(QUrl('file:///F:/python/python/xxq/qtwj/my/runabao/linear prediction.html'))
        self.setCentralWidget(self.browser)


    def plot_3(self):
        from pyecharts import options as opts
        from pyecharts.charts import Bar
        from pyecharts.commons.utils import JsCode

        c = (
            Bar()
                .add_xaxis(['r0c0', 'r0c1', 'r0c2', 'r1c0', 'r1c1', 'r1c2', 'r2c0', 'r2c1', 'r2c2'])
                .add_yaxis("total", [0, 0, 0, 0, 1, 0, 0, 1, 0], category_gap="50%")
                .set_series_opts(
                itemstyle_opts={
                    "normal": {
                        "color": JsCode(
                            """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                        offset: 0,
                        color: 'rgba(204, 32, 142,1)'
                    }, {
                        offset: 1,
                        color: 'rgba(103, 19, 210, 1)'
                    }], false)"""
                        ),
                        "barBorderRadius": [30, 30, 30, 30],
                        "shadowColor": "rgb(0, 160, 221)",
                    }
                }
            )
                .set_global_opts(title_opts=opts.TitleOpts(title="Defect statistics of different patches"))
                .render("Defect statistics of different patches.html")
        )
        self.browser = QWebEngineView()
        # 加载外部的web界面
        self.browser.load(QUrl('file:///F:/python/python/xxq/qtwj/my/runabao/Defect statistics of different patches.html'))
        self.setCentralWidget(self.browser)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = My_Main_window()
    main_window.show()
    app.exec()