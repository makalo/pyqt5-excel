# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_lan.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1060, 760)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1091, 721))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 511, 681))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setGeometry(QtCore.QRect(530, 360, 511, 311))
        self.groupBox_4.setObjectName("groupBox_4")
        self.textBrowserlog = QtWidgets.QTextBrowser(self.groupBox_4)
        self.textBrowserlog.setGeometry(QtCore.QRect(10, 30, 481, 211))
        self.textBrowserlog.setObjectName("textBrowserlog")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_4)
        self.progressBar.setGeometry(QtCore.QRect(90, 270, 391, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox_4)
        self.lcdNumber.setGeometry(QtCore.QRect(20, 270, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(528, 42, 511, 301))
        self.groupBox.setObjectName("groupBox")
        self.pushButtonbrowse = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonbrowse.setGeometry(QtCore.QRect(30, 60, 113, 51))
        self.pushButtonbrowse.setObjectName("pushButtonbrowse")
        self.pushButtonclear = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonclear.setGeometry(QtCore.QRect(140, 60, 113, 51))
        self.pushButtonclear.setObjectName("pushButtonclear")
        self.pushButtonselall = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonselall.setGeometry(QtCore.QRect(250, 60, 113, 51))
        self.pushButtonselall.setObjectName("pushButtonselall")
        self.pushButtonload = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonload.setGeometry(QtCore.QRect(360, 60, 113, 51))
        self.pushButtonload.setObjectName("pushButtonload")
        self.pushButtonsplit = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonsplit.setGeometry(QtCore.QRect(30, 140, 113, 51))
        self.pushButtonsplit.setObjectName("pushButtonsplit")
        self.pushButtonmerge = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonmerge.setGeometry(QtCore.QRect(140, 140, 113, 51))
        self.pushButtonmerge.setObjectName("pushButtonmerge")
        self.comboBoxfiletype = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxfiletype.setGeometry(QtCore.QRect(30, 230, 101, 26))
        self.comboBoxfiletype.setObjectName("comboBoxfiletype")
        self.pushButtonanalyse = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonanalyse.setGeometry(QtCore.QRect(250, 140, 113, 51))
        self.pushButtonanalyse.setObjectName("pushButtonanalyse")
        self.pushButtonmakalo = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonmakalo.setGeometry(QtCore.QRect(360, 140, 113, 51))
        self.pushButtonmakalo.setObjectName("pushButtonmakalo")
        self.pushButton_link = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_link.setGeometry(QtCore.QRect(260, 210, 201, 61))
        self.pushButton_link.setObjectName("pushButton_link")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 0, 1091, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_confirm_idx = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_confirm_idx.setGeometry(QtCore.QRect(890, 50, 113, 32))
        self.pushButton_confirm_idx.setObjectName("pushButton_confirm_idx")
        self.pushButton_clear_idx = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_clear_idx.setGeometry(QtCore.QRect(890, 20, 113, 32))
        self.pushButton_clear_idx.setObjectName("pushButton_clear_idx")
        self.comboBox_wb = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_wb.setGeometry(QtCore.QRect(170, 20, 481, 26))
        self.comboBox_wb.setObjectName("comboBox_wb")
        self.comboBox_ws = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_ws.setGeometry(QtCore.QRect(170, 50, 481, 26))
        self.comboBox_ws.setObjectName("comboBox_ws")
        self.label_keyidx = QtWidgets.QLabel(self.groupBox_2)
        self.label_keyidx.setGeometry(QtCore.QRect(660, 20, 51, 21))
        self.label_keyidx.setObjectName("label_keyidx")
        self.label_range = QtWidgets.QLabel(self.groupBox_2)
        self.label_range.setGeometry(QtCore.QRect(660, 50, 51, 21))
        self.label_range.setObjectName("label_range")
        self.comboBox_x = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_x.setGeometry(QtCore.QRect(730, 20, 51, 26))
        self.comboBox_x.setObjectName("comboBox_x")
        self.comboBox_y = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_y.setGeometry(QtCore.QRect(780, 20, 91, 26))
        self.comboBox_y.setObjectName("comboBox_y")
        self.comboBox_r1 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_r1.setGeometry(QtCore.QRect(730, 50, 51, 26))
        self.comboBox_r1.setObjectName("comboBox_r1")
        self.comboBox_r2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_r2.setGeometry(QtCore.QRect(780, 50, 91, 26))
        self.comboBox_r2.setObjectName("comboBox_r2")
        self.checkBox_book = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_book.setGeometry(QtCore.QRect(10, 20, 131, 21))
        self.checkBox_book.setChecked(True)
        self.checkBox_book.setObjectName("checkBox_book")
        self.checkBox_sheet = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_sheet.setGeometry(QtCore.QRect(10, 50, 131, 20))
        self.checkBox_sheet.setChecked(True)
        self.checkBox_sheet.setObjectName("checkBox_sheet")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 79, 1091, 611))
        self.groupBox_5.setObjectName("groupBox_5")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_5)
        self.tableWidget.setGeometry(QtCore.QRect(0, 30, 1091, 571))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1060, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "makalo提供技术支持"))
        self.groupBox_3.setTitle(_translate("MainWindow", "兰神专属"))
        self.groupBox_4.setTitle(_translate("MainWindow", "显示区"))
        self.groupBox.setTitle(_translate("MainWindow", "功能区"))
        self.pushButtonbrowse.setText(_translate("MainWindow", "..."))
        self.pushButtonclear.setText(_translate("MainWindow", "clear"))
        self.pushButtonselall.setText(_translate("MainWindow", "select"))
        self.pushButtonload.setText(_translate("MainWindow", "load"))
        self.pushButtonsplit.setText(_translate("MainWindow", "split"))
        self.pushButtonmerge.setText(_translate("MainWindow", "merge"))
        self.pushButtonanalyse.setText(_translate("MainWindow", "analyse"))
        self.pushButtonmakalo.setText(_translate("MainWindow", "makalo"))
        self.pushButton_link.setText(_translate("MainWindow", "联系makalo  提需求"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.groupBox_2.setTitle(_translate("MainWindow", "参数配置"))
        self.pushButton_confirm_idx.setText(_translate("MainWindow", "confirm"))
        self.pushButton_clear_idx.setText(_translate("MainWindow", "clear"))
        self.label_keyidx.setText(_translate("MainWindow", "idx"))
        self.label_range.setText(_translate("MainWindow", "range"))
        self.checkBox_book.setText(_translate("MainWindow", "broadcast books"))
        self.checkBox_sheet.setText(_translate("MainWindow", "broadcast sheets"))
        self.groupBox_5.setTitle(_translate("MainWindow", "excel显示"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "        Home        "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "        Data        "))
