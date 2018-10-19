# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import sys
#import qdarkstyle
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from Ui_mainwindow import Ui_MainWindow
from photos import pictures
from photographers import photographers
from devices import devices
from pic_group import picgroup
from people_group import peogroup

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    showName=pyqtSignal(str)
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.enterpic.clicked.connect(self.slotpictures)
        self.enterpeople.clicked.connect(self.slotphotographers)
        self.enterdevices.clicked.connect(self.slotdevices)
        self.enterpicgroup.clicked.connect(self.slotpicgroup)
        self.enterpeogroup.clicked.connect(self.slotpeogroup) 
        self.showName[str].connect(self.addname)   
    
    def slotpictures(self):
        self.pictures=pictures()
        self.pictures.show()  
    def slotphotographers(self):
        self.photographers=photographers()
        self.photographers.show()
    def slotdevices(self):
        self.devices=devices()
        self.devices.show()
    def slotpicgroup(self):
        self.picgroup=picgroup()
        self.picgroup.show()
    def slotpeogroup(self):
        self.peogroup=peogroup()
        self.peogroup.show()    
    def addname(self, text):
        words="WELCOME "+text+" !"
        self.welcome_words.setText(words)
        
        
if  __name__=='__main__':
    app=QApplication(sys.argv)
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainwindow=MainWindow()
    #mainwindow.showName.emit('kenzo')
    mainwindow.show()
    sys.exit(app.exec_())
    
