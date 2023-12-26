from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):

    def __init__(self, main_window):
        self.main_window = main_window

    global sliderInfo
    
    def setupUi(self, Dialog, slider_info):
        global sliderInfo
        sliderInfo=slider_info
        sliders=len(slider_info)
        Dialog.setObjectName("Dialog")
        y=350
        if(sliders==1 or sliders==2):
            x=208
        elif(sliders==3):
            x=315
        elif(sliders==4):
            x=420
        elif(sliders==5):
            x=520
        elif(sliders==6):
            x=620
        else:
            x=721
        Dialog.resize(x, y)
        self.applyBtn = QtWidgets.QPushButton(Dialog)
        self.applyBtn.setGeometry(QtCore.QRect(20, 310, 75, 23))
        self.applyBtn.setObjectName("applyBtn")
        self.cancelBtn = QtWidgets.QPushButton(Dialog)
        self.cancelBtn.setGeometry(QtCore.QRect(110, 310, 75, 23))
        self.cancelBtn.setObjectName("cancelBtn")
        self.slider1 = QtWidgets.QSlider(Dialog)
        self.slider1.setGeometry(QtCore.QRect(40, 60, 22, 160))
        self.slider1.setOrientation(QtCore.Qt.Vertical)
        self.slider1.setObjectName("slider1")
        self.slider1Label = QtWidgets.QLabel(Dialog)
        self.slider1Label.setGeometry(QtCore.QRect(0, 240, 101, 16))
        self.slider1Label.setAlignment(QtCore.Qt.AlignCenter)
        self.slider1Label.setObjectName("slider1Label")
        self.slider1Value = QtWidgets.QLabel(Dialog)
        self.slider1Value.setGeometry(QtCore.QRect(30, 30, 41, 20))
        self.slider1Value.setAlignment(QtCore.Qt.AlignCenter)
        self.slider1Value.setObjectName("slider1Value")
        self.slider2 = QtWidgets.QSlider(Dialog)
        self.slider2.setGeometry(QtCore.QRect(140, 60, 22, 160))
        self.slider2.setOrientation(QtCore.Qt.Vertical)
        self.slider2.setObjectName("slider2")
        self.slider2Label = QtWidgets.QLabel(Dialog)
        self.slider2Label.setGeometry(QtCore.QRect(100, 240, 101, 16))
        self.slider2Label.setAlignment(QtCore.Qt.AlignCenter)
        self.slider2Label.setObjectName("slider2Label")
        self.slider2Value = QtWidgets.QLabel(Dialog)
        self.slider2Value.setGeometry(QtCore.QRect(130, 30, 41, 20))
        self.slider2Value.setAlignment(QtCore.Qt.AlignCenter)
        self.slider2Value.setObjectName("slider2Value")
        self.slider3 = QtWidgets.QSlider(Dialog)
        self.slider3.setGeometry(QtCore.QRect(240, 60, 22, 160))
        self.slider3.setOrientation(QtCore.Qt.Vertical)
        self.slider3.setObjectName("slider3")
        self.slider3Label = QtWidgets.QLabel(Dialog)
        self.slider3Label.setGeometry(QtCore.QRect(200, 240, 111, 16))
        self.slider3Label.setAlignment(QtCore.Qt.AlignCenter)
        self.slider3Label.setObjectName("slider3Label")
        self.slider3Value = QtWidgets.QLabel(Dialog)
        self.slider3Value.setGeometry(QtCore.QRect(230, 30, 41, 20))
        self.slider3Value.setAlignment(QtCore.Qt.AlignCenter)
        self.slider3Value.setObjectName("slider3Value")
        self.slider4 = QtWidgets.QSlider(Dialog)
        self.slider4.setGeometry(QtCore.QRect(350, 60, 22, 160))
        self.slider4.setOrientation(QtCore.Qt.Vertical)
        self.slider4.setObjectName("slider4")
        self.slider4Label = QtWidgets.QLabel(Dialog)
        self.slider4Label.setGeometry(QtCore.QRect(310, 240, 111, 16))
        self.slider4Label.setAlignment(QtCore.Qt.AlignCenter)
        self.slider4Label.setObjectName("slider4Label")
        self.slider4Value = QtWidgets.QLabel(Dialog)
        self.slider4Value.setGeometry(QtCore.QRect(340, 30, 41, 20))
        self.slider4Value.setAlignment(QtCore.Qt.AlignCenter)
        self.slider4Value.setObjectName("slider4Value")
        self.slider5 = QtWidgets.QSlider(Dialog)
        self.slider5.setGeometry(QtCore.QRect(450, 60, 22, 160))
        self.slider5.setOrientation(QtCore.Qt.Vertical)
        self.slider5.setObjectName("slider5")
        self.slider5Label = QtWidgets.QLabel(Dialog)
        self.slider5Label.setGeometry(QtCore.QRect(420, 240, 91, 16))
        self.slider5Label.setAlignment(QtCore.Qt.AlignCenter)
        self.slider5Label.setObjectName("slider5Label")
        self.slider5Value = QtWidgets.QLabel(Dialog)
        self.slider5Value.setGeometry(QtCore.QRect(440, 30, 41, 20))
        self.slider5Value.setAlignment(QtCore.Qt.AlignCenter)
        self.slider5Value.setObjectName("slider5Value")
        self.slider6 = QtWidgets.QSlider(Dialog)
        self.slider6.setGeometry(QtCore.QRect(550, 60, 22, 160))
        self.slider6.setOrientation(QtCore.Qt.Vertical)
        self.slider6.setObjectName("slider6")
        self.slider6Label = QtWidgets.QLabel(Dialog)
        self.slider6Label.setGeometry(QtCore.QRect(520, 240, 81, 16))
        self.slider6Label.setAlignment(QtCore.Qt.AlignCenter)
        self.slider6Label.setObjectName("slider6Label")
        self.slider6Value = QtWidgets.QLabel(Dialog)
        self.slider6Value.setGeometry(QtCore.QRect(540, 30, 41, 20))
        self.slider6Value.setAlignment(QtCore.Qt.AlignCenter)
        self.slider6Value.setObjectName("slider6Value")
        self.slider7 = QtWidgets.QSlider(Dialog)
        self.slider7.setGeometry(QtCore.QRect(650, 60, 22, 160))
        self.slider7.setOrientation(QtCore.Qt.Vertical)
        self.slider7.setObjectName("slider7")
        self.slider7Label = QtWidgets.QLabel(Dialog)
        self.slider7Label.setGeometry(QtCore.QRect(620, 240, 91, 16))
        self.slider7Label.setAlignment(QtCore.Qt.AlignCenter)
        self.slider7Label.setObjectName("slider7Label")
        self.slider7Value = QtWidgets.QLabel(Dialog)
        self.slider7Value.setGeometry(QtCore.QRect(640, 30, 41, 20))
        self.slider7Value.setAlignment(QtCore.Qt.AlignCenter)
        self.slider7Value.setObjectName("slider7Value")
        self.cancelBtn.clicked.connect(lambda: self.on_cancel_clicked(Dialog))
        self.applyBtn.clicked.connect(lambda: self.applyChanges(Dialog))

        for slider in [self.slider1,self.slider2,self.slider3,self.slider4,self.slider5,self.slider6,self.slider7]:
            if (sliderInfo.get(slider.objectName()) != None):
                slider.setMaximum(slider_info[slider.objectName()]["max"])
                slider.setMinimum(slider_info[slider.objectName()]["min"])
                slider.setValue(slider_info[slider.objectName()]["default"])

        self.slider1.valueChanged.connect(lambda value: self.updateSliderLabel(self.slider1,self.slider1Value, value))
        self.slider2.valueChanged.connect(lambda value: self.updateSliderLabel(self.slider2,self.slider2Value, value))
        self.slider3.valueChanged.connect(lambda value: self.updateSliderLabel(self.slider3,self.slider3Value, value))
        self.slider4.valueChanged.connect(lambda value: self.updateSliderLabel(self.slider4,self.slider4Value, value))
        self.slider5.valueChanged.connect(lambda value: self.updateSliderLabel(self.slider5,self.slider5Value, value))
        self.slider6.valueChanged.connect(lambda value: self.updateSliderLabel(self.slider6,self.slider6Value, value))
        self.slider7.valueChanged.connect(lambda value: self.updateSliderLabel(self.slider7,self.slider7Value, value))

        for i in range(sliders+1, 8):
                getattr(self, f"slider{i}").setVisible(False)
                getattr(self, f"slider{i}Label").setVisible(False)
                getattr(self, f"slider{i}Value").setVisible(False)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cancelBtn.setText(_translate("Dialog", "Cancel"))
        self.applyBtn.setText(_translate("Dialog", "Apply"))

        for label in [self.slider1Label,self.slider2Label,self.slider3Label,self.slider4Label,self.slider5Label,self.slider6Label,self.slider7Label]:
            if(sliderInfo.get(label.objectName()[:-5]) != None):
                label.setText(_translate("Dialog", sliderInfo[label.objectName()[:-5]]["label"]))

        for value in [self.slider1Value,self.slider2Value,self.slider3Value,self.slider4Value,self.slider5Value,self.slider6Value,self.slider7Value]:
            if(sliderInfo.get(value.objectName()[:-5]) != None):
                value.setText(_translate("Dialog", str(sliderInfo[value.objectName()[:-5]]["default"])))

    def on_cancel_clicked(self,dialog):
        dialog.close()

    def updateSliderLabel(self, slider, label, value):
        if(sliderInfo.get(slider.objectName())!=None):
            if((slider.value()-sliderInfo[slider.objectName()]["min"])%(sliderInfo[slider.objectName()]["increment"])==0):
                label.setText(str(value))
            else:
                slider.setValue(((slider.value()-sliderInfo[slider.objectName()]["min"])//(sliderInfo[slider.objectName()]["increment"]))*(sliderInfo[slider.objectName()]["increment"])+sliderInfo[slider.objectName()]["min"])

    def getSliderValues(self):
        return [self.slider1.value(),self.slider2.value(),self.slider3.value(),self.slider4.value(),self.slider5.value(),self.slider6.value(),self.slider7.value()]

    def applyChanges(self, dialog):
        dialog.close()
        self.main_window.handleApplyChanges(self.getSliderValues())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
