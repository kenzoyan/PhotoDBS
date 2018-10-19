import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from PyQt5.QtSql import *

class addphoto(QDialog):
    loadPhotoSuccess = pyqtSignal()
    getRecordSuccess=pyqtSignal()
    #findPathSuccess=pyqtSignal(str)
    def __init__(self, parent=None , db=None):
        super(addphoto, self).__init__(parent)
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle("上传图片")
        self.nowRecord=QSqlRecord()
        self.db=db
    def setUpUI(self):
        # 书写信息，上传照片
        
        self.resize(400, 600)
        self.layout = QFormLayout()
        self.setStyleSheet("QDialog {\n"
"background-color:rgb(225,238,210);\n"
"}")
        self.setLayout(self.layout)

        # Label控件
        self.titlelabel = QLabel("    请输入")
        self.setStyleSheet("QLabel {\n"
"color:rgb(151,173,172);\n"
"}")
       
        self.idLabel =                QLabel("图片编号:")
        self.idLabel.setStyleSheet("QLabel {\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"background:rgb(137, 190, 178);\n"
"color:rgb(255, 255, 255);\n"
"min-width:8em;\n"
"padding:6px;\n"
"}\n"
)
        self.dateLabel =             QLabel("拍摄时间:")
        self.dateLabel.setStyleSheet("QLabel {\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"background:rgb(137, 190, 178);\n"
"color:rgb(255, 255, 255);\n"
"min-width:8em;\n"
"padding:6px;\n"
"}\n"
)
        self.peopleNameLabel = QLabel("摄  影 师:")
        self.peopleNameLabel.setStyleSheet("QLabel {\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"background:rgb(137, 190, 178);\n"
"color:rgb(255, 255, 255);\n"
"min-width:8em;\n"
"padding:6px;\n"
"}\n"
)
        self.groupLabel =           QLabel("分      组:")
        self.groupLabel.setStyleSheet("QLabel {\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"background:rgb(137, 190, 178);\n"
"color:rgb(255, 255, 255);\n"
"min-width:8em;\n"
"padding:6px;\n"
"}\n"
)
        self.likeLabel =              QLabel("喜爱评分:")
        self.likeLabel.setStyleSheet("QLabel {\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"background:rgb(137, 190, 178);\n"
"color:rgb(255, 255, 255);\n"
"min-width:8em;\n"
"padding:6px;\n"
"}\n"
)
        self.deviceLabel =          QLabel("拍摄设备:")
        self.deviceLabel.setStyleSheet("QLabel {\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"background:rgb(137, 190, 178);\n"
"color:rgb(255, 255, 255);\n"
"min-width:8em;\n"
"padding:6px;\n"
"}\n"
)
        self.locationLabel =        QLabel("地      点:")
        self.locationLabel.setStyleSheet("QLabel {\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"background:rgb(137, 190, 178);\n"
"color:rgb(255, 255, 255);\n"
"min-width:8em;\n"
"padding:6px;\n"
"}\n"
)
        self.findPathLabel=        QLabel("图片路径:")
        self.findPathLabel.setStyleSheet("QLabel {\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"background:rgb(137, 190, 178);\n"
"color:rgb(255, 255, 255);\n"
"min-width:8em;\n"
"padding:6px;\n"
"}\n"
)
        # button控件
        self.addButton = QPushButton("上传")
        self.addButton.setStyleSheet("QPushButton {\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"background:rgb(224, 160, 158);\n"
"color:rgb(255, 255, 255);\n"
"min-width:10em;\n"
"padding:6px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(224,0,0);\n"
"border-style: inset;\n"
"}")
        self.findButton = QPushButton("寻找图片")
        self.findButton.setStyleSheet("QPushButton {\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"background:rgb(0, 85, 127);\n"
"color:rgb(255, 255, 255);\n"
"min-width:10em;\n"
"padding:6px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(224,0,0);\n"
"border-style: inset;\n"
"}")
        # lineEdit控件
        self.idEdit = QLineEdit()
        self.idEdit.setStyleSheet("QLineEdit {\n"
"\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"min-width:10em;\n"
"padding:6px;\n"
"}")
        self.dateEdit = QDateTimeEdit()
        self.dateEdit.setStyleSheet("QDateTimeEdit {\n"
"\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"min-width:10em;\n"
"padding:6px;\n"
"}")
        self.dateEdit.setDisplayFormat("yyyy/MM/dd hh:mm")
        
        self.peopleNameEdit = QLineEdit()
        self.peopleNameEdit.setStyleSheet("QLineEdit {\n"
"\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"min-width:10em;\n"
"padding:6px;\n"
"}")
        self.groupEdit = QLineEdit()
        self.groupEdit.setStyleSheet("QLineEdit {\n"
"\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"min-width:10em;\n"
"padding:6px;\n"
"}")
        self.likeEdit = QLineEdit()
        self.likeEdit.setStyleSheet("QLineEdit {\n"
"\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"min-width:10em;\n"
"padding:6px;\n"
"}")
        self.deviceEdit=QLineEdit()
        self.deviceEdit.setStyleSheet("QLineEdit {\n"
"\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"min-width:10em;\n"
"padding:6px;\n"
"}")
        self.locationEdit=QLineEdit()
        self.locationEdit.setStyleSheet("QLineEdit {\n"
"\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"min-width:10em;\n"
"padding:6px;\n"
"}")
        self.pathEdit=QLineEdit()
        self.pathEdit.setStyleSheet("QLineEdit {\n"
"\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: beige;\n"
"min-width:10em;\n"
"padding:6px;\n"
"}")
        #设置默认提示值
        
        self.idEdit.setPlaceholderText("图片编号")
        self.likeEdit.setPlaceholderText("评分{1，5}之间")
        self.peopleNameEdit.setPlaceholderText("名字")
        self.groupEdit.setPlaceholderText("风格分组")
        self.deviceEdit.setPlaceholderText("设备名字")
        self.locationEdit.setPlaceholderText("拍照地点")
        self.pathEdit.setPlaceholderText("图片存储路径")
        '''
        self.bookNameEdit.setMaxLength(10)
        self.bookIdEdit.setMaxLength(6)
        self.authNameEdit.setMaxLength(10)
        self.publisherEdit.setMaxLength(10)
        self.addNumEdit.setMaxLength(12)
        self.addNumEdit.setValidator(QIntValidator())
        '''
         #添加进formlayout
        self.layout.addRow("", self.titlelabel)
        self.layout.addRow(self.idLabel ,self.idEdit)
        self.layout.addRow(self.dateLabel,  self.dateEdit)
        self.layout.addRow(self.peopleNameLabel, self.peopleNameEdit)
        self.layout.addRow(self.groupLabel, self.groupEdit)
        self.layout.addRow(self.likeLabel, self.likeEdit)
        self.layout.addRow(self.deviceLabel, self.deviceEdit)
        self.layout.addRow(self.locationLabel, self.locationEdit)
        self.layout.addRow(self.findPathLabel, self.pathEdit)
        self.layout.addRow(self.findButton, self.addButton)

        # 设置字体
        font = QFont()
        font.setFamily("方正兰亭超细黑简体")
        font.setPixelSize(30)
        self.titlelabel.setFont(font)
        font.setPixelSize(20)
        self.idLabel.setFont(font)
        self.dateLabel.setFont(font)
        self.peopleNameLabel.setFont(font)
        self.groupLabel.setFont(font)
        self.likeLabel.setFont(font)
        self.deviceLabel.setFont(font)
        self.locationLabel.setFont(font)
        self.findPathLabel.setFont(font)
        self.idEdit.setFont(font)
        self.dateEdit.setFont(font)
        self.peopleNameEdit.setFont(font)
        self.groupEdit.setFont(font)
        self.likeEdit.setFont(font)
        self.deviceEdit.setFont(font)
        self.locationEdit.setFont(font)
        self.pathEdit.setFont(font)
        
        # button设置
        font.setPixelSize(25)
        self.addButton.setFont(font)
        self.addButton.setFixedHeight(50)
        self.addButton.setFixedWidth(200)
        self.findButton.setFont(font)
        self.findButton.setFixedHeight(50)
        self.findButton.setFixedWidth(200)
        
        # 设置间距
        self.titlelabel.setMargin(8)
        self.layout.setVerticalSpacing(10)
        
        self.addButton.clicked.connect(self.addButtonCicked)
        self.findButton.clicked.connect(self.findPhotoPath)
        
    def addButtonCicked(self):
        
        self.id=self.idEdit.text()
        self.date=self.dateEdit.text()
        self.peoplename=self.peopleNameEdit.text()
        self.group=self.groupEdit.text()
        self.like=self.likeEdit.text()
        self.device=self.deviceEdit.text()
        self.location=self.locationEdit.text()
        self.path=self.pathEdit.text()

        if (
                self.id == "" or self.date == "" or self.peoplename == "" or self.group == "" or self.like == "" or self.device == "" or self.location == "" or self.path==""):
            print(QMessageBox.warning(self, "警告", "有字段为空，添加失败", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            if not self.recordCheckSuccess():
                print("fail to check")
                return
            else:
                self.nowRecord.setValue(0, self.id)
                self.nowRecord.setValue(1, self.date)
                self.nowRecord.setValue(2, self.peoplename)
                self.nowRecord.setValue(3, self.group)
                self.nowRecord.setValue(4, self.like)
                self.nowRecord.setValue(5, self.device)
                self.nowRecord.setValue(6, self.location)
                self.nowRecord.setValue(7, self.path)
                print(self.nowRecord.value(7))
                #empty question  记录添加成功
                if not self.nowRecord.isEmpty():
                    self.getRecordSuccess.emit()
                    print(self.nowRecord.value(1))
                else:
                    print("nowrecord is empty")
                
            self.close()
            self.clearEdit()
        return
    def recordCheckSuccess(self):
        #继承photo的db
        query=QSqlQuery(self.db)
        
        query.exec("select pic_id from pictures where pic_id=%s"%self.id)
        query.first()
        check_id=query.value(0)
        print("id", check_id)
        if(check_id==None):
            print("id is good")
        else:
            QMessageBox.information(self, "提示", "id字段已存在，添加失败", QMessageBox.Yes, QMessageBox.Yes)
            self.clearEdit()
            return False
        
        query.exec("select name,people_id from photographers where name='%s'"%self.peoplename)
        query.first()
        check_name=query.value(0)
        print("name", check_name)
        if(check_name==None):
            QMessageBox.information(self, "提示", "摄影师不存在，请先添加摄影师", QMessageBox.Yes, QMessageBox.Yes)
            self.clearEdit()
            return False
        else:
            print("name is good")
            self.peoplename=query.value(1)
       

        
        query.exec("select picgroup_name,picgroup_id from pic_group where picgroup_name='%s'"%self.group)
        query.first()
        check_group=query.value(0)
        print("group", check_group)
        if(check_group==None):
            QMessageBox.information(self, "提示", "分组不存在，请先添加分组", QMessageBox.Yes, QMessageBox.Yes)
            self.clearEdit()
            return False
        else:
            print("group is good")
            self.group=query.value(1)
            
        
        query.exec("select dev_name,dev_id from devices where dev_name='%s'"%self.device)
        query.first()
        check_device=query.value(0)
        print("group", check_device)
        if(check_device==None):
            QMessageBox.information(self, "提示", "设备不存在，请先添加设备", QMessageBox.Yes, QMessageBox.Yes)
            self.clearEdit()
            return False
        else:
            print("device is good")
            self.device=query.value(1)
            #self.db.close()
            return True
        
    def clearEdit(self):
        self.idEdit.clear()
        self.dateEdit.clear()
        self.peopleNameEdit.clear()
        self.groupEdit.clear()
        self.likeEdit.clear()
        self.deviceEdit.clear()
        self.locationEdit.clear()
        self.pathEdit.clear()
    
    def findPhotoPath(self):
        self.filename = QFileDialog.getOpenFileName(self, "OpenFile", ".", 
            "Image Files(*.jpg *.jpeg *.png)")[0]
        self.pathEdit.setText(self.filename)
        #从最左边显示
        #self.pathEdit.setCursorPosition(1)
        print(self.filename)
     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainMindow = addphoto()
    mainMindow.show()
    sys.exit(app.exec_())
