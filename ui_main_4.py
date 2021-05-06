

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(933, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.drop_shadow_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName("drop_shadow_layout")
        self.drop_shadow_frame = QtWidgets.QFrame(self.centralwidget)
        self.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(34, 36, 102, 255), stop:0.52381 rgba(9, 9, 20, 255));")
        self.drop_shadow_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.drop_shadow_frame.setObjectName("drop_shadow_frame")
        self.TitleLabel = QtWidgets.QLabel(self.drop_shadow_frame)
        self.TitleLabel.setGeometry(QtCore.QRect(80, 0, 731, 151))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.TitleLabel.setObjectName("TitleLabel")
        self.TotalBudgetLabel = QtWidgets.QLabel(self.drop_shadow_frame)
        self.TotalBudgetLabel.setGeometry(QtCore.QRect(10, 140, 221, 121))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.TotalBudgetLabel.setFont(font)
        self.TotalBudgetLabel.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.TotalBudgetLabel.setObjectName("TotalBudgetLabel")
        self.BudgetRemLabel = QtWidgets.QLabel(self.drop_shadow_frame)
        self.BudgetRemLabel.setGeometry(QtCore.QRect(10, 200, 221, 121))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.BudgetRemLabel.setFont(font)
        self.BudgetRemLabel.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.BudgetRemLabel.setObjectName("BudgetRemLabel")
        self.progressBar = QtWidgets.QProgressBar(self.drop_shadow_frame)
        self.progressBar.setGeometry(QtCore.QRect(500, 250, 321, 31))
        self.progressBar.setStyleSheet("color: rgb(121, 253, 255);\n"
"alternate-background-color: rgb(107, 255, 255);\n"
"background-color: rgb(117, 237, 255);")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.InvestmentsLabel = QtWidgets.QLabel(self.drop_shadow_frame)
        self.InvestmentsLabel.setGeometry(QtCore.QRect(10, 290, 271, 141))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.InvestmentsLabel.setFont(font)
        self.InvestmentsLabel.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.InvestmentsLabel.setObjectName("InvestmentsLabel")
        self.AirLabel = QtWidgets.QLabel(self.drop_shadow_frame)
        self.AirLabel.setGeometry(QtCore.QRect(10, 350, 501, 141))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.AirLabel.setFont(font)
        self.AirLabel.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.AirLabel.setObjectName("AirLabel")
        self.LEDLabel = QtWidgets.QLabel(self.drop_shadow_frame)
        self.LEDLabel.setGeometry(QtCore.QRect(10, 480, 501, 141))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.LEDLabel.setFont(font)
        self.LEDLabel.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.LEDLabel.setObjectName("LEDLabel")
        self.PVLabel = QtWidgets.QLabel(self.drop_shadow_frame)
        self.PVLabel.setGeometry(QtCore.QRect(10, 600, 501, 141))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PVLabel.setFont(font)
        self.PVLabel.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.PVLabel.setObjectName("PVLabel")
        self.PVLabelA = QtWidgets.QLabel(self.drop_shadow_frame)
        self.PVLabelA.setGeometry(QtCore.QRect(50, 650, 501, 141))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PVLabelA.setFont(font)
        self.PVLabelA.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.PVLabelA.setObjectName("PVLabelA")
        self.PVLabelB = QtWidgets.QLabel(self.drop_shadow_frame)
        self.PVLabelB.setGeometry(QtCore.QRect(50, 690, 501, 141))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PVLabelB.setFont(font)
        self.PVLabelB.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.PVLabelB.setObjectName("PVLabelB")
        self.AirSlider = QtWidgets.QSlider(self.drop_shadow_frame)
        self.AirSlider.setGeometry(QtCore.QRect(430, 420, 431, 21))
        self.AirSlider.setOrientation(QtCore.Qt.Horizontal)
        self.AirSlider.setObjectName("AirSlider")
        self.AirSlider.valueChanged.connect(self.Air_number_changed)
        
        
        self.LEDSlider = QtWidgets.QSlider(self.drop_shadow_frame)
        self.LEDSlider.setGeometry(QtCore.QRect(430, 550, 431, 21))
        self.LEDSlider.setOrientation(QtCore.Qt.Horizontal)
        self.LEDSlider.setObjectName("LEDSlider")
        self.LEDSlider.valueChanged.connect(self.LED_number_changed)
        
        
        self.PVSlider = QtWidgets.QSlider(self.drop_shadow_frame)
        self.PVSlider.setGeometry(QtCore.QRect(430, 680, 431, 21))
        self.PVSlider.setOrientation(QtCore.Qt.Horizontal)
        self.PVSlider.setObjectName("PVSlider")
        self.PVSlider.valueChanged.connect(self.PV_number_changed)
        
        
        self.checkBox = QtWidgets.QCheckBox(self.drop_shadow_frame)
        self.checkBox.setGeometry(QtCore.QRect(230, 720, 81, 20))
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet("background-color: none\n"
"")
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.drop_shadow_frame)
        self.checkBox_2.setGeometry(QtCore.QRect(230, 760, 81, 20))
        self.checkBox_2.setAutoFillBackground(False)
        self.checkBox_2.setStyleSheet("background-color: none\n"
"")
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.DollarLabel = QtWidgets.QLabel(self.drop_shadow_frame)
        self.DollarLabel.setGeometry(QtCore.QRect(580, 380, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.DollarLabel.setFont(font)
        self.DollarLabel.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.DollarLabel.setObjectName("DollarLabel")
        self.DollarLabel3_2 = QtWidgets.QLabel(self.drop_shadow_frame)
        self.DollarLabel3_2.setGeometry(QtCore.QRect(580, 510, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.DollarLabel3_2.setFont(font)
        self.DollarLabel3_2.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.DollarLabel3_2.setObjectName("DollarLabel3_2")
        self.DollarLabel3 = QtWidgets.QLabel(self.drop_shadow_frame)
        self.DollarLabel3.setGeometry(QtCore.QRect(580, 640, 20, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.DollarLabel3.setFont(font)
        self.DollarLabel3.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.DollarLabel3.setObjectName("DollarLabel3")
        self.DollarLabel_2 = QtWidgets.QLabel(self.drop_shadow_frame)
        self.DollarLabel_2.setGeometry(QtCore.QRect(420, 440, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.DollarLabel_2.setFont(font)
        self.DollarLabel_2.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.DollarLabel_2.setObjectName("DollarLabel_2")
        self.DollarLabel_3 = QtWidgets.QLabel(self.drop_shadow_frame)
        self.DollarLabel_3.setGeometry(QtCore.QRect(420, 570, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.DollarLabel_3.setFont(font)
        self.DollarLabel_3.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.DollarLabel_3.setObjectName("DollarLabel_3")
        self.DollarLabel_4 = QtWidgets.QLabel(self.drop_shadow_frame)
        self.DollarLabel_4.setGeometry(QtCore.QRect(420, 700, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.DollarLabel_4.setFont(font)
        self.DollarLabel_4.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.DollarLabel_4.setObjectName("DollarLabel_4")
        self.DollarLabel_5 = QtWidgets.QLabel(self.drop_shadow_frame)
        self.DollarLabel_5.setGeometry(QtCore.QRect(800, 440, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.DollarLabel_5.setFont(font)
        self.DollarLabel_5.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.DollarLabel_5.setObjectName("DollarLabel_5")
        self.DollarLabel_6 = QtWidgets.QLabel(self.drop_shadow_frame)
        self.DollarLabel_6.setGeometry(QtCore.QRect(800, 570, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.DollarLabel_6.setFont(font)
        self.DollarLabel_6.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.DollarLabel_6.setObjectName("DollarLabel_6")
        self.DollarLabel_7 = QtWidgets.QLabel(self.drop_shadow_frame)
        self.DollarLabel_7.setGeometry(QtCore.QRect(800, 700, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.DollarLabel_7.setFont(font)
        self.DollarLabel_7.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.DollarLabel_7.setObjectName("DollarLabel_7")
        self.AirMaxBudLabel = QtWidgets.QLabel(self.drop_shadow_frame)
        self.AirMaxBudLabel.setGeometry(QtCore.QRect(810, 440, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.AirMaxBudLabel.setFont(font)
        self.AirMaxBudLabel.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.AirMaxBudLabel.setObjectName("AirMaxBudLabel")
        self.LEDMaxBudLabel = QtWidgets.QLabel(self.drop_shadow_frame)
        self.LEDMaxBudLabel.setGeometry(QtCore.QRect(810, 570, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.LEDMaxBudLabel.setFont(font)
        self.LEDMaxBudLabel.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.LEDMaxBudLabel.setObjectName("LEDMaxBudLabel")
        self.PVMaxBudLabel = QtWidgets.QLabel(self.drop_shadow_frame)
        self.PVMaxBudLabel.setGeometry(QtCore.QRect(810, 700, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PVMaxBudLabel.setFont(font)
        self.PVMaxBudLabel.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.PVMaxBudLabel.setObjectName("PVMaxBudLabel")
        self.AirCurrBudLabel = QtWidgets.QLabel(self.drop_shadow_frame)
        self.AirCurrBudLabel.setGeometry(QtCore.QRect(600, 380, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.AirCurrBudLabel.setFont(font)
        self.AirCurrBudLabel.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.AirCurrBudLabel.setObjectName("AirCurrBudLabel")
        self.LEDCurrBudLabel = QtWidgets.QLabel(self.drop_shadow_frame)
        self.LEDCurrBudLabel.setGeometry(QtCore.QRect(600, 510, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.LEDCurrBudLabel.setFont(font)
        self.LEDCurrBudLabel.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.LEDCurrBudLabel.setObjectName("LEDCurrBudLabel")
        self.PVCurrBudLabel = QtWidgets.QLabel(self.drop_shadow_frame)
        self.PVCurrBudLabel.setGeometry(QtCore.QRect(600, 640, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PVCurrBudLabel.setFont(font)
        self.PVCurrBudLabel.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.PVCurrBudLabel.setObjectName("PVCurrBudLabel")
        self.BudgetRemLabel_3 = QtWidgets.QLabel(self.drop_shadow_frame)
        self.BudgetRemLabel_3.setGeometry(QtCore.QRect(240, 250, 20, 31))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.BudgetRemLabel_3.setFont(font)
        self.BudgetRemLabel_3.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.BudgetRemLabel_3.setObjectName("BudgetRemLabel_3")
        self.BudgetRemLabel_4 = QtWidgets.QLabel(self.drop_shadow_frame)
        self.BudgetRemLabel_4.setGeometry(QtCore.QRect(240, 190, 20, 31))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.BudgetRemLabel_4.setFont(font)
        self.BudgetRemLabel_4.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.BudgetRemLabel_4.setObjectName("BudgetRemLabel_4")
        self.BudgetRemNumLabel = QtWidgets.QLabel(self.drop_shadow_frame)
        self.BudgetRemNumLabel.setGeometry(QtCore.QRect(270, 240, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.BudgetRemNumLabel.setFont(font)
        self.BudgetRemNumLabel.setStyleSheet("background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.BudgetRemNumLabel.setObjectName("BudgetRemNumLabel")
        self.BudgetButton = QtWidgets.QPushButton(self.drop_shadow_frame)
        self.BudgetButton.setGeometry(QtCore.QRect(500, 190, 141, 28))
        self.BudgetButton.setStyleSheet("background-color: rgb(83, 241, 255);")
        self.BudgetButton.setObjectName("BudgetButton")
        self.BudgetButton.clicked.connect(self.click_bud_btn)
        
        
        self.BudgetButton_2 = QtWidgets.QPushButton(self.drop_shadow_frame)
        self.BudgetButton_2.setGeometry(QtCore.QRect(740, 790, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BudgetButton_2.setFont(font)
        self.BudgetButton_2.setStyleSheet("background-color: rgb(83, 241, 255);")
        self.BudgetButton_2.setObjectName("BudgetButton_2")
        self.BudgetButton_2.clicked.connect(self.click_run_btn)
        
        
        
        self.TotBudEdit = QtWidgets.QLineEdit(self.drop_shadow_frame)
        self.TotBudEdit.setGeometry(QtCore.QRect(270, 200, 113, 22))
        self.TotBudEdit.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.TotBudEdit.setObjectName("TotBudEdit")
        self.ErrorLabel = QtWidgets.QLabel(self.drop_shadow_frame)
        self.ErrorLabel.setGeometry(QtCore.QRect(10, 820, 671, 51))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ErrorLabel.setFont(font)
        self.ErrorLabel.setStyleSheet("background-color: none;\n"
"color: rgb(255, 0, 0);")
        self.ErrorLabel.setObjectName("ErrorLabel")
        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TitleLabel.setText(_translate("MainWindow", "Austin Decarbonization Budget Tool [$ Mil]"))
        self.TotalBudgetLabel.setText(_translate("MainWindow", "Total Budget:"))
        self.BudgetRemLabel.setText(_translate("MainWindow", "Budget Remaining: "))
        self.InvestmentsLabel.setText(_translate("MainWindow", "Investments"))
        self.AirLabel.setText(_translate("MainWindow", "Home Energy Efficiency (Air Sealing)"))
        self.LEDLabel.setText(_translate("MainWindow", "Efficient Lighting Program (LEDs)"))
        self.PVLabel.setText(_translate("MainWindow", "Solar Installation Program (check one)"))
        self.PVLabelA.setText(_translate("MainWindow", "A) Retrofitted?"))
        self.PVLabelB.setText(_translate("MainWindow", "B) New Homes?"))
        self.DollarLabel.setText(_translate("MainWindow", "$"))
        self.DollarLabel3_2.setText(_translate("MainWindow", "$"))
        self.DollarLabel3.setText(_translate("MainWindow", "$"))
        self.DollarLabel_2.setText(_translate("MainWindow", "$0"))
        self.DollarLabel_3.setText(_translate("MainWindow", "$0"))
        self.DollarLabel_4.setText(_translate("MainWindow", "$0"))
        self.DollarLabel_5.setText(_translate("MainWindow", "$"))
        self.DollarLabel_6.setText(_translate("MainWindow", "$"))
        self.DollarLabel_7.setText(_translate("MainWindow", "$"))
        self.AirMaxBudLabel.setText(_translate("MainWindow", "0"))
        self.LEDMaxBudLabel.setText(_translate("MainWindow", "0"))
        self.PVMaxBudLabel.setText(_translate("MainWindow", "0"))
        self.AirCurrBudLabel.setText(_translate("MainWindow", "0"))
        self.LEDCurrBudLabel.setText(_translate("MainWindow", "0"))
        self.PVCurrBudLabel.setText(_translate("MainWindow", "0"))
        self.BudgetRemLabel_3.setText(_translate("MainWindow", "$"))
        self.BudgetRemLabel_4.setText(_translate("MainWindow", "$"))
        self.BudgetRemNumLabel.setText(_translate("MainWindow", "0"))
        self.BudgetButton.setText(_translate("MainWindow", "Press to Set Budget and Reset"))
        self.BudgetButton_2.setText(_translate("MainWindow", "Run"))
        self.TotBudEdit.setPlaceholderText(_translate("MainWindow", "0"))
        self.ErrorLabel.setText(_translate("MainWindow", "⠀⠀"))
        
        self.TotBud = 0
        self.AirValue = 0
        self.LEDValue = 0
        self.PVValue = 0
        
    def click_bud_btn(self):
        
        self.ErrorLabel.setText('')
        
        self.TotBud = self.TotBudEdit.text()
        
        if self.TotBud.isnumeric() == True:
            
            self.TotBud = int(self.TotBud)
            self.AirMaxBudLabel.setText(str(self.TotBud))
            self.LEDMaxBudLabel.setText(str(self.TotBud))
            self.PVMaxBudLabel.setText(str(self.TotBud))
        
            self.AirSlider.setMaximum(self.TotBud)
            self.LEDSlider.setMaximum(self.TotBud)
            self.PVSlider.setMaximum(self.TotBud)
        
            self.BudgetRemNumLabel.setText(str(self.TotBud))
        
            self.AirSlider.setValue(0)
            self.LEDSlider.setValue(0)
            self.PVSlider.setValue(0)
        
        else:
            self.ErrorLabel.setText('Please enter an integer for the budget.')
            
            
    def Air_number_changed(self):
        
        if self.TotBud > 0:
        
            self.AirValue = str(self.AirSlider.value())
            self.AirCurrBudLabel.setText(self.AirValue)
        
            self.Remaining_Budget = self.TotBud - int(self.AirValue) - int(self.LEDValue) - int(self.PVValue)
        
            self.LEDSlider.setMaximum(self.Remaining_Budget)
            self.LEDMaxBudLabel.setText(str(self.Remaining_Budget))
            
            self.LEDSlider.setMaximum(self.Remaining_Budget)
            self.LEDMaxBudLabel.setText(str(self.Remaining_Budget))
        
            self.PVSlider.setMaximum(self.Remaining_Budget)
            self.PVMaxBudLabel.setText(str(self.Remaining_Budget))
        
            self.BudgetRemNumLabel.setText(str(self.Remaining_Budget))
        
            self.progressValue = (1 - (self.Remaining_Budget/self.TotBud))*100
            self.progressBar.setValue(int(self.progressValue))

        else:
            self.ErrorLabel.setText('Error. Please input valid budget and reset.')
        
    def LED_number_changed(self):
        
        if self.TotBud > 0:
            
            self.LEDValue = str(self.LEDSlider.value())
            self.LEDCurrBudLabel.setText(self.LEDValue)
        
            self.Remaining_Budget = self.TotBud - int(self.AirValue) - int(self.LEDValue) - int(self.PVValue)
        
            self.PVSlider.setMaximum(self.Remaining_Budget)
            self.PVMaxBudLabel.setText(str(self.Remaining_Budget))
        
            self.BudgetRemNumLabel.setText(str(self.Remaining_Budget))
        
            self.progressValue = (1 - (self.Remaining_Budget/self.TotBud))*100
            self.progressBar.setValue(int(self.progressValue))
    
        else:
            self.ErrorLabel.setText('Error. Please input valid budget and reset.')
            
    def PV_number_changed(self):
        
        if self.TotBud > 0:
            
            self.PVValue = str(self.PVSlider.value())
            self.PVCurrBudLabel.setText(self.PVValue)
        
            self.Remaining_Budget = self.TotBud - int(self.AirValue) - int(self.LEDValue) - int(self.PVValue)
        
            self.BudgetRemNumLabel.setText(str(self.Remaining_Budget))
        
            self.progressValue = (1 - (self.Remaining_Budget/self.TotBud))*100
            self.progressBar.setValue(int(self.progressValue))
            
        else:
            self.ErrorLabel.setText('Error. Please input valid budget and reset.')
                
            
    def click_run_btn(self):
        
        if self.TotBud <= 0:
            self.ErrorLabel.setText('Error. Please input valid budget and reset.')
            
        elif self.checkBox.isChecked() == self.checkBox_2.isChecked():
            self.ErrorLabel.setText('Error. Please check only one box.')
            
        else:
            self.ErrorLabel.setText('')
            
            self.AirValue = int(self.AirValue)*1e6
            self.LEDValue = int(self.LEDValue)*1e6
            self.PVValue = int(self.PVValue)*1e6
            
            self.Results()
            self.Plotting()
            

            
            
            
            
            
    def Results(self):

        # Inputs (integers):  Home Energy [$], Effecient Lighting [$], PV installation [$] (IN DOLLAR UNITS)
        # Home Energy[$] --->Total/Average Cost = Number of Houses ---> Number of houses * % offset * average electricity use per month = total electricity saved per month
        # Effecient Lighting [$] -----> Total/Average cost = Number of houses ----> Number of houses * % offset * average electricity use per month = total electricity saved per month
        # PV Installation [$] -----> Total/Average cost[$ / kW] = kW of solar install ------> kW of solar install * (production ratio/12)*1000 = kWh per month

        # average montly residential electricity use (kWh/month), pulled from Austin Energy billing data (average over 1 year)
        import pandas as pd
        import numpy as np
        
        file = 'Residential_Average_Monthly_kWh_and_Bills_New.csv'
        data = pd.read_csv(file, encoding='latin-1')
        
        energy_list = np.array(data.Average_kWh)

        energy_use = sum(energy_list)/len(energy_list)
        
        num_res = 454616
        
        # energy saved from air sealing (kWh/month)
        air_cost = 3500     # $/home to seal building envelope
        num_homes = int(self.AirValue) / air_cost
        energy_saved_1 = (num_homes * 0.10 * energy_use)/num_res
        
        # energy saved from replacing inefficient bulbs w/ LEDs (kWh/month)
        LED_cost = 2 * 50 * 0.60    # $/home to replace all inefficient bulbs
        num_homes = int(self.LEDValue) / LED_cost
        percent_offset = 0.09 *( 1 - 0.4 / (0.40*1 + 0.60*4))
        energy_saved_2 = (num_homes * percent_offset * energy_use)/num_res
        
        if self.checkBox.isChecked() == True:
            PV_mult = 1
        else:
            PV_mult = 0.9
         
        
        # energy generated by installing additional rooftop solar PV (kWh/month)
        PV_cost = 1960*PV_mult     # $/kW average residential install cost in Austin
        prod_ratio = 1.45   # kWh/yr per W of PV installed (ranges from 1.3-1.6 for U.S.)
        kw_installed = int(self.PVValue) / PV_cost
        energy_gen = ((kw_installed * prod_ratio) / 12) * 1000
        
        self.energy_saved = energy_saved_1 + energy_saved_2
        self.energy_gen = energy_gen
        self.energy_use = energy_use
    

        
        
    def Plotting(self):
        
        # Imports
        import matplotlib.pyplot as plt
        import pandas as pd
        import math as m
        
        '''
        *********************************
        
        CODE FOR ELECTRICITY USAGE (RESIDENTIAL) PLOT
        
        *********************************
        '''
        
        # Takes data from CSV and uses Pandas to put into list
        file = 'Residential_Average_Monthly_kWh_and_Bills_New.csv'
        data = pd.read_csv(file, encoding='latin-1')
        
        # Converts power to temp list
        power_tempList = data["Average_kWh"].tolist()
        
        # Puts the data in correct format
        date = data.Date
        date_tempList = []
        for i in date:
            a, b, c = i.split(" ")
            x,y,z = a.split("/")
            q = x + "/" + z
            date_tempList.append(q)
        
        # Takes data from 2015-2019 (Three Full Electricity Cycles) and puts into new lists
        date_list = []
        power_past = []
        k = 0
        for i in date_tempList:
            j = i[3:]
            j = int(j)
            if j > 2015:
                date_list.append(date_tempList[k])
                power_past.append(power_tempList[k])
            k += 1
        
        '''
        Sinusoidal Regression Equation From Excel for Comparison
        r^2 = 0.7228
        y = 279.2835*sin(0.5236x-2.0879) + 871.1282
        '''
        
        # Using sin equation: -a*sin(bx) + c
        # Finding a
        ymax = max(power_past)
        ymin = min(power_past)
        a = (ymax - ymin) / 2
        
        # Finding b
        # 12 is used as period due to a full power cycle taking a year
        b = (2 * m.pi) / 12
        
        # Finding c
        c = power_past[0]
        
        # Call function to get total electricty saved and incorporate into sinusoidal regression
        # Creates Regression for both old and new data
        power_regr = []
        power_change = []
        change = self.energy_saved # Called from inputs
        
        for i in range(len(power_past) + 12):
            power_regr.append(-a*m.sin((b*i)+1)+c) 
            power_change.append((-a*m.sin((b*i)+1)+c) - change)
        output_list = power_change[-13:]
        
        # Creating Plot
        
        # Updated date list
        new_dateList = []
        for i in date_list:
            new_dateList.append(i)
        
        # Future dates to be used with regression models
        future_dates = ["03/2019","04/2019","05/2019","06/2019","07/2019","08/2019","09/2019","10/2019","11/2019","12/2019","01/2020","02/2020","03/2020"]
        for i in future_dates:
            if i not in new_dateList:
                new_dateList.append(i)
    
        # Text Colors/FontSize
        plt.rcParams['font.weight'] = 'bold'
        # plt.rcParams['font.sans-serif'] = ['Lucida Grande']
        plt.rcParams['font.size'] = '11'
        plt.rcParams['text.color'] = 'black'
    
        # Window Size
        fig = plt.figure(figsize=(12,5))
        
        # Color
        fig.patch.set_facecolor('lightcyan')
        
        # Plotting
        plt.subplot(2,2,(1,2))
        plt.plot(date_list, power_past, label = 'Original Data')
        plt.plot(future_dates, output_list, label = 'New Data Regression', linewidth = 4.5)
        plt.plot(new_dateList, power_regr, label = 'Original Data Regression')
        
        
        # Extra Design
        axes = plt.gca()
        axes.set_ylim([400,1400])
        plt.legend(loc=2, prop={'size': 7})
        plt.title('Electricity Usage (Residential)', fontweight="bold", fontsize=16)
        plt.xlabel('Month(mm/yyyy)', fontsize=12)
        plt.xticks(rotation=80, fontsize=8)
        plt.ylabel('Energy per Month (kWh)', fontsize=12)
        plt.show()
        
        
        '''
        *********************************
        
        CODE FOR ENERGY MIX PLOT
        
        *********************************
        '''
        
        # Data
    
        #energy_gen = 50000
        energy_gen = self.energy_gen
        num_res = 454616 # number of residential customers 2020
        res_tot = num_res * self.energy_use  # kWh per month
        energy = ['Solar', 'Gas', 'Wind', 'Coal', 'Other']
        percentage_original = [2.3, 45.66, 22.88, 18, 11.16]
        percentage = [2.3, 45.66, 22.88, 18, 11.16] # 2020 annual texas values from ERCOT
        pv_percent = (energy_gen / res_tot) *100
        percentage[0] += pv_percent
        percentage[3] -= pv_percent
        
        # Makes solar explode out
        solar = (0.1, 0, 0, 0, 0)
        
        # Colors
        colors = ['springgreen', 'lightcoral', 'khaki', 'aquamarine', 'thistle']
        
    
        # Create pie subplot
    
        plt.subplot(2,2,3)
        plt.pie(percentage_original,explode = solar, colors = colors, labels = energy, autopct='%1.2f%%', shadow=True, startangle=90, textprops={'fontsize': 8})
        plt.title('Original Austin Energy Mix', fontweight="bold", fontsize=16)
        fig.patch.set_facecolor('lightcyan')
        plt.axis('equal')  
        plt.tight_layout()
        plt.show()
        
        plt.subplot(2,2,4)
        plt.pie(percentage,explode = solar, colors = colors, labels = energy, autopct='%1.2f%%', shadow=True, startangle=90, textprops={'fontsize': 8})
        plt.title('New Austin Energy Mix', fontweight="bold", fontsize=16)
        fig.patch.set_facecolor('lightcyan')
        plt.axis('equal')  
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    import sys
    #app = QtWidgets.QApplication(sys.argv)
    app = QCoreApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

