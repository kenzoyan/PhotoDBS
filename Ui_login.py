# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\57070\Desktop\py file\PYQT5\eric6_pyqt5\photoDBS\login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1026, 786)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(12)
        Dialog.setFont(font)
        Dialog.setStyleSheet("QDialog{\n"
"border-image:url(C:/Users/57070/Desktop/py file/PYQT5/eric6_pyqt5/photoDBS/photos/loginphoto.jpg);\n"
"}")
        Dialog.setSizeGripEnabled(True)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(400, 290, 91, 31))
        font = QtGui.QFont()
        font.setFamily("方正兰亭超细黑简体")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"background:rgb(0, 85, 127);\n"
"color:rgb(255, 255, 255);\n"
"min-width:5em;\n"
"padding:6px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(224,0,0);\n"
"border-style: inset;\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(400, 350, 91, 31))
        font = QtGui.QFont()
        font.setFamily("方正兰亭超细黑简体")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"background:rgb(0, 85, 127);\n"
"color:rgb(255, 255, 255);\n"
"min-width:5em;\n"
"padding:6px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(224,0,0);\n"
"border-style: inset;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(380, 110, 291, 61))
        font = QtGui.QFont()
        font.setFamily("方正兰亭超细黑简体")
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color: transparent;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(940, 760, 91, 31))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color: transparent;\n"
"}\n"
"")
        self.label_4.setObjectName("label_4")
        self.username = QtWidgets.QLineEdit(Dialog)
        self.username.setGeometry(QtCore.QRect(490, 290, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.username.setFont(font)
        self.username.setStyleSheet("QLineEdit {\n"
"\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"font: bold 14px;\n"
"min-width:10em;\n"
"padding:6px;\n"
"}")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(490, 350, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setStyleSheet("QLineEdit {\n"
"\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"font: bold 14px;\n"
"min-width:10em;\n"
"padding:6px;\n"
"}")
        self.password.setObjectName("password")
        #设置小黑点
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(380, 550, 301, 61))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(28)
        font.setUnderline(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel{\n"
"background-color: transparent;\n"
"color:black;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(570, 610, 321, 51))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{\n"
"background-color: transparent;\n"
"color:black;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setGeometry(QtCore.QRect(420, 460, 91, 41))
        font = QtGui.QFont()
        font.setFamily("方正兰亭超细黑简体")
        font.setPointSize(14)
        self.okButton.setFont(font)
        self.okButton.setStyleSheet("QPushButton {\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"background:rgb(0, 85, 127);\n"
"color:rgb(255, 255, 255);\n"
"min-width:5em;\n"
"padding:6px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(224,0,0);\n"
"border-style: inset;\n"
"}")
        self.okButton.setObjectName("okButton")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(530, 460, 91, 41))
        font = QtGui.QFont()
        font.setFamily("方正兰亭超细黑简体")
        font.setPointSize(14)
        self.cancelButton.setFont(font)
        self.cancelButton.setStyleSheet("QPushButton {\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"background:rgb(0, 85, 127);\n"
"color:rgb(255, 255, 255);\n"
"min-width:5em;\n"
"padding:6px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(224,0,0);\n"
"border-style: inset;\n"
"}")
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(Dialog)
        self.okButton.clicked.connect(Dialog.accept)
        self.cancelButton.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "图片管理系统"))
        self.label.setText(_translate("Dialog", "用户名"))
        self.label_2.setText(_translate("Dialog", "密    码"))
        self.label_3.setText(_translate("Dialog", "图片管理系统"))
        self.label_4.setText(_translate("Dialog", "by Kenzo Yan"))
        self.label_5.setText(_translate("Dialog", "有光即可摄影!"))
        self.label_6.setText(_translate("Dialog", "——阿尔弗莱德•史迪格里兹"))
        self.okButton.setText(_translate("Dialog", "登录"))
        self.cancelButton.setText(_translate("Dialog", "退出"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

