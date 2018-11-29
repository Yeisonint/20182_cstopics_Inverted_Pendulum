import sys
import numpy as np

from qwt.qt.QtGui import QApplication, QPen
from qwt.qt.QtCore import Qt
from qwt import QwtPlot, QwtPlotMarker, QwtLegend, QwtPlotCurve, QwtText, QwtPlotGrid


class RewardPlot(QwtPlot):
	def __init__(self, *args):
		QwtPlot.__init__(self, *args)
		self.insertLegend(QwtLegend(), QwtPlot.RightLegend)
		self.enableAxis(self.xBottom)

		# insert a few curves
		self.Reward = QwtPlotCurve('Reward')
		self.Reward.setPen(QPen(Qt.darkGreen))
		self.Reward.attach(self)

		# initialize the data
		self.Reward.setData([0],[0])

		# replot
		self.replot()

	def newData(self,Reward):
		self.Reward.setData(list(range(len(Reward))),Reward)
		# replot
		self.replot()

class AlphaEpsilonPlot(QwtPlot):
	def __init__(self, *args):
		QwtPlot.__init__(self, *args)
		self.insertLegend(QwtLegend(), QwtPlot.RightLegend)
		self.enableAxis(self.xBottom)

		# insert a few curves
		self.Alpha = QwtPlotCurve('Alpha')
		self.Alpha.setPen(QPen(Qt.red))
		self.Alpha.attach(self)
		self.Epsilon = QwtPlotCurve('Epsilon')
		self.Epsilon.setPen(QPen(Qt.blue))
		self.Epsilon.attach(self)

		# initialize the data
		self.Alpha.setData([0],[0])
		self.Epsilon.setData([0],[0])

		# replot
		self.replot()

	def newData(self,Alpha,Epsilon):
		self.Alpha.setData(list(range(len(Alpha))),Alpha)
		self.Epsilon.setData(list(range(len(Epsilon))),Epsilon)
		# replot
		self.replot()
