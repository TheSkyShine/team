# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    
    
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 729)
        
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        
        self.Eff_Slider = QtWidgets.QSlider(self.centralwidget)
        self.Eff_Slider.setGeometry(QtCore.QRect(320, 380, 291, 22))
        self.Eff_Slider.setMaximum(100)
        self.Eff_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Eff_Slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Eff_Slider.setTickInterval(10)
        self.Eff_Slider.setObjectName("Eff_Slider")
        self.Eff_Slider.valueChanged.connect(self.number_changed)
        
        
        self.TotBudget = QtWidgets.QLabel(self.centralwidget)
        self.TotBudget.setGeometry(QtCore.QRect(20, 180, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.TotBudget.setFont(font)
        self.TotBudget.setObjectName("TotBudget")
        
        
        self.TotBudEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.TotBudEdit.setGeometry(QtCore.QRect(200, 190, 113, 22))
        self.TotBudEdit.setObjectName("TotBudEdit")
        
        
        self.RemBud = QtWidgets.QLabel(self.centralwidget)
        self.RemBud.setGeometry(QtCore.QRect(20, 240, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.RemBud.setFont(font)
        self.RemBud.setObjectName("RemBud")
        
        
        self.RemBudProgBar = QtWidgets.QProgressBar(self.centralwidget)
        self.RemBudProgBar.setGeometry(QtCore.QRect(250, 240, 221, 31))
        self.RemBudProgBar.setMaximum(50)
        self.RemBudProgBar.setProperty("value", 24)
        self.RemBudProgBar.setFormat("")
        self.RemBudProgBar.setObjectName("RemBudProgBar")
        
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 320, 55, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        
        
        self.Label1 = QtWidgets.QLabel(self.centralwidget)
        self.Label1.setGeometry(QtCore.QRect(20, 370, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Label1.setFont(font)
        self.Label1.setObjectName("Label1")
        
        
        self.Label2 = QtWidgets.QLabel(self.centralwidget)
        self.Label2.setGeometry(QtCore.QRect(20, 430, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Label2.setFont(font)
        self.Label2.setObjectName("Label2")
        
        
        self.Program_CheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.Program_CheckBox.setGeometry(QtCore.QRect(490, 430, 71, 31))
        self.Program_CheckBox.setText("")
        self.Program_CheckBox.setObjectName("Program_CheckBox")
        
        
        self.Label3 = QtWidgets.QLabel(self.centralwidget)
        self.Label3.setGeometry(QtCore.QRect(20, 480, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Label3.setFont(font)
        self.Label3.setObjectName("Label3")
        
        
        self.RunButton = QtWidgets.QPushButton(self.centralwidget)
        self.RunButton.setGeometry(QtCore.QRect(900, 580, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.RunButton.setFont(font)
        self.RunButton.setObjectName("RunButton")
        self.RunButton.clicked.connect(self.click_btn)
        
        
        self.Label3_2 = QtWidgets.QLabel(self.centralwidget)
        self.Label3_2.setGeometry(QtCore.QRect(110, 520, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Label3_2.setFont(font)
        self.Label3_2.setObjectName("Label3_2")
        
        
        self.Label3_3 = QtWidgets.QLabel(self.centralwidget)
        self.Label3_3.setGeometry(QtCore.QRect(110, 550, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Label3_3.setFont(font)
        self.Label3_3.setObjectName("Label3_3")
        
        
        self.Program_CheckBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.Program_CheckBox_2.setGeometry(QtCore.QRect(270, 520, 71, 31))
        self.Program_CheckBox_2.setText("")
        self.Program_CheckBox_2.setObjectName("Program_CheckBox_2")
        
        
        self.Program_CheckBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.Program_CheckBox_3.setGeometry(QtCore.QRect(270, 550, 71, 31))
        self.Program_CheckBox_3.setText("")
        self.Program_CheckBox_3.setObjectName("Program_CheckBox_3")
        
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 70, 711, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 410, 16, 16))
        self.label_2.setObjectName("label_2")
        
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(600, 410, 16, 16))
        self.label_4.setObjectName("label_4")
        
        
        self.RemBud_Label = QtWidgets.QLabel(self.centralwidget)
        self.RemBud_Label.setGeometry(QtCore.QRect(480, 240, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.RemBud_Label.setFont(font)
        self.RemBud_Label.setObjectName("RemBud_Label")
        
        
        self.RemBud_3 = QtWidgets.QLabel(self.centralwidget)
        self.RemBud_3.setGeometry(QtCore.QRect(460, 240, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.RemBud_3.setFont(font)
        self.RemBud_3.setObjectName("RemBud_3")
        
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(430, 350, 55, 16))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        
        
        self.Eff_Label = QtWidgets.QLabel(self.centralwidget)
        self.Eff_Label.setGeometry(QtCore.QRect(450, 340, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Eff_Label.setFont(font)
        self.Eff_Label.setObjectName("Eff_Label")
        
        
        self.RemBud_4 = QtWidgets.QLabel(self.centralwidget)
        self.RemBud_4.setGeometry(QtCore.QRect(480, 340, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.RemBud_4.setFont(font)
        self.RemBud_4.setObjectName("RemBud_4")
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TotBudget.setText(_translate("MainWindow", "Total Budget ($):"))
        self.RemBud.setText(_translate("MainWindow", "Budget Remaning:"))
        self.Label1.setText(_translate("MainWindow", "1) Home Energy Effeciency"))
        self.Label2.setText(_translate("MainWindow", "2) Smart Thermostats/ Appliances Program?"))
        self.Label3.setText(_translate("MainWindow", "3) PV Installation Rebate Program"))
        self.RunButton.setText(_translate("MainWindow", "RUN"))
        self.Label3_2.setText(_translate("MainWindow", "A) Retrofitted"))
        self.Label3_3.setText(_translate("MainWindow", "B) New Homes"))
        self.label.setText(_translate("MainWindow", "Austin City Energy Budget Decision Maker"))
        self.label_2.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "100"))
        self.RemBud_Label.setText(_translate("MainWindow", "0"))
        self.RemBud_3.setText(_translate("MainWindow", "$"))
        self.Eff_Label.setText(_translate("MainWindow", "0"))
        self.RemBud_4.setText(_translate("MainWindow", "%"))
        
    def number_changed(self):
        new_value = str(self.Eff_Slider.value())
        self.Eff_Label.setText(new_value)
        
    def click_btn(self):
        TotBud = int(self.TotBudEdit.text())
        effic = int(self.Eff_Slider.value())
        self.RemBud_Label.setText(str(TotBud))
        print(effic)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

