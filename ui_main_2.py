

from PyQt5 import QtCore, QtGui, QtWidgets

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
        self.TitleLabel.setText(_translate("MainWindow", "City of Austin Sustainability Budget Maker"))
        self.TotalBudgetLabel.setText(_translate("MainWindow", "Total Budget:"))
        self.BudgetRemLabel.setText(_translate("MainWindow", "Budget Remaining: "))
        self.InvestmentsLabel.setText(_translate("MainWindow", "Investments"))
        self.AirLabel.setText(_translate("MainWindow", "Home Energy Efficiency (Air Sealing)"))
        self.LEDLabel.setText(_translate("MainWindow", "Efficient Lighting Program (LEDs)"))
        self.PVLabel.setText(_translate("MainWindow", "PV Installation Rebate Program (check one)"))
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
        
        self.TotBud = int(self.TotBudEdit.text())
    
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
        
    def Air_number_changed(self):
        
        if self.TotBud > 0:
        
            self.AirValue = str(self.AirSlider.value())
            self.AirCurrBudLabel.setText(self.AirValue)
        
            self.Remaining_Budget = self.TotBud - int(self.AirValue) - int(self.LEDValue) - int(self.PVValue)
        
            self.LEDSlider.setMaximum(self.Remaining_Budget)
            self.LEDMaxBudLabel.setText(str(self.Remaining_Budget))
        
            self.PVSlider.setMaximum(self.Remaining_Budget)
            self.PVMaxBudLabel.setText(str(self.Remaining_Budget))
        
            self.BudgetRemNumLabel.setText(str(self.Remaining_Budget))
        
            self.progressValue = (1 - (self.Remaining_Budget/self.TotBud))*100
            self.progressBar.setValue(self.progressValue)

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
            self.progressBar.setValue(self.progressValue)
    
        else:
            self.ErrorLabel.setText('Error. Please input valid budget and reset.')
            
    def PV_number_changed(self):
        
        if self.TotBud > 0:
            
            self.PVValue = str(self.PVSlider.value())
            self.PVCurrBudLabel.setText(self.PVValue)
        
            self.Remaining_Budget = self.TotBud - int(self.AirValue) - int(self.LEDValue) - int(self.PVValue)
        
            self.BudgetRemNumLabel.setText(str(self.Remaining_Budget))
        
            self.progressValue = (1 - (self.Remaining_Budget/self.TotBud))*100
            self.progressBar.setValue(self.progressValue)
            
        else:
            self.ErrorLabel.setText('Error. Please input valid budget and reset.')
                
            
    def click_run_btn(self):
        if self.checkBox.isChecked() == True and self.checkBox_2.isChecked() == True:
            self.ErrorLabel.setText('Error. Please check only one box.')
            
        elif self.checkBox.isChecked() == False and self.checkBox_2.isChecked() == False:
            self.ErrorLabel.setText('Error. Please check only one box.')
            
        else:
            self.ErrorLabel.setText('')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

