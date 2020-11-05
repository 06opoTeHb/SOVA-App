# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'share.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogShare(object):
    def setupUi(self, DialogShare):
        DialogShare.setObjectName("DialogShare")
        DialogShare.resize(510, 141)
        DialogShare.setMaximumSize(QtCore.QSize(16777215, 141))
        self.label = QtWidgets.QLabel(DialogShare)
        self.label.setGeometry(QtCore.QRect(0, 0, 121, 141))
        self.label.setMinimumSize(QtCore.QSize(121, 141))
        self.label.setText("")
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(DialogShare)
        self.layoutWidget.setGeometry(QtCore.QRect(140, 17, 353, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.retranslateUi(DialogShare)
        QtCore.QMetaObject.connectSlotsByName(DialogShare)

    def retranslateUi(self, DialogShare):
        _translate = QtCore.QCoreApplication.translate
        DialogShare.setWindowTitle(_translate("DialogShare", "Поддержка"))
        self.label_2.setText(_translate("DialogShare", "Автор: У.А.В."))
        self.label_4.setText(_translate("DialogShare", "По вопросам обращаться:"))
        self.label_3.setText(_translate("DialogShare", "E-MAIL: sova_app@inbox.ru"))
