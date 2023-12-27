from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel
from Dialog import Ui_Dialog

import cv2
import os

import Algorithms

global input_image
input_image=""
global sliderValues
global selectedOption
global selectedAlgorithm

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1355, 686)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inputLabel = QtWidgets.QLabel(self.centralwidget)
        self.inputLabel.setGeometry(QtCore.QRect(300, 140, 471, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(18)
        self.inputLabel.setFont(font)
        self.inputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.inputLabel.setObjectName("inputLabel")
        self.inputImage = QtWidgets.QLabel(self.centralwidget)
        self.inputImage.setGeometry(QtCore.QRect(300, 190, 471, 351))
        self.inputImage.setText("")
        self.inputImage.setAlignment(QtCore.Qt.AlignCenter)
        self.inputImage.setObjectName("inputImage")
        self.outputImage = QtWidgets.QLabel(self.centralwidget)
        self.outputImage.setGeometry(QtCore.QRect(830, 190, 471, 351))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(14)
        self.outputImage.setFont(font)
        self.outputImage.setText("")
        self.outputImage.setAlignment(QtCore.Qt.AlignCenter)
        self.outputImage.setStyleSheet("color: #023020;")
        self.outputImage.setObjectName("outputImage")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(830, 140, 471, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(18)
        self.outputLabel.setFont(font)
        self.outputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.algorithmsLabel = QtWidgets.QLabel(self.centralwidget)
        self.algorithmsLabel.setGeometry(QtCore.QRect(30, 110, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.algorithmsLabel.setFont(font)
        self.algorithmsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.algorithmsLabel.setStyleSheet("border: 2px solid black; border-radius: 5px;")
        self.algorithmsLabel.setObjectName("algorithmsLabel")
        self.histogramEqualizationBtn = QtWidgets.QPushButton(self.centralwidget)
        self.histogramEqualizationBtn.setGeometry(QtCore.QRect(30, 110, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.histogramEqualizationBtn.setFont(font)
        self.histogramEqualizationBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.histogramEqualizationBtn.setStyleSheet("")
        self.histogramEqualizationBtn.setObjectName("histogramEqualizationBtn")
        self.algorithmBtn1 = QtWidgets.QPushButton(self.centralwidget)
        self.algorithmBtn1.setGeometry(QtCore.QRect(30, 200, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.algorithmBtn1.setFont(font)
        self.algorithmBtn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.algorithmBtn1.setStyleSheet("")
        self.algorithmBtn1.setObjectName("algorithmBtn1")
        self.algorithmBtn2 = QtWidgets.QPushButton(self.centralwidget)
        self.algorithmBtn2.setGeometry(QtCore.QRect(30, 260, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.algorithmBtn2.setFont(font)
        self.algorithmBtn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.algorithmBtn2.setStyleSheet("")
        self.algorithmBtn2.setObjectName("algorithmBtn2")
        self.algorithmBtn3 = QtWidgets.QPushButton(self.centralwidget)
        self.algorithmBtn3.setGeometry(QtCore.QRect(30, 320, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.algorithmBtn3.setFont(font)
        self.algorithmBtn3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.algorithmBtn3.setStyleSheet("")
        self.algorithmBtn3.setObjectName("algorithmBtn3")
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.setGeometry(QtCore.QRect(30, 520, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.backBtn.setFont(font)
        self.backBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backBtn.setStyleSheet("")
        self.backBtn.setObjectName("backBtn")
        self.contrastStrechBtn = QtWidgets.QPushButton(self.centralwidget)
        self.contrastStrechBtn.setGeometry(QtCore.QRect(30, 170, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contrastStrechBtn.setFont(font)
        self.contrastStrechBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.contrastStrechBtn.setObjectName("contrastStrechBtn")
        self.deblurBtn = QtWidgets.QPushButton(self.centralwidget)
        self.deblurBtn.setGeometry(QtCore.QRect(30, 230, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.deblurBtn.setFont(font)
        self.deblurBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deblurBtn.setObjectName("deblurBtn")
        self.sharpenBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sharpenBtn.setGeometry(QtCore.QRect(30, 290, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sharpenBtn.setFont(font)
        self.sharpenBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sharpenBtn.setObjectName("sharpenBtn")
        self.fixCracksBtn = QtWidgets.QPushButton(self.centralwidget)
        self.fixCracksBtn.setGeometry(QtCore.QRect(30, 410, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fixCracksBtn.setFont(font)
        self.fixCracksBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fixCracksBtn.setObjectName("fixCracksBtn")
        self.colorizeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.colorizeBtn.setGeometry(QtCore.QRect(30, 470, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.colorizeBtn.setFont(font)
        self.colorizeBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.colorizeBtn.setObjectName("colorizeBtn")
        self.denoiseBtn = QtWidgets.QPushButton(self.centralwidget)
        self.denoiseBtn.setGeometry(QtCore.QRect(30, 350, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.denoiseBtn.setFont(font)
        self.denoiseBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.denoiseBtn.setObjectName("denoiseBtn")
        self.topicLabel = QtWidgets.QLabel(self.centralwidget)
        self.topicLabel.setGeometry(QtCore.QRect(540, 10, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.topicLabel.setFont(font)
        self.topicLabel.setStyleSheet("")
        self.topicLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.topicLabel.setObjectName("topicLabel")
        self.noImageSelectedLabel = QtWidgets.QLabel(self.centralwidget)
        self.noImageSelectedLabel.setGeometry(QtCore.QRect(490, 270, 611, 121))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.noImageSelectedLabel.setFont(font)
        self.noImageSelectedLabel.setStyleSheet("border: 2px dashed red; border-radius: 10px;")
        self.noImageSelectedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.noImageSelectedLabel.setObjectName("noImageSelectedLabel")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(213, 30, 20, 611))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.applyBtnCentered = QtWidgets.QPushButton(self.centralwidget)
        self.applyBtnCentered.setGeometry(QtCore.QRect(750, 600, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.applyBtnCentered.setFont(font)
        self.applyBtnCentered.setObjectName("applyBtnCentered")
        self.colorCorrectionBtn = QtWidgets.QPushButton(self.centralwidget)
        self.colorCorrectionBtn.setGeometry(QtCore.QRect(30, 530, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.colorCorrectionBtn.setFont(font)
        self.colorCorrectionBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.colorCorrectionBtn.setObjectName("colorCorrectionBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1355, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_Image = QtWidgets.QAction(MainWindow)
        self.actionSave_Image.setObjectName("actionSave_Image")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_Image)
        self.menubar.addAction(self.menuFile.menuAction())
        self.inputLabel.setVisible(False)
        self.outputLabel.setVisible(False)
        self.inputImage.setVisible(False)
        self.outputImage.setVisible(False)
        self.noImageSelectedLabel.setVisible(True)
        self.algorithmBtn1.setVisible(False)
        self.algorithmBtn2.setVisible(False)
        self.algorithmBtn3.setVisible(False)
        self.algorithmsLabel.setVisible(False)
        self.applyBtnCentered.setVisible(False)
        self.backBtn.setVisible(False)
        self.histogramEqualizationBtn.clicked.connect(self.HistogramEqualizationClicked)
        self.contrastStrechBtn.clicked.connect(self.ContrastStretchClicked)
        self.deblurBtn.clicked.connect(self.DeblurClicked)
        self.sharpenBtn.clicked.connect(self.SharpenClicked)
        self.fixCracksBtn.clicked.connect(self.FixCracksClicked)
        self.colorizeBtn.clicked.connect(self.ColorizeClicked)
        self.denoiseBtn.clicked.connect(self.DenoiseClicked)
        self.colorCorrectionBtn.clicked.connect(self.ColorCorrectionClicked)
        self.algorithmBtn1.clicked.connect(self.AlgorithmBtn1Clicked)
        self.algorithmBtn2.clicked.connect(self.AlgorithmBtn2Clicked)
        self.algorithmBtn3.clicked.connect(self.AlgorithmBtn3Clicked)
        self.backBtn.clicked.connect(self.BackBtnClicked)
        self.actionSave_Image.setEnabled(False)
        self.applyBtnCentered.clicked.connect(self.ApplyCenteredClicked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.inputLabel.setText(_translate("MainWindow", "Input"))
        self.outputLabel.setText(_translate("MainWindow", "Output"))
        self.outputImage.setText(_translate("MainWindow", "No changes\nmade"))
        self.algorithmsLabel.setText(_translate("MainWindow", "Algorithm(s)"))
        self.histogramEqualizationBtn.setText(_translate("MainWindow", "Histogram Equalization"))
        self.contrastStrechBtn.setText(_translate("MainWindow", "Contrast Strech"))
        self.deblurBtn.setText(_translate("MainWindow", "Deblur"))
        self.algorithmBtn1.setText(_translate("MainWindow", "Algorithm Btn 1"))
        self.algorithmBtn2.setText(_translate("MainWindow", "Algorithm Btn 2"))
        self.algorithmBtn3.setText(_translate("MainWindow", "Algorithm Btn 3"))
        self.backBtn.setText(_translate("MainWindow", "<--  Back     "))
        self.sharpenBtn.setText(_translate("MainWindow", "Sharpen"))
        self.fixCracksBtn.setText(_translate("MainWindow", "Fix Cracks"))
        self.colorizeBtn.setText(_translate("MainWindow", "Colorize"))
        self.denoiseBtn.setText(_translate("MainWindow", "Denoise"))
        self.topicLabel.setText(_translate("MainWindow", "ART Restoration"))
        self.noImageSelectedLabel.setText(_translate("MainWindow", "No image selected. Select any image from file menu."))
        self.applyBtnCentered.setText(_translate("MainWindow", "Apply"))
        self.colorCorrectionBtn.setText(_translate("MainWindow", "Color Correction"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open Image"))
        self.actionSave_Image.setText(_translate("MainWindow", "Save Image"))
        self.actionOpen.triggered.connect(self.openImage)
        self.actionSave_Image.triggered.connect(self.saveImagePermanent)

    def openImage(self):
        self.actionSave_Image.setEnabled(False)
        QtCore.QCoreApplication.processEvents()
        self.delete_files_in_folder()
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Open Image", "", "Images (*.png *.xpm *.jpg *.bmp *.gif *.jpeg *.webp *.tiff *.heic);;All Files (*)", options=options
        )
        if fileName:
            pixmap = QtGui.QPixmap(fileName)
            image=cv2.imread(fileName)
            is_height_greater = image.shape[0] > image.shape[1] if len(image.shape) == 3 else False
            if(is_height_greater):
                pixmap = pixmap.scaledToHeight(351)
            else:
                pixmap = pixmap.scaledToWidth(471)
            self.inputImage.setPixmap(pixmap)

            global input_image
            input_image = fileName
            self.inputLabel.setVisible(True)
            self.outputLabel.setVisible(True)
            self.inputImage.setVisible(True)
            self.outputImage.setVisible(True)
            self.noImageSelectedLabel.setVisible(False)
            self.outputImage.setText("No changes\nmade")
            QtCore.QCoreApplication.processEvents()

    def showOutput(self,fileName):
        pixmap = QtGui.QPixmap(fileName)
        image=cv2.imread(fileName)
        is_height_greater = image.shape[0] > image.shape[1] if len(image.shape) == 3 else False
        if(is_height_greater):
            pixmap = pixmap.scaledToHeight(351)
        else:
            pixmap = pixmap.scaledToWidth(471)
        self.outputImage.setPixmap(pixmap)

    def hideAllButtons(self):
        self.histogramEqualizationBtn.setVisible(False)
        self.contrastStrechBtn.setVisible(False)
        self.deblurBtn.setVisible(False)
        self.sharpenBtn.setVisible(False)
        self.fixCracksBtn.setVisible(False)
        self.colorizeBtn.setVisible(False)
        self.denoiseBtn.setVisible(False)
        self.colorCorrectionBtn.setVisible(False)
        self.algorithmBtn1.setVisible(False)
        self.algorithmBtn2.setVisible(False)
        self.algorithmBtn3.setVisible(False)
        self.backBtn.setVisible(False)
        self.algorithmsLabel.setVisible(False)
        self.applyBtnCentered.setVisible(False)

    def showOptions(self):
        self.histogramEqualizationBtn.setVisible(True)
        self.contrastStrechBtn.setVisible(True)
        self.deblurBtn.setVisible(True)
        self.sharpenBtn.setVisible(True)
        self.fixCracksBtn.setVisible(True)
        self.colorizeBtn.setVisible(True)
        self.denoiseBtn.setVisible(True)
        self.colorCorrectionBtn.setVisible(True)
        self.algorithmBtn1.setVisible(False)
        self.algorithmBtn2.setVisible(False)
        self.algorithmBtn3.setVisible(False)
        self.backBtn.setVisible(False)

    def show1AlgorithmBtn(self,btn1Text):
        self.hideAllButtons()
        self.algorithmsLabel.setVisible(True)
        self.algorithmBtn1.setVisible(True)
        self.backBtn.setVisible(True)
        self.algorithmBtn1.setText(btn1Text)

    def show2AlgorithmBtns(self,btn1Text,btn2Text):
        self.hideAllButtons()
        self.algorithmsLabel.setVisible(True)
        self.algorithmBtn1.setVisible(True)
        self.algorithmBtn1.setText(btn1Text)
        self.backBtn.setVisible(True)
        self.algorithmBtn2.setVisible(True)
        self.algorithmBtn2.setText(btn2Text)

    def show3AlgorithmBtns(self,btn1Text,btn2Text,btn3Text):
        self.hideAllButtons()
        self.algorithmsLabel.setVisible(True)
        self.algorithmBtn1.setVisible(True)
        self.algorithmBtn1.setText(btn1Text)
        self.algorithmBtn2.setVisible(True)
        self.algorithmBtn2.setText(btn2Text)
        self.backBtn.setVisible(True)
        self.algorithmBtn3.setVisible(True)
        self.algorithmBtn3.setText(btn3Text)

    def HistogramEqualizationClicked(self):
        if(input_image!=""):
            global selectedOption
            selectedOption="histogramEqualization"
            self.show2AlgorithmBtns("CLAHE","OpenCV Eqialization")
        
    def ContrastStretchClicked(self):
        if(input_image!=""):
            global selectedOption
            selectedOption="contrastStretch"
            self.show1AlgorithmBtn("Manual Stretch")

    def DeblurClicked(self):
        global selectedOption
        if(input_image!=""):
            selectedOption = "deblur"
            self.show1AlgorithmBtn("Richardson-Lucy")
    
    def SharpenClicked(self):
        global selectedOption
        if(input_image!=""):
            selectedOption = "sharpen"
            self.show1AlgorithmBtn("Sharpen")
    
    def FixCracksClicked(self):
        global selectedOption
        if(input_image!=""):
            selectedOption = "fixCracks"
            self.show1AlgorithmBtn("Auto Fix Cracks")

    def ColorizeClicked(self):
        global selectedOption
        if(input_image!=""):
            selectedOption = "colorize"
            self.applyBtnCentered.setVisible(True)
            self.applyBtnCentered.setText("Colorize")

    def ColorCorrectionClicked(self):
        global selectedOption
        if(input_image!=""):
            selectedOption = "colorCorrect"
            self.show1AlgorithmBtn("Enhance Colors")

    def DenoiseClicked(self):
        global selectedOption
        if(input_image!=""):
            selectedOption="denoise"
            self.show3AlgorithmBtns("FastNlMeans","Bm3D","Median Blur")

    def BackBtnClicked(self):
        self.hideAllButtons()
        self.applyBtnCentered.setVisible(False)
        self.showOptions()

    def AlgorithmBtn1Clicked(self):
        global selectedAlgorithm
        if(selectedOption=="denoise"):
            selectedAlgorithm="FastNlMeans"
            self.showDialog({"slider1":{"label":"Filter Strength","default":5,"min":5,"max":30,"increment":1},"slider2":{"label":"Template Win. Size","default":7,"min":1,"max":21,"increment":2},"slider3":{"label":"Search Win. Size","default":21,"min":21,"max":50,"increment":1}})
        if(selectedOption=="histogramEqualization"):
            selectedAlgorithm="CLAHE"
            self.showDialog({"slider1":{"label":"Clip Limit","default":5,"min":1,"max":80,"increment":1}})
        if(selectedOption=="deblur"):
            selectedAlgorithm="Richardson-Lucy"
            self.showDialog({"slider1":{"label":"Iterations","default":10,"min":1,"max":100,"increment":1}, "slider2":{"label":"PSF Size","default":5,"min":1,"max":100,"increment":2}})
        if(selectedOption=="fixCracks"):
            selectedAlgorithm="AutoFix"
            self.showDialog({"slider1":{"label":"Min Edge Range","default":0,"min":0,"max":255,"increment":1}, "slider2":{"label":"Max Edge Range","default":255,"min":0,"max":255,"increment":1}, "slider3":{"label":"Min Desired Length","default":100,"min":0,"max":1000,"increment":10}, "slider4":{"label":"Max Desired Length","default":200,"min":0,"max":1000,"increment":10}, "slider5":{"label":"Max Line Gap","default":10,"min":0,"max":1000,"increment":1}, "slider6":{"label":"Kernel Size","default":5,"min":1,"max":1001,"increment":2}, "slider7":{"label":"Kernal Size 2","default":3,"min":1,"max":1001,"increment":2}})
        if(selectedOption=="sharpen"):
            selectedAlgorithm="Sharpen"
            self.showDialog({"slider1":{"label":"Sigma","default":15,"min":0,"max":100,"increment":1},"slider2":{"label":"Strength","default":15,"min":0,"max":100,"increment":1}})
        if(selectedOption=="contrastStretch"):
            selectedAlgorithm="ManualStretch"
            self.showDialog({"slider1":{"label":"Min Pixel Value","default":0,"min":0,"max":255,"increment":1},"slider2":{"label":"Max Pixel Value","default":255,"min":0,"max":255,"increment":1}})
        if(selectedOption=="colorCorrect"):
            selectedAlgorithm="EnhanceColors"
            self.showDialog({"slider1":{"label":"Red Factor","default":10,"min":5,"max":20,"increment":1},"slider2":{"label":"Green Factor","default":10,"min":5,"max":20,"increment":1},"slider3":{"label":"Blue Factor","default":10,"min":5,"max":20,"increment":1}})

    def AlgorithmBtn2Clicked(self):
        global selectedAlgorithm
        if(selectedOption=="denoise"):
            selectedAlgorithm="Bm3D"
            self.showDialog({"slider1":{"label":"Sigma PSD","default":1,"min":0,"max":800,"increment":1}})
        if(selectedOption=="histogramEqualization"):
            selectedAlgorithm="OpenCVEqialization"
            self.showDialog({"slider1":{"label":"Alpha (Contrast)","default":10,"min":0,"max":100,"increment":1},"slider2":{"label":"Beta (Brightness)","default":0,"min":10,"max":100,"increment":1}})

    def AlgorithmBtn3Clicked(self):
        global selectedAlgorithm
        if(selectedOption=="denoise"):
            selectedAlgorithm="MedianBlur"
            self.showDialog({"slider1":{"label":"K Size","default":5,"min":1,"max":11,"increment":2}})

    def ApplyCenteredClicked(self):
        global selectedOption
        if(selectedOption=="colorize"):
            self.outputImage.setText("Please wait\nLoading...")
            QtCore.QCoreApplication.processEvents()
            output_image = Algorithms.Colorize(input_image)
        self.saveImage(output_image)
        self.actionSave_Image.setEnabled(True)
        self.applyBtnCentered.setVisible(False)
        
    def handleApplyChanges(self, slider_values):
        global sliderValues
        sliderValues = slider_values
        self.outputImage.setText("Please wait\nLoading...")
        QtCore.QCoreApplication.processEvents()
        self.actionSave_Image.setEnabled(True)

        if(selectedAlgorithm=="FastNlMeans"):
            output_image=Algorithms.FastNlMeans_Denoising(input_image,sliderValues[0],sliderValues[1],sliderValues[2])
            self.saveImage(output_image)
        if(selectedAlgorithm=="Bm3D"):
            output_image=Algorithms.BM3D_Denoising(input_image,sliderValues[0]/10)
            self.saveImage(output_image)
        if(selectedAlgorithm=="MedianBlur"):
            output_image=Algorithms.MedianBlur_Denoising(input_image,sliderValues[0])
            self.saveImage(output_image)
        if(selectedAlgorithm=="Richardson-Lucy"):
            output_image,_ = Algorithms.Richardson_lucy_blind_deconvolution_psf(input_image,sliderValues[0],(sliderValues[1],sliderValues[1]))
            self.saveImage(output_image)
        if(selectedAlgorithm=="CLAHE"):
            output_image=Algorithms.CLAHE(input_image,sliderValues[0])
            self.saveImage(output_image)
        if(selectedAlgorithm=="AutoFix"):
            output_image=Algorithms.Automated_Crack_Fixing(input_image,sliderValues[0],sliderValues[1],sliderValues[2],sliderValues[3],sliderValues[4],sliderValues[5],sliderValues[6])
            self.saveImage(output_image)
        if(selectedAlgorithm=="Sharpen"):
            output_image=Algorithms.Sharpen(input_image,sliderValues[0]/10,sliderValues[1]/10)
            self.saveImage(output_image)
        if(selectedAlgorithm=="ManualStretch"):
            output_image=Algorithms.Contrast_stretch(input_image,sliderValues[0],sliderValues[1])
            self.saveImage(output_image)
        if(selectedAlgorithm=="EnhanceColors"):
            output_image=Algorithms.Color_correction(input_image,sliderValues[0]/10,sliderValues[1]/10,sliderValues[2]/10)
            self.saveImage(output_image)
        if(selectedAlgorithm=="OpenCVEqialization"):
            output_image=Algorithms.OpenCV_Histogram_Equalization(input_image,sliderValues[0]/10,sliderValues[1]/10)
            self.saveImage(output_image)
        
    def showDialog(self, sliderInfo):
        dialog = QDialog()
        dialog_ui = Ui_Dialog(self)
        dialog_ui.setupUi(dialog,sliderInfo)
        dialog.setWindowTitle("Adjustment")
        icon = QtGui.QIcon("Icons/dialogIcon.jpg")
        dialog.setWindowIcon(icon)
        dialog.exec_()

    def saveImage(self,image, name="Temp/temp"):
        _,extension = os.path.splitext(input_image)
        cv2.imwrite(name + extension, image)
        self.showOutput(name + extension)
        # print(f"Image saved as {name+extension}")

    def saveImagePermanent(self):
        if(input_image!=""):
            _,extension = os.path.splitext(input_image)
            directory_path, image_name = os.path.split(input_image)
            image = cv2.imread("Temp/temp"+extension)
            cv2.imwrite(directory_path+ "/Edited_"+ image_name, image)
            self.deleteImage("Temp/temp"+extension)

    def deleteImage(self,name):
        try:
            os.remove(name)
        except FileNotFoundError:
            print(f"Image {name} not found.")
        except Exception as e:
            print(f"Error deleting image {name}: {e}")

    def delete_files_in_folder(self,temp_folder_path="Temp"):
        if not os.path.exists(temp_folder_path):
            return

        files_to_delete = [os.path.join(temp_folder_path, file) for file in os.listdir(temp_folder_path)]

        for file_path in files_to_delete:
            try:
                os.remove(file_path)
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("Art Restoration")
    icon = QtGui.QIcon("Icons/icon.png")
    MainWindow.setWindowIcon(icon)
    MainWindow.show()
    sys.exit(app.exec_())
