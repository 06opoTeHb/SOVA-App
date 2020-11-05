# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Admin\PycharmProjects\OSINT\modules\license.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogLicense(object):
    def setupUi(self, DialogLicense):
        DialogLicense.setObjectName("DialogLicense")
        DialogLicense.resize(471, 480)
        DialogLicense.setMinimumSize(QtCore.QSize(471, 480))
        DialogLicense.setMaximumSize(QtCore.QSize(471, 480))
        self.textBrowser = QtWidgets.QTextBrowser(DialogLicense)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 471, 480))
        self.textBrowser.setMinimumSize(QtCore.QSize(471, 480))
        self.textBrowser.setMaximumSize(QtCore.QSize(471, 480))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        self.textBrowser.setFont(font)
        self.textBrowser.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textBrowser.setOpenLinks(False)
        self.textBrowser.setObjectName("textBrowser")
        self.pb_InStart = QtWidgets.QPushButton(DialogLicense)
        self.pb_InStart.setGeometry(QtCore.QRect(190, 440, 75, 23))
        self.pb_InStart.setObjectName("pb_InStart")

        self.retranslateUi(DialogLicense)
        QtCore.QMetaObject.connectSlotsByName(DialogLicense)

    def retranslateUi(self, DialogLicense):
        _translate = QtCore.QCoreApplication.translate
        DialogLicense.setWindowTitle(_translate("DialogLicense", "Лицензии"))
        self.pb_InStart.setText(_translate("DialogLicense", " В начало"))
