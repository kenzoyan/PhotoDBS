# -*- coding: utf-8 -*-

"""
Module implementing login.
"""
import sys
#import qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Ui_login import Ui_Dialog
from mainwindow import  MainWindow

class login(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(login, self).__init__(parent)
        self.setupUi(self)
        self.mainwindow=MainWindow()
        self.okButton.clicked.connect(self.okButton_clicked)
    @pyqtSlot()
    def okButton_clicked(self):
        
        # 设置验证
        
        name = self.username.text()
        psw= self.password.text()
        if (name == "" or psw == ""):
            QMessageBox.warning(self, "警告", "学号和密码不可为空!", QMessageBox.Yes, QMessageBox.Yes)
            
        if(name=='kenzo'):
            if(psw=='123456'):
                QMessageBox.information(self, "登陆成功", "登陆成功！", QMessageBox.Yes, QMessageBox.Yes)
                self.mainwindow.show()
                self.mainwindow.showName.emit(name)
            else:
                QMessageBox.warning(self, "警告", "密码错误!", QMessageBox.Yes, QMessageBox.Yes)
                
    
        
        
    

if   __name__=='__main__':
    app=QApplication(sys.argv)
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    login=login()
    login.show()
    sys.exit(app.exec_())
