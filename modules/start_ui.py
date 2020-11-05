# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Admin\PycharmProjects\OSINT\modules\start.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogStart(object):
    def setupUi(self, DialogStart):
        DialogStart.setObjectName("DialogStart")
        DialogStart.resize(451, 471)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogStart.sizePolicy().hasHeightForWidth())
        DialogStart.setSizePolicy(sizePolicy)
        DialogStart.setMinimumSize(QtCore.QSize(451, 471))
        DialogStart.setMaximumSize(QtCore.QSize(451, 471))
        self.textBrowser = QtWidgets.QTextBrowser(DialogStart)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 451, 471))
        self.textBrowser.setMinimumSize(QtCore.QSize(451, 471))
        self.textBrowser.setMaximumSize(QtCore.QSize(451, 471))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(DialogStart)
        QtCore.QMetaObject.connectSlotsByName(DialogStart)

    def retranslateUi(self, DialogStart):
        _translate = QtCore.QCoreApplication.translate
        DialogStart.setWindowTitle(_translate("DialogStart", "Подготовка"))
        self.textBrowser.setHtml(_translate("DialogStart", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
