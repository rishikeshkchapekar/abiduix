# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'application.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(800, 600)
		MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.img_label = QtWidgets.QLabel(self.centralwidget)
		self.img_label.setGeometry(QtCore.QRect(40, 20, 721, 381))
		self.img_label.setScaledContents(True)
		self.img_label.setObjectName("img_label")
		self.left_button = QtWidgets.QPushButton(self.centralwidget)
		self.left_button.setGeometry(QtCore.QRect(300, 450, 41, 41))
		font = QtGui.QFont()
		font.setBold(False)
		font.setWeight(50)
		self.left_button.setFont(font)
		self.left_button.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"border-radius: 10px;")
		self.left_button.setText("")
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("icons8-x-windows-11-outline-favicons/red-x-10340.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.left_button.setIcon(icon)
		self.left_button.setIconSize(QtCore.QSize(16, 16))
		self.left_button.setObjectName("left_button")
		self.right_button = QtWidgets.QPushButton(self.centralwidget)
		self.right_button.setGeometry(QtCore.QRect(420, 450, 41, 41))
		self.right_button.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"border-radius: 10px;")
		self.right_button.setText("")
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap("icons8-x-windows-11-outline-favicons/camera-6748.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(70, 460, 131, 41))
		self.pushButton.setStyleSheet("color: rgb(239, 41, 41);")
		self.pushButton.setObjectName("pushButton")
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

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.img_label.setText(_translate("MainWindow", "TextLabel"))
		self.left_label.setText(_translate("MainWindow", "Cancel"))
		self.right_label.setText(_translate("MainWindow", "Take Picture"))
		self.pushButton.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
