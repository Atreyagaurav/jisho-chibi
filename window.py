# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import os

def resource(path):
    return os.path.join(os.path.dirname(__file__), path)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(236, 196)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolSync = QtWidgets.QToolButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource("./icons/auto.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolSync.setIcon(icon)
        self.toolSync.setObjectName("toolSync")
        self.horizontalLayout.addWidget(self.toolSync)
        self.txtClip = QtWidgets.QLineEdit(self.centralwidget)
        self.txtClip.setObjectName("txtClip")
        self.horizontalLayout.addWidget(self.txtClip)
        self.btnSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearch.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(resource("./icons/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSearch.setIcon(icon1)
        self.btnSearch.setObjectName("btnSearch")
        self.horizontalLayout.addWidget(self.btnSearch)
        self.btnPrev = QtWidgets.QPushButton(self.centralwidget)
        self.btnPrev.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(resource("./icons/prev.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPrev.setIcon(icon2)
        self.btnPrev.setObjectName("btnPrev")
        self.horizontalLayout.addWidget(self.btnPrev)
        self.btnNext = QtWidgets.QPushButton(self.centralwidget)
        self.btnNext.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(resource("./icons/next.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNext.setIcon(icon3)
        self.btnNext.setObjectName("btnNext")
        self.horizontalLayout.addWidget(self.btnNext)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webEngineView.sizePolicy().hasHeightForWidth())
        self.webEngineView.setSizePolicy(sizePolicy)
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")
        self.verticalLayout.addWidget(self.webEngineView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 236, 20))
        self.menubar.setObjectName("menubar")
        self.menuJisho = QtWidgets.QMenu(self.menubar)
        self.menuJisho.setObjectName("menuJisho")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuClipboard = QtWidgets.QMenu(self.menuOptions)
        self.menuClipboard.setObjectName("menuClipboard")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSearchInJishoWeb = QtWidgets.QAction(MainWindow)
        self.actionSearchInJishoWeb.setObjectName("actionSearchInJishoWeb")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionPrimarySelection = QtWidgets.QAction(MainWindow)
        self.actionPrimarySelection.setCheckable(True)
        self.actionPrimarySelection.setChecked(True)
        self.actionPrimarySelection.setObjectName("actionPrimarySelection")
        self.actionClipboard_2 = QtWidgets.QAction(MainWindow)
        self.actionClipboard_2.setCheckable(True)
        self.actionClipboard_2.setObjectName("actionClipboard_2")
        self.actionPreviousSearch = QtWidgets.QAction(MainWindow)
        self.actionPreviousSearch.setObjectName("actionPreviousSearch")
        self.actionNextSearch = QtWidgets.QAction(MainWindow)
        self.actionNextSearch.setObjectName("actionNextSearch")
        self.actionGithub = QtWidgets.QAction(MainWindow)
        self.actionGithub.setObjectName("actionGithub")
        self.actionClearSearchHistory = QtWidgets.QAction(MainWindow)
        self.actionClearSearchHistory.setObjectName("actionClearSearchHistory")
        self.actionHide = QtWidgets.QAction(MainWindow)
        self.actionHide.setObjectName("actionHide")
        self.actionNextResult = QtWidgets.QAction(MainWindow)
        self.actionNextResult.setObjectName("actionNextResult")
        self.actionPreviousResult = QtWidgets.QAction(MainWindow)
        self.actionPreviousResult.setObjectName("actionPreviousResult")
        self.menuJisho.addAction(self.actionSearchInJishoWeb)
        self.menuJisho.addAction(self.actionNextResult)
        self.menuJisho.addAction(self.actionPreviousResult)
        self.menuJisho.addAction(self.actionPreviousSearch)
        self.menuJisho.addAction(self.actionNextSearch)
        self.menuJisho.addAction(self.actionHide)
        self.menuJisho.addAction(self.actionExit)
        self.menuClipboard.addAction(self.actionPrimarySelection)
        self.menuClipboard.addAction(self.actionClipboard_2)
        self.menuOptions.addAction(self.menuClipboard.menuAction())
        self.menuOptions.addAction(self.actionClearSearchHistory)
        self.menuAbout.addAction(self.actionGithub)
        self.menubar.addAction(self.menuJisho.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Jisho Chibi"))
        self.toolSync.setToolTip(_translate("MainWindow", "Sync with Selection/Clipboard"))
        self.toolSync.setText(_translate("MainWindow", "..."))
        self.btnSearch.setToolTip(_translate("MainWindow", "Search from Textbar"))
        self.btnPrev.setToolTip(_translate("MainWindow", "Previous Definition"))
        self.btnNext.setToolTip(_translate("MainWindow", "Next Definition"))
        self.menuJisho.setTitle(_translate("MainWindow", "jisho"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuClipboard.setTitle(_translate("MainWindow", "Clipboard"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionSearchInJishoWeb.setText(_translate("MainWindow", "Search in Jisho Web"))
        self.actionSearchInJishoWeb.setShortcut(_translate("MainWindow", "W"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Q"))
        self.actionPrimarySelection.setText(_translate("MainWindow", "Primary/Selection"))
        self.actionClipboard_2.setText(_translate("MainWindow", "Clipboard"))
        self.actionPreviousSearch.setText(_translate("MainWindow", "Previous Search"))
        self.actionPreviousSearch.setShortcut(_translate("MainWindow", "PgUp, Up"))
        self.actionNextSearch.setText(_translate("MainWindow", "Next Search"))
        self.actionNextSearch.setShortcut(_translate("MainWindow", "PgDown, Down"))
        self.actionGithub.setText(_translate("MainWindow", "Github"))
        self.actionClearSearchHistory.setText(_translate("MainWindow", "Clear Search History"))
        self.actionClearSearchHistory.setShortcut(_translate("MainWindow", "Del"))
        self.actionHide.setText(_translate("MainWindow", "Hide"))
        self.actionHide.setShortcut(_translate("MainWindow", "Esc"))
        self.actionNextResult.setText(_translate("MainWindow", "Next Result"))
        self.actionNextResult.setShortcut(_translate("MainWindow", "Right, N"))
        self.actionPreviousResult.setText(_translate("MainWindow", "Previous Result"))
        self.actionPreviousResult.setShortcut(_translate("MainWindow", "Left, P"))
from PyQt5 import QtWebEngineWidgets
