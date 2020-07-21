# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messenger.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(590, 532)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.l_name = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_name.setFont(font)
        self.l_name.setObjectName("l_name")
        self.gridLayout.addWidget(self.l_name, 0, 0, 1, 3)
        self.lE_login = QtWidgets.QLineEdit(self.centralwidget)
        self.lE_login.setObjectName("lE_login")
        self.gridLayout.addWidget(self.lE_login, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(91, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.lE_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lE_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lE_password.setObjectName("lE_password")
        self.gridLayout.addWidget(self.lE_password, 1, 2, 1, 1)
        self.tB_chat = QtWidgets.QTextBrowser(self.centralwidget)
        self.tB_chat.setReadOnly(True)
        self.tB_chat.setObjectName("tB_chat")
        self.gridLayout.addWidget(self.tB_chat, 2, 0, 1, 3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tE_message = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tE_message.sizePolicy().hasHeightForWidth())
        self.tE_message.setSizePolicy(sizePolicy)
        self.tE_message.setMaximumSize(QtCore.QSize(16777215, 92))
        self.tE_message.setObjectName("tE_message")
        self.horizontalLayout.addWidget(self.tE_message)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 46, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.pB_send = QtWidgets.QPushButton(self.centralwidget)
        self.pB_send.setObjectName("pB_send")
        self.verticalLayout.addWidget(self.pB_send)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.l_name.setText(_translate("MainWindow", "Chibis Messenger"))
        self.lE_login.setPlaceholderText(_translate("MainWindow", "Login"))
        self.lE_password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.tE_message.setPlaceholderText(_translate("MainWindow", "Message"))
        self.pB_send.setText(_translate("MainWindow", "Send"))