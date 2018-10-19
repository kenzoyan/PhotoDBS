# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtSql import *


class peogroup(QWidget):
    def __init__(self):
        super(peogroup, self).__init__()
        self.resize(700, 500)
        self.setWindowTitle("摄影师分组管理")
        # 查询模型
        self.queryModel = None
        # 数据表
        self.tableView = None
        # 当前页
        self.currentPage = 0
        # 总页数
        self.totalPage = 0
        # 总记录数
        self.totalRecord = 0
        # 每页数据数
        self.pageRecord = 10
        self.setUpUI()

    def setUpUI(self):
        self.layout = QVBoxLayout()
        self.Hlayout1 = QHBoxLayout()
        self.Hlayout2 = QHBoxLayout()

       # Hlayout1控件的初始化
        self.searchEdit = QLineEdit()
        self.searchEdit.setStyleSheet("QLineEdit {\n"
"\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"font: bold 14px;\n"
"min-width:10em;\n"
"padding:6px;\n"
"}")
        self.searchEdit.setFixedHeight(32)
        font = QFont()
        font.setPixelSize(15)
        self.searchEdit.setFont(font)

        self.searchButton = QPushButton("查询")
        self.searchButton.setFixedHeight(32)
        self.searchButton.setFont(font)
        #self.searchButton.setIcon(QIcon(QPixmap("./images/search.png")))
        self.searchButton.setStyleSheet("QPushButton {\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"background:rgb(240,195,186);\n"
"color:rgb(255, 255, 255);\n"
"min-width:5em;\n"
"padding:6px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(224,0,0);\n"
"border-style: inset;\n"
"}")

        self.condisionComboBox = QComboBox()
        self.condisionComboBox.setStyleSheet("QComboBox {\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"background:rgb(216,0,102);\n"
"color:rgb(255, 255, 255);\n"
"min-width:7em;\n"
"padding:6px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(224,0,0);\n"
"border-style: inset;\n"
"}")
        searchCondision = ['按分组查询','按分组编号查询',  '按分组人数查询']
        self.condisionComboBox.setFixedHeight(32)
        self.condisionComboBox.setFont(font)
        self.condisionComboBox.addItems(searchCondision)

        self.Hlayout1.addWidget(self.searchEdit)
        self.Hlayout1.addWidget(self.searchButton)
        self.Hlayout1.addWidget(self.condisionComboBox)

        # Hlayout2初始化
        self.jumpToLabel = QLabel("跳转到第")
        self.pageEdit = QLineEdit()
        self.pageEdit.setFixedWidth(30)
        s = "/" + str(self.totalPage) + "页"
        self.pageLabel = QLabel(s)
        self.jumpToButton = QPushButton("跳转")
        self.jumpToButton.setStyleSheet("QPushButton {\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"background:rgb(202,160,102);\n"
"color:rgb(255, 255, 255);\n"
"min-width:4em;\n"
"padding:6px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(224,0,0);\n"
"border-style: inset;\n"
"}")
        self.prevButton = QPushButton("前一页")
        self.prevButton.setStyleSheet("QPushButton {\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"background:rgb(202,160,102);\n"
"color:rgb(255, 255, 255);\n"
"min-width:4em;\n"
"padding:6px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(224,0,0);\n"
"border-style: inset;\n"
"}")
        self.prevButton.setFixedWidth(60)
        self.backButton = QPushButton("后一页")
        self.backButton.setStyleSheet("QPushButton {\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"background:rgb(202,160,102);\n"
"color:rgb(255, 255, 255);\n"
"min-width:4em;\n"
"padding:6px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(224,0,0);\n"
"border-style: inset;\n"
"}")
        self.backButton.setFixedWidth(60)
        self.addButton=QPushButton("添加")
        self.addButton.setStyleSheet("QPushButton {\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"background:rgb(202,160,102);\n"
"color:rgb(255, 255, 255);\n"
"min-width:4em;\n"
"padding:6px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(224,0,0);\n"
"border-style: inset;\n"
"}")
        self.deleteButton=QPushButton("删除")
        self.deleteButton.setStyleSheet("QPushButton {\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"background:rgb(202,160,102);\n"
"color:rgb(255, 255, 255);\n"
"min-width:4em;\n"
"padding:6px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(224,0,0);\n"
"border-style: inset;\n"
"}")
        self.submitButton=QPushButton("提交")
        self.submitButton.setStyleSheet("QPushButton {\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"background:rgb(202,160,102);\n"
"color:rgb(255, 255, 255);\n"
"min-width:4em;\n"
"padding:6px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(224,0,0);\n"
"border-style: inset;\n"
"}")
        
        
        
        Hlayout = QHBoxLayout()
        Hlayout.addWidget(self.addButton)
        Hlayout.addWidget(self.submitButton)
        Hlayout.addWidget(self.jumpToLabel)
        Hlayout.addWidget(self.pageEdit)
        Hlayout.addWidget(self.pageLabel)
        Hlayout.addWidget(self.jumpToButton)
        Hlayout.addWidget(self.prevButton)
        Hlayout.addWidget(self.backButton)
        Hlayout.addWidget(self.deleteButton)

        widget = QWidget()
        widget.setLayout(Hlayout)
        widget.setFixedWidth(600)
        self.Hlayout2.addWidget(widget)

        # tableView
       
        #self.db = QSqlDatabase.addDatabase("QSQLITE")
        #self.db.setDatabaseName('./db/LibraryManagement.db')
        '''self.db=pymysql.connect(host='localhost', user='root',passwd='123456',  db='test',charset='utf8')  
        self.cur=self.db.cursor()
        self.cur.execute('SELECT VERSION()')
        data=self.cur.fetchall()
        print('Database version : %s'% data) 
        '''
        self.db=QSqlDatabase.addDatabase('QMYSQL','mysql')
        self.db.setDatabaseName('test')
        self.db.setHostName('localhost')
        self.db.setUserName('root')
        self.db.setPassword('123456')
        if(self.db.open()):
            print('success')
        else:
            print(self.db.lastError().text())
        self.db.open()
        print(self.db.tables())
        
        self.tableView = QTableView()
        self.tableView.setStyleSheet("QTableView{\n" 
"color: rgb(0, 0, 0); \n" 
"border: 1px solid #C07010;          /*边框颜色*/  \n"
" gridline-color:#C07010;             /*grid线颜色*/ \n" 
" background-color: transparent;  \n"
" alternate-background-color: rgb(200, 200, 200); /*行交替颜色*/  \n"
" selection-background-color: rgb(58, 116, 150); /*选中行背景颜色*/ \n" 
"}  \n"
"QTableView::item:!alternate:!selected{  \n"
"    background-color: rgb(220, 220, 220);    /*交替行的另一颜色*/  \n"
"}  \n"
"QHeaderView::section{  \n"
"   background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(80, 80, 80, 255), stop:1 rgba(30, 30, 30, 255));  \n"
"    color: rgb(202,160,102);  \n"
"    padding-left: 4px;  \n"
"    border: 1px solid #C07010;  \n"
"    min-height: 30px;  \n"
"}  \n"
)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.queryModel = QSqlTableModel(self, self.db)
        self.queryModel.setTable("people_group")
        self.queryModel.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.queryModel.setSort(0, Qt.AscendingOrder)
        self.queryModel.select()
        print(self.queryModel.lastError().text())
        self.searchButtonClicked()
        self.tableView.setModel(self.queryModel)
        
        self.queryModel.setHeaderData(0, Qt.Horizontal, "分组编号")
        self.queryModel.setHeaderData(1, Qt.Horizontal, "名称")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "人数")
        
        self.queryModel.select()
        
        self.layout.addLayout(self.Hlayout1)
        self.layout.addWidget(self.tableView)
        self.layout.addLayout(self.Hlayout2)
        self.setLayout(self.layout)
        self.searchButton.clicked.connect(self.searchButtonClicked)
        self.prevButton.clicked.connect(self.prevButtonClicked)
        self.backButton.clicked.connect(self.backButtonClicked)
        self.jumpToButton.clicked.connect(self.jumpToButtonClicked)
        self.searchEdit.returnPressed.connect(self.searchButtonClicked)
        self.addButton.clicked.connect(self.addRecord)
        self.deleteButton.clicked.connect(self.deleteRecord)
        self.submitButton.clicked.connect(self.submitRecord)
    def setButtonStatus(self):
        if(self.currentPage==self.totalPage):
            self.prevButton.setEnabled(True)
            self.backButton.setEnabled(False)
        if(self.currentPage==1):
            self.backButton.setEnabled(True)
            self.prevButton.setEnabled(False)
        if(self.currentPage<self.totalPage and self.currentPage>1):
            self.prevButton.setEnabled(True)
            self.backButton.setEnabled(True)

    # 得到记录数
    def getTotalRecordCount(self):
        
        self.queryModel.select()
        self.totalRecord = self.queryModel.rowCount()
        print(self.totalRecord)
        
        return

    # 得到总页数
    def getPageCount(self):
        self.getTotalRecordCount()
        # 上取整
        self.totalPage = int((self.totalRecord + self.pageRecord - 1) / self.pageRecord)
        return
    # 分页记录查询
    def recordQuery(self, index):
        conditionChoice = self.condisionComboBox.currentText()
        if (conditionChoice == '按分组查询'):
            conditionChoice = 'peogroup_name'
            self.input= self.searchEdit.text()
            self.allCondition=conditionChoice+"='"+str(self.input)+"'"
        elif (conditionChoice == '按分组编号查询'):
            conditionChoice = 'people_group.peogroup_id'
            self.input= self.searchEdit.text()
            self.allCondition=conditionChoice+"="+str(self.input)
        elif (conditionChoice == '按分组人数查询'):
            conditionChoice = 'peogroup_number'
            self.input= self.searchEdit.text()
            self.allCondition=conditionChoice+"="+str(self.input)
       

        if (self.searchEdit.text() == ""):
            
            self.queryModel.setFilter("peogroup_id>0")
            self.queryModel.select()
            self.totalRecord = self.queryModel.rowCount()
            self.totalPage = int((self.totalRecord + self.pageRecord - 1) / self.pageRecord)
            label = "/" + str(int(self.totalPage)) + "页"
            self.pageLabel.setText(label)
            #self.queryModel.select()
            self.setButtonStatus()
        else:
            
            print(self.allCondition)
            self.queryModel.setFilter(self.allCondition)
            self.queryModel.select()
            print(self.queryModel.lastError().text())
            self.totalRecord = self.queryModel.rowCount()
        
        # 当查询无记录时的操作
        if(self.totalRecord==0):
            print(QMessageBox.information(self,"提醒","查询无记录",QMessageBox.Yes,QMessageBox.Yes))
            self.queryModel.select()
            self.totalRecord = self.queryModel.rowCount()
            self.totalPage = int((self.totalRecord + self.pageRecord - 1) / self.pageRecord)
            label = "/" + str(int(self.totalPage)) + "页"
            self.pageLabel.setText(label)
        
            self.queryModel.select()
            self.setButtonStatus()
            return
            
        self.totalPage = int((self.totalRecord + self.pageRecord - 1) / self.pageRecord)
        label = "/" + str(int(self.totalPage)) + "页"
        self.pageLabel.setText(label)
        self.queryModel.select()
        self.setButtonStatus()
        return
        
    # 点击查询
    def searchButtonClicked(self):
        self.currentPage = 1
        self.pageEdit.setText(str(self.currentPage))
        self.getPageCount()
        s = "/" + str(int(self.totalPage)) + "页"
        self.pageLabel.setText(s)
        index = (self.currentPage - 1) * self.pageRecord
        self.recordQuery(index)
        return

    # 向前翻页
    def prevButtonClicked(self):
        self.currentPage -= 1
        if (self.currentPage <= 1):
            self.currentPage = 1
        self.pageEdit.setText(str(self.currentPage))
        index = (self.currentPage - 1) * self.pageRecord
        self.recordQuery(index)
        return

    # 向后翻页
    def backButtonClicked(self):
        self.currentPage += 1
        if (self.currentPage >= int(self.totalPage)):
            self.currentPage = int(self.totalPage)
        self.pageEdit.setText(str(self.currentPage))
        index = (self.currentPage - 1) * self.pageRecord
        self.recordQuery(index)
        return

    # 点击跳转
    def jumpToButtonClicked(self):
        if (self.pageEdit.text().isdigit()):
            self.currentPage = int(self.pageEdit.text())
            if (self.currentPage > self.totalPage):
                self.currentPage = self.totalPage
            if (self.currentPage <= 1):
                self.currentPage = 1
        else:
            self.currentPage = 1
        index = (self.currentPage - 1) * self.pageRecord
        self.pageEdit.setText(str(self.currentPage))
        self.recordQuery(index)
        return
    #添加记录
    def addRecord(self):
        row = self.queryModel.rowCount()
        self.queryModel.insertRow(row)
        index = self.queryModel.index(row, 0)
        self.tableView.setCurrentIndex(index)
        self.tableView.edit(index)
    #删除记录
    def deleteRecord(self):
        curRow=self.tableView.currentIndex().row()
        self.queryModel.removeRow(curRow)
        ok=QMessageBox.warning(self, "警告", "确定修改?", QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if(ok==QMessageBox.No):
            self.queryModel.revertAll()
        else:
            self.queryModel.submitAll()
    def submitRecord(self):
        self.queryModel.database().transaction()
        if(self.queryModel.submitAll()):
            self.queryModel.database().commit()
            QMessageBox.information(self,"提交","提交成功",QMessageBox.Yes,QMessageBox.Yes)
        else:
            self.queryModel.database().rollback()
            QMessageBox.warning(self, "警告", "数据库错误,或许填入了不符合条件的值", QMessageBox.Yes, QMessageBox.Yes)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainMindow = peogroup()
    mainMindow.show()
    sys.exit(app.exec_())
