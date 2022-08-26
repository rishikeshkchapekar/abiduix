# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'application.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2
from datetime import datetime
import os


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):

		self.section = 0

		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(800, 600)
		MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.img_label = QtWidgets.QLabel(self.centralwidget)
		self.img_label.setGeometry(QtCore.QRect(40, 20, 721, 381))
		self.img_label.setStyleSheet("border-radius: 20px;")
		self.img_label.setScaledContents(True)
		self.img_label.setObjectName("img_label")
		self.left_button = QtWidgets.QPushButton(self.centralwidget)
		self.left_button.setGeometry(QtCore.QRect(300, 450, 41, 41))
		font = QtGui.QFont()
		font.setBold(False)
		font.setWeight(50)
		self.left_button.setFont(font)
		self.left_button.setStyleSheet("background-color: rgb(46, 52, 54);\ncolor: rgb(240, 4, 4);\n"
"border-radius: 10px;")
		self.left_button.setText("")
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("icons/red-x-10340.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.left_button.setIcon(icon)
		self.left_button.setIconSize(QtCore.QSize(16, 16))
		self.left_button.setObjectName("left_button")
		self.right_button = QtWidgets.QPushButton(self.centralwidget)
		self.right_button.setGeometry(QtCore.QRect(420, 450, 41, 41))
		self.right_button.setStyleSheet("background-color: rgb(46, 52, 54);\n color: rgb(37, 150, 190);\n"
"border-radius: 10px;")
		self.right_button.setText("")
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap("icons/camera-6748.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.right_button.setIcon(icon1)
		self.right_button.setObjectName("right_button")
		self.left_label = QtWidgets.QLabel(self.centralwidget)
		self.left_label.setGeometry(QtCore.QRect(290, 500, 61, 20))
		self.left_label.setStyleSheet("color: rgb(243, 243, 243);")
		self.left_label.setAlignment(QtCore.Qt.AlignCenter)
		self.left_label.setObjectName("left_label")
		self.right_label = QtWidgets.QLabel(self.centralwidget)
		self.right_label.setGeometry(QtCore.QRect(400, 500, 91, 20))
		self.right_label.setStyleSheet("color: rgb(243, 243, 243);")
		self.right_label.setAlignment(QtCore.Qt.AlignCenter)
		self.right_label.setObjectName("right_label")
		self.prompt_label = QtWidgets.QLabel(self.centralwidget)
		self.prompt_label.setGeometry(QtCore.QRect(250, 420, 301, 16))
		self.prompt_label.setAlignment(QtCore.Qt.AlignCenter)
		self.prompt_label.setStyleSheet("color: rgb(243, 243, 243);")
		self.prompt_label.setText("")
		self.prompt_label.setAlignment(QtCore.Qt.AlignCenter)
		self.prompt_label.setObjectName("prompt_label")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		# added after generating code from ui

		self.right_button.clicked.connect(self.rightBtnClicked)
		self.left_button.clicked.connect(self.leftBtnClicked)

		self.imgWorker = ImageWorker()
		self.imgWorker.start()
		self.imgWorker.ImageUpdate.connect(self.imageUpdate)

		# ------------------------------------------------------#

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.img_label.setText(_translate("MainWindow", "TextLabel"))
		self.left_label.setText(_translate("MainWindow", "Cancel"))
		self.right_label.setText(_translate("MainWindow", "Take Picture"))

	# --------------------added after generating code from UI---------------------------#

	def setPromptLabelText(self,text):
		self.prompt_label.setText(text)

	def adjustPromptLabelSize(self):
		self.prompt_label.adjustSize()			

	def styleRightBtn(self):
		if self.section == 1:
			self.right_button.setGeometry(QtCore.QRect(420, 450, 100, 41))
			self.right_button.setText("I love it!")
			icon1 = QtGui.QIcon()
			icon1.addPixmap(QtGui.QPixmap("icons/heart-492.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			self.right_button.setIcon(icon1)

		
		if self.section	== 2:
			self.right_button.setGeometry(QtCore.QRect(400, 450, 120, 41))
			self.right_button.setText("Yes please")
			self.setPromptLabelText("Would you like to post this photo to \"client instagram\" account?")
			self.adjustPromptLabelSize()		

	def styleLeftBtn(self):
		if self.section == 1:
			self.left_button.setGeometry(QtCore.QRect(240, 450, 100, 41))
			self.left_button.setText("Retake")
			icon1 = QtGui.QIcon()
			icon1.addPixmap(QtGui.QPixmap("icons/dislike.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			self.left_button.setIcon(icon1)	

		if self.section == 2:
			self.left_button.setText("No, just save it here")
			self.left_button.setGeometry(QtCore.QRect(160, 450, 180, 41))

	def rightBtnClicked(self):
		self.left_label.setText("")
		self.right_label.setText("")

		if self.section == 0: #clicked on take picture
			self.imgWorker.captureImage()
			self.imgWorker.showCapturedImage()
			self.setPromptLabelText("Do you like this photo?")
			self.section = 1

		elif self.section == 1: #clicked on i love it
			self.section = 2

		self.styleRightBtn()
		self.styleLeftBtn()

	def leftBtnClicked(self):
		if self.section == 1: #clicked on retake
			self.resetAll()

		elif self.section == 2: #clicked on just save it here
			self.imgWorker.saveImage()
			self.resetAll()


	def imageUpdate(self,image):
		self.img_label.setPixmap(QPixmap.fromImage(image))		
	


	def resetAll(self):
		self.left_button.setGeometry(QtCore.QRect(300, 450, 41, 41))
		self.left_button.setText("")
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("icons/red-x-10340.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.left_button.setIcon(icon)

		self.right_button.setGeometry(QtCore.QRect(420, 450, 41, 41))
		self.right_button.setText("")
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap("icons/camera-6748.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.right_button.setIcon(icon1)

		self.setPromptLabelText("")

		self.left_label.setText("Cancel")
		self.right_label.setText("Take Picture")

		self.imgWorker.showPreview = True

		self.section = 0

	# ------------------------------------------------------------- #

class ImageWorker(QThread):
	ImageUpdate = pyqtSignal(QImage)
	def run(self):
		self.ThreadActive = True
		self.showPreview = True
		self.frame = None

		Capture = cv2.VideoCapture(0)
		
		while self.ThreadActive:
			if self.showPreview:
				ret,frame = Capture.read()
				if ret:
					image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
					self.frame = frame
					flipped = cv2.flip(image,1)
					convert_qt = QImage(flipped.data,flipped.shape[1],flipped.shape[0],QImage.Format_RGB888)
					# pic = convert_qt.scaled(640,480,Qt.KeepAspectRatio)
					
					self.ImageUpdate.emit(convert_qt)

	def saveImage(self):
		image = self.frame
		now = datetime.now() 
		filepath = now.strftime("%m-%d-%Y_%H:%M:%S")
		
		if not os.path.exists("images"):
			os.mkdir("images", 0755 );
		filepath = f"images/{filepath}.png"
		cv2.imwrite(filepath,image)


	def captureImage(self):
		# show 3 second timer and then set showPreview to false
		self.showPreview = False

	def showCapturedImage(self):
		image = cv2.cvtColor(self.frame,cv2.COLOR_BGR2RGB)
		flipped = cv2.flip(self.frame,1)
		convert_qt = QImage(flipped.data,flipped.shape[1],flipped.shape[0],QImage.Format_RGB888)
		self.ImageUpdate.emit(convert_qt)

	def stop():
		self.ThreadActive = False
		self.quit()

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
