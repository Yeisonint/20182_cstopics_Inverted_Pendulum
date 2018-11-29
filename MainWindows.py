# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindows.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
import subprocess
from subprocess import Popen, PIPE
import graphics
import Q_Learning
import threading

class Ui_MainWindow(object):
	Port = ""
	path = ""
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(640, 480)
		MainWindow.setMinimumSize(QtCore.QSize(640, 480))
		MainWindow.setMaximumSize(QtCore.QSize(640, 480))
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.CB_Puerto = QtWidgets.QComboBox(self.centralwidget)
		self.CB_Puerto.setGeometry(QtCore.QRect(0, 40, 111, 27))
		self.CB_Puerto.setObjectName("CB_Puerto")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(0, 10, 221, 19))
		self.label.setObjectName("label")
		self.B_Refrescar = QtWidgets.QPushButton(self.centralwidget)
		self.B_Refrescar.setGeometry(QtCore.QRect(120, 40, 91, 27))
		self.B_Refrescar.setObjectName("B_Refrescar")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(230, 10, 201, 19))
		self.label_2.setObjectName("label_2")
		self.B_Conectar = QtWidgets.QPushButton(self.centralwidget)
		self.B_Conectar.setGeometry(QtCore.QRect(0, 70, 91, 27))
		self.B_Conectar.setObjectName("B_Conectar")
		self.B_Desconectar = QtWidgets.QPushButton(self.centralwidget)
		self.B_Desconectar.setGeometry(QtCore.QRect(100, 70, 111, 27))
		self.B_Desconectar.setObjectName("B_Desconectar")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(230, 40, 79, 19))
		self.label_3.setObjectName("label_3")
		self.label_4 = QtWidgets.QLabel(self.centralwidget)
		self.label_4.setGeometry(QtCore.QRect(230, 70, 79, 19))
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(self.centralwidget)
		self.label_5.setGeometry(QtCore.QRect(230, 100, 79, 19))
		self.label_5.setObjectName("label_5")
		self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.doubleSpinBox.setGeometry(QtCore.QRect(300, 40, 79, 28))
		self.doubleSpinBox.setObjectName("doubleSpinBox")
		self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.doubleSpinBox_2.setGeometry(QtCore.QRect(300, 70, 79, 28))
		self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
		self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.doubleSpinBox_3.setGeometry(QtCore.QRect(300, 100, 79, 28))
		self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
		self.label_6 = QtWidgets.QLabel(self.centralwidget)
		self.label_6.setGeometry(QtCore.QRect(390, 40, 191, 19))
		self.label_6.setObjectName("label_6")
		self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
		self.spinBox.setGeometry(QtCore.QRect(390, 60, 181, 28))
		self.spinBox.setObjectName("spinBox")
		self.B_Comenzar = QtWidgets.QPushButton(self.centralwidget)
		self.B_Comenzar.setGeometry(QtCore.QRect(390, 100, 111, 27))
		self.B_Comenzar.setObjectName("B_Comenzar")
		self.B_DetenerA = QtWidgets.QPushButton(self.centralwidget)
		self.B_DetenerA.setGeometry(QtCore.QRect(509, 100, 111, 27))
		self.B_DetenerA.setObjectName("B_DetenerA")
		#self.Barra_Progreso = QtWidgets.QProgressBar(self.centralwidget)
		#self.Barra_Progreso.setGeometry(QtCore.QRect(230, 160, 391, 23))
		#self.Barra_Progreso.setProperty("value", 24)
		#self.Barra_Progreso.setObjectName("Barra_Progreso")
		#self.label_7 = QtWidgets.QLabel(self.centralwidget)
		#self.label_7.setGeometry(QtCore.QRect(230, 140, 211, 19))
		#self.label_7.setObjectName("label_7")
		self.B_Ayuda = QtWidgets.QPushButton(self.centralwidget)
		self.B_Ayuda.setGeometry(QtCore.QRect(530, 10, 100, 27))
		self.B_Ayuda.setObjectName("B_Ayuda")
		self.label_8 = QtWidgets.QLabel(self.centralwidget)
		self.label_8.setGeometry(QtCore.QRect(60, 200, 221, 19))
		self.label_8.setObjectName("label_8")
		self.label_9 = QtWidgets.QLabel(self.centralwidget)
		self.label_9.setGeometry(QtCore.QRect(380, 200, 241, 19))
		self.label_9.setObjectName("label_9")
		self.label_10 = QtWidgets.QLabel(self.centralwidget)
		self.label_10.setGeometry(QtCore.QRect(0, 110, 221, 19))
		self.label_10.setObjectName("label_10")
		self.B_Cargar = QtWidgets.QPushButton(self.centralwidget)
		self.B_Cargar.setGeometry(QtCore.QRect(0, 130, 101, 27))
		self.B_Cargar.setObjectName("B_Cargar")
		self.B_Guardar = QtWidgets.QPushButton(self.centralwidget)
		self.B_Guardar.setGeometry(QtCore.QRect(110, 130, 100, 27))
		self.B_Guardar.setObjectName("B_Guardar")
		self.B_Probar = QtWidgets.QPushButton(self.centralwidget)
		self.B_Probar.setGeometry(QtCore.QRect(0, 160, 100, 27))
		self.B_Probar.setObjectName("B_Probar")
		self.B_DetenerP = QtWidgets.QPushButton(self.centralwidget)
		self.B_DetenerP.setGeometry(QtCore.QRect(110, 160, 100, 27))
		self.B_DetenerP.setObjectName("B_DetenerP")
		#self.WG_1 = QtWidgets.QWidget(self.centralwidget)
		self.WG_1 =graphics.RewardPlot(self.centralwidget)
		self.WG_1.setGeometry(QtCore.QRect(10, 220, 301, 221))
		self.WG_1.setObjectName("WG_1")
		#self.WG_2 = QtWidgets.QWidget(self.centralwidget)
		self.WG_2 =graphics.AlphaEpsilonPlot(self.centralwidget)
		self.WG_2.setGeometry(QtCore.QRect(320, 220, 301, 221))
		self.WG_2.setObjectName("WG_2")
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		# Valores spinbox
		self.spinBox.setRange(0,10000)
		self.doubleSpinBox.setRange(0.0,1.0)
		self.doubleSpinBox_2.setRange(0.0,1.0)
		self.doubleSpinBox_3.setRange(0.0,1.0)
		self.doubleSpinBox.setSingleStep(0.01)
		self.doubleSpinBox_2.setSingleStep(0.01)
		self.doubleSpinBox_3.setSingleStep(0.01)

		# Creamos las conecciones de los eventos
		self.B_Ayuda.setEnabled(False)
		self.B_Refrescar.clicked.connect(self.refreshSerialPort)
		self.B_Conectar.clicked.connect(self.connectSerialPort)
		self.B_Cargar.clicked.connect(self.openFile)
		self.B_Guardar.clicked.connect(self.saveFile)
		self.B_Comenzar.clicked.connect(self.startTraining)
		self.B_DetenerP.clicked.connect(self.stopTraining)
		self.B_DetenerA.clicked.connect(self.stopTraining)
		self.B_Probar.clicked.connect(self.testTraining)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Cart Pole Q Learning"))
		self.label.setText(_translate("MainWindow", "Seleccione el puerto serie:"))
		self.B_Refrescar.setText(_translate("MainWindow", "Refrescar"))
		self.label_2.setText(_translate("MainWindow", "Parametros aprendizaje:"))
		self.B_Conectar.setText(_translate("MainWindow", "S. Puerto"))
		self.B_Desconectar.setText(_translate("MainWindow", "Desconectar"))
		self.label_3.setText(_translate("MainWindow", "Gamma:"))
		self.label_4.setText(_translate("MainWindow", "Alpha:"))
		self.label_5.setText(_translate("MainWindow", "Epsilon:"))
		self.label_6.setText(_translate("MainWindow", "Numero de iteraciones:"))
		self.B_Comenzar.setText(_translate("MainWindow", "Comenzar"))
		self.B_DetenerA.setText(_translate("MainWindow", "Detener"))
		#self.label_7.setText(_translate("MainWindow", "Progreso del aprendizaje:"))
		self.B_Ayuda.setText(_translate("MainWindow", "Ayuda"))
		self.label_8.setText(_translate("MainWindow", "Recompensa vs iteraciones"))
		self.label_9.setText(_translate("MainWindow", "Alpha y Epsilon vs iteraciones"))
		self.label_10.setText(_translate("MainWindow", "Exportar e importar Q table"))
		self.B_Cargar.setText(_translate("MainWindow", "Cargar"))
		self.B_Guardar.setText(_translate("MainWindow", "Guardar"))
		self.B_Probar.setText(_translate("MainWindow", "Probar"))
		self.B_DetenerP.setText(_translate("MainWindow", "Detener"))

	def openFile(self):
		try:
			file = QFileDialog.getOpenFileName(None, "Abrir fichero", "")
			self.path = file[0]
			return ""
		except:
			return ""

 
	def saveFile(self):
		try:
			file = QFileDialog.getSaveFileName(None, "Guardar fichero", "")
			self.Cart.save_QTable(file[0])
			return QFileInfo(file).path()
		except:
			return ""

	def refreshSerialPort(self):
		self.CB_Puerto.clear()
		p = subprocess.run("python -m serial.tools.list_ports", stdout=subprocess.PIPE, shell=True)
		p = p.stdout.decode('utf-8').replace(" ","")
		p = p.split('\n')
		p = p[:len(p)-1]
		print(p)
		for port in p:
			self.CB_Puerto.addItem(port)

	def connectSerialPort(self):
		self.Port = self.CB_Puerto.currentText()

	def connectSerialPort(self):
		self.Port = self.CB_Puerto.currentText()

	def disconnectSerialPort(self):
		try:
			self.Cart.closeSerialPort()
		except:
			pass

	def startTraining(self):
		self.hiloCart = threading.Thread(target=self.training)
		self.hiloCart.start()
		try:
			pass
		except:
			print("Error, Asegurate de llenar todos los parametros")

	def stopTraining(self):
		try:
			#self.Cart.stop=True
			self.hiloCart._Thread_stop()
		except:
			pass

	def testTraining(self):
		print(self.path)
		self.Cart = Q_Learning.Qlearning_CartPole(self.spinBox.value(),self.doubleSpinBox.value(),self.doubleSpinBox_2.value(),self.doubleSpinBox_3.value(),self.Port)
		self.Cart.test(self.path)
		try:
			pass
		except:
			print("Error, Algo paso con la conexion o la tabla Q cargada")

	def training(self):
		self.Cart = Q_Learning.Qlearning_CartPole(self.spinBox.value(),self.doubleSpinBox.value(),self.doubleSpinBox_2.value(),self.doubleSpinBox_3.value(),self.Port)
		self.Cart.start()
		print(self.Cart.getData())
		self.WG_1.newData(self.Cart.getData()[0])
		self.WG_2.newData(self.Cart.getData()[4],self.Cart.getData()[5])

	

# Inicio codigo
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())

