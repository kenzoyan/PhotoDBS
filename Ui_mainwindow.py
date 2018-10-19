# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\57070\Desktop\py file\PYQT5\eric6_pyqt5\photoDBS\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 888)
        MainWindow.setStyleSheet("QMainWindow{\n"
"border-image:url(C:/Users/57070/Desktop/py file/PYQT5/eric6_pyqt5/photoDBS/photos/mainwindow1.jpg);\n"
"}")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.maintitle = QtWidgets.QLabel(self.centralWidget)
        self.maintitle.setGeometry(QtCore.QRect(400, 70, 301, 81))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(28)
        self.maintitle.setFont(font)
        self.maintitle.setStyleSheet("QLabel{\n"
"border：none;\n"
"border-radius：5px;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"")
        self.maintitle.setObjectName("maintitle")
        self.welcome_words = QtWidgets.QLabel(self.centralWidget)
        self.welcome_words.setGeometry(QtCore.QRect(430, 200, 261, 51))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(16)
        self.welcome_words.setFont(font)
        self.welcome_words.setStyleSheet("QLabel{\n"
"border：none;\n"
"border-radius：5px;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"")
        self.welcome_words.setObjectName("welcome_words")
        self.layoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(440, 310, 211, 471))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.enterpic = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.enterpic.setFont(font)
        self.enterpic.setStyleSheet("QPushButton {\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"background:rgb(204, 188, 255);\n"
"color:rgb(255, 255, 255);\n"
"min-width:10em;\n"
"padding:6px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(224,0,0);\n"
"border-style: inset;\n"
"}")
        self.enterpic.setObjectName("enterpic")
        self.verticalLayout.addWidget(self.enterpic)
        self.enterpeople = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.enterpeople.setFont(font)
        self.enterpeople.setStyleSheet("QPushButton {\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"background:rgb(204, 188, 255);\n"
"color:rgb(255, 255, 255);\n"
"min-width:10em;\n"
"padding:6px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(224,0,0);\n"
"border-style: inset;\n"
"}")
        self.enterpeople.setObjectName("enterpeople")
        self.verticalLayout.addWidget(self.enterpeople)
        self.enterdevices = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.enterdevices.setFont(font)
        self.enterdevices.setStyleSheet("QPushButton {\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"background:rgb(204, 188, 255);\n"
"color:rgb(255, 255, 255);\n"
"min-width:10em;\n"
"padding:6px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(224,0,0);\n"
"border-style: inset;\n"
"}")
        self.enterdevices.setObjectName("enterdevices")
        self.verticalLayout.addWidget(self.enterdevices)
        self.enterpicgroup = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.enterpicgroup.setFont(font)
        self.enterpicgroup.setStyleSheet("QPushButton {\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"background:rgb(204, 188, 255);\n"
"color:rgb(255, 255, 255);\n"
"min-width:10em;\n"
"padding:6px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(224,0,0);\n"
"border-style: inset;\n"
"}")
        self.enterpicgroup.setObjectName("enterpicgroup")
        self.verticalLayout.addWidget(self.enterpicgroup)
        self.enterpeogroup = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(20)
        self.enterpeogroup.setFont(font)
        self.enterpeogroup.setStyleSheet("QPushButton {\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"background:rgb(204, 188, 255);\n"
"color:rgb(255, 255, 255);\n"
"min-width:10em;\n"
"padding:6px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(224,0,0);\n"
"border-style: inset;\n"
"}")
        self.enterpeogroup.setObjectName("enterpeogroup")
        self.verticalLayout.addWidget(self.enterpeogroup)
        self.layoutWidget.raise_()
        self.welcome_words.raise_()
        self.maintitle.raise_()
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.maintitle.setText(_translate("MainWindow", "图片管理系统"))
        self.welcome_words.setText(_translate("MainWindow", "WELCOME, kenzo"))
        self.enterpic.setText(_translate("MainWindow", "照片管理"))
        self.enterpeople.setText(_translate("MainWindow", "摄影师管理"))
        self.enterdevices.setText(_translate("MainWindow", "设备管理"))
        self.enterpicgroup.setText(_translate("MainWindow", "图片分组"))
        self.enterpeogroup.setText(_translate("MainWindow", "摄影师分组"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

