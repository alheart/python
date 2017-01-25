# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Code\Git\python\gui\eric\AutoTerm\autoterm.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(705, 367)
        Dialog.setSizeGripEnabled(True)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 101, 31))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.serialText = QtWidgets.QTextBrowser(Dialog)
        self.serialText.setGeometry(QtCore.QRect(160, 50, 311, 41))
        self.serialText.setObjectName("serialText")
        self.macText = QtWidgets.QTextBrowser(Dialog)
        self.macText.setGeometry(QtCore.QRect(160, 120, 311, 41))
        self.macText.setObjectName("macText")
        self.startBtn = QtWidgets.QPushButton(Dialog)
        self.startBtn.setGeometry(QtCore.QRect(160, 180, 121, 51))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.startBtn.setFont(font)
        self.startBtn.setObjectName("startBtn")
        self.optionBtn = QtWidgets.QPushButton(Dialog)
        self.optionBtn.setGeometry(QtCore.QRect(390, 200, 75, 31))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.optionBtn.setFont(font)
        self.optionBtn.setObjectName("optionBtn")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 280, 71, 21))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.statusLabel = QtWidgets.QLabel(Dialog)
        self.statusLabel.setGeometry(QtCore.QRect(120, 280, 441, 21))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(14)
        self.statusLabel.setFont(font)
        self.statusLabel.setText("")
        self.statusLabel.setObjectName("statusLabel")
        self.prosBar = QtWidgets.QProgressBar(Dialog)
        self.prosBar.setGeometry(QtCore.QRect(30, 320, 551, 23))
        self.prosBar.setProperty("value", 0)
        self.prosBar.setObjectName("prosBar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Serial:"))
        self.label_2.setText(_translate("Dialog", "MAC:"))
        self.startBtn.setText(_translate("Dialog", "Start"))
        self.optionBtn.setText(_translate("Dialog", "Option"))
        self.label_3.setText(_translate("Dialog", "[Idle]"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

