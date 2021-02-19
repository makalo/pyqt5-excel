# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_lan.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
class ComboBoxNEW(QtWidgets.QComboBox):
    popupAboutToBeShown = QtCore.pyqtSignal()

    def showPopup(self):
        self.popupAboutToBeShown.emit()
        super(ComboBoxNEW, self).showPopup()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(946, 675)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 911, 601))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 401, 551))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(420, 10, 481, 551))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        self.pushButtonbrowse = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonbrowse.setGeometry(QtCore.QRect(0, 20, 113, 51))
        self.pushButtonbrowse.setObjectName("pushButtonbrowse")
        self.pushButtonclear = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonclear.setGeometry(QtCore.QRect(110, 20, 113, 51))
        self.pushButtonclear.setObjectName("pushButtonclear")
        self.pushButtonselall = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonselall.setGeometry(QtCore.QRect(220, 20, 113, 51))
        self.pushButtonselall.setObjectName("pushButtonselall")
        self.pushButtonload = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonload.setGeometry(QtCore.QRect(330, 20, 113, 51))
        self.pushButtonload.setObjectName("pushButtonload")
        self.comboBoxfiletypeX = ComboBoxNEW(self.groupBox)
        self.comboBoxfiletypeX.setGeometry(QtCore.QRect(30, 160, 101, 26))
        self.comboBoxfiletypeX.setObjectName("comboBoxfiletypeX")
        self.pushButtonsplit = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonsplit.setGeometry(QtCore.QRect(0, 80, 113, 51))
        self.pushButtonsplit.setObjectName("pushButtonsplit")
        self.pushButtonmerge = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonmerge.setGeometry(QtCore.QRect(110, 80, 113, 51))
        self.pushButtonmerge.setObjectName("pushButtonmerge")
        self.labelx = QtWidgets.QLabel(self.groupBox)
        self.labelx.setGeometry(QtCore.QRect(15, 161, 16, 20))
        self.labelx.setObjectName("labelx")
        self.comboBoxfiletype = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxfiletype.setGeometry(QtCore.QRect(280, 160, 101, 26))
        self.comboBoxfiletype.setObjectName("comboBoxfiletype")
        self.pushButtonanalyse = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonanalyse.setGeometry(QtCore.QRect(220, 80, 113, 51))
        self.pushButtonanalyse.setObjectName("pushButtonanalyse")
        self.pushButtonmakalo = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonmakalo.setGeometry(QtCore.QRect(330, 80, 113, 51))
        self.pushButtonmakalo.setObjectName("pushButtonmakalo")
        self.labely = QtWidgets.QLabel(self.groupBox)
        self.labely.setGeometry(QtCore.QRect(145, 161, 16, 20))
        self.labely.setObjectName("labely")
        self.comboBoxfiletypeY = ComboBoxNEW(self.groupBox)
        self.comboBoxfiletypeY.setGeometry(QtCore.QRect(160, 160, 101, 26))
        self.comboBoxfiletypeY.setObjectName("comboBoxfiletypeY")
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_4 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.textBrowserlog = QtWidgets.QTextBrowser(self.groupBox_4)
        self.textBrowserlog.setGeometry(QtCore.QRect(10, 30, 461, 141))
        self.textBrowserlog.setObjectName("textBrowserlog")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_4)
        self.progressBar.setGeometry(QtCore.QRect(90, 190, 361, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox_4)
        self.lcdNumber.setGeometry(QtCore.QRect(20, 190, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout.addWidget(self.groupBox_4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(25, 21, 881, 551))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 946, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.comboBoxfiletypeY.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setWindowOpacity(0.9)  # 设置窗口透明度
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_3.setTitle(_translate("MainWindow", "兰神专属"))
        self.groupBox.setTitle(_translate("MainWindow", "功能区"))
        self.pushButtonbrowse.setText(_translate("MainWindow", "..."))
        self.pushButtonclear.setText(_translate("MainWindow", "clear"))
        self.pushButtonselall.setText(_translate("MainWindow", "select all"))
        self.pushButtonload.setText(_translate("MainWindow", "load"))
        self.pushButtonsplit.setText(_translate("MainWindow", "split"))
        self.pushButtonmerge.setText(_translate("MainWindow", "merge"))
        self.labelx.setText(_translate("MainWindow", " X"))
        self.pushButtonanalyse.setText(_translate("MainWindow", "analyse"))
        self.pushButtonmakalo.setText(_translate("MainWindow", "makalo"))
        self.labely.setText(_translate("MainWindow", " Y"))
        self.groupBox_4.setTitle(_translate("MainWindow", "显示区"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "        Home        "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "        Data        "))






