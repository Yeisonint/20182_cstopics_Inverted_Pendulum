import lib
import numpy as np
import math  
from collections import deque
import matplotlib.pyplot as plt
from scipy import interpolate
import csv, operator
import serial
import time
import random

class Qlearning_CartPole:

	# Definicion de la cantidad de estados
	buckets = (3, 16, 10)
	total_reward = []
	total_alpha = []
	total_epsilon = []
	stop=False
	iteration=0
	act_alpha=0
	act_epsilon=0

	# Tabla reward
	reward_table = np.array([
	[-4, -4.33, -4.66, -5, -3, 0.2, 0.3, 0.5, 0.75], 
	[-3.75, -4, -4.33, -4.66, -2, 0.3, 0.5, 0.75, 0.5], 
	[-3.5, -3.75, -4, -4.33, -1, 0.5, 0.75, 0.5, 0.3], 
	[-3.25, -3.5, -3.75, -4, 0, 0.75, 0.5, 0.3, 0.2], 
	[-3, -2, -1, 0, 1, 0, -1, -2, -3], 
	[0.2, 0.3, 0.5, 0.75, 0, -4, -3.75, -3.5, -3.25], 
	[0.3, 0.5, 0.75, 0.5, -1, -4.33, -4, -3.75, -3.5], 
	[0.5, 0.75, 0.5, 0.3, -2, -4.66, -4.33, -4, -3.75], 
	[0.75, 0.5, 0.3, 0.2, -3, -5, -4.66, -4.33, -4]])
	reward_table_x = np.arange(-1.0, 1.25, 0.25)
	reward_table_y = np.arange(1.0, -1.25, -0.25)
	reward_interpolation = interpolate.interp2d(reward_table_x, reward_table_y, reward_table, kind='linear')

	# Funcion de inicializacion
	def __init__(self, num_episodes = 1000, gamma = 1.0, min_alpha = 0.1, min_epsilon = 0.1, serialPort = '/dev/ttyACM0'):
		# Definimos las variables locales
		self.num_episodes = num_episodes #Numero de episodios hasta que termine
		self.gamma = gamma 				 #Factor de descuento
		self.min_alpha = min_alpha		 #Tasa de aprendizaje
		self.min_epsilon = min_epsilon	 #Tasa de exploracion
		self.Q_table = np.ones(list(self.buckets + (9,)))
		self.states_count = np.zeros(list(self.buckets))
		# Creamos el objeto del puerto serie
		self.OpenCM=serial.Serial(serialPort,baudrate=115200, timeout = 1.0)

	# pos = [-1.0, 1.0], donde:
	# 	* -1.0: máximo a la izquierda
	# 	*  1.0: máximo a la derecha
	# vel = [-1.0, 1.0], donde:
	# 	* -1.0: muy rapido a la izquierda
	# 	*  1.0: muy rapido a la derecha
	def get_reward(self,pos, vel):
		return self.reward_interpolation(pos, vel)[0]

	def closeSerialPort(self):
		self.OpenCM.close()

	def getData(self):
		return (self.total_reward,self.iteration,self.act_alpha,self.act_epsilon,self.total_alpha,self.total_epsilon)

	def stopAll(self):
		self.stop=True

	# Funcion decreciente con el tiempo
	def dec(self,value,time):
		return (np.multiply(np.linspace(np.sqrt(value),1,num=self.num_episodes),np.linspace(np.sqrt(value),1,num=self.num_episodes)))[self.num_episodes-time-1]

	# Funcion de disctretizacion
	def discretize(self):
		self.OpenCM.flushInput()
		self.OpenCM.flush()
		self.OpenCM.flushOutput()
		ser=str(self.OpenCM.readline().decode())
		ser=ser.split('\n')[0]
		ser=ser.split(',')
		return list(int(s) for s in ser)

	# Funcion que resetea
	def reset(self):
		val=0
		while True:
			try:
				self.OpenCM.write(b'0')
				time.sleep(0.1)
				self.OpenCM.write(b'8')
				time.sleep(0.1)
				self.OpenCM.flushInput()
				self.OpenCM.flush()
				self.OpenCM.flushOutput()
				ser=str(self.OpenCM.readline().decode())
				val=int(ser.split(',')[1])
			except:
				pass
			if val>=7 and val <=9:
				break
		self.OpenCM.write(b'4')
		return

	# Dependiendo del valor de epsilon, escoje entre explorar y explotar
	def choose_action(self, state, epsilon):
		# rand num actions
		try:
			return (random.randint(0,8),"Explorar") if (np.random.random() <= epsilon) else (np.argmax(self.Q_table[tuple(state)]),"Explotar")
		except:
			return (random.randint(0,8),"Explorar")
	def save_QTable(self,name):
		#np.savetxt('Q_table',self.Q_table.flatten(),fmt='%1.4e')
		np.save(name, self.Q_table)

	def test(self,Q_table_path):
		stop = False
		done = False
		# Hace un ultimo recorrido en el cual usa la tabla Q aprendida
		Q_table=np.load(Q_table_path)
		self.reset()
		current_state = self.discretize()[:3]
		while not done:
			try:
				time.sleep(0.05)
				print(current_state)
				action = np.argmax(Q_table[tuple(current_state)])
				print(action)
				self.OpenCM.write(bytes(str(action), 'utf-8'))
				new_state = self.discretize()[:3]
				current_state = new_state
				if (current_state[1]<=3 or current_state[1]>=12):
					done=True
				if stop:
					return "Finish by user"
			except:
				break
		return "Finish"

	# Funcion de aprendizaje
	def start(self):
		# Inicia el ciclo de iteraciones
		for e in range(self.num_episodes):
			# Reinicia el cartpole
			self.reset()
			# Discretizacion de la observacion
			try:
				current_state = self.discretize()[:3]
			except:
				current_state = [0,0,0]
			# Obtencion de la tasa de aprendizaje y el epsilon para esta iteracion
			alpha = self.dec(self.min_alpha,e)
			epsilon = self.dec(self.min_epsilon,e)
			# Inicializa la bandera de meta y crea el vector que almacenara los instantes en los que gana
			done = False
			actual_reward=0
			stop=False
			# Comienza el aprendizaje de la iteracion actual
			while not done:
				# Espera
				time.sleep(0.08)
				new_state = [0,0,0]
				try:
					action = self.choose_action(current_state, epsilon)
					self.OpenCM.write(bytes(str(action[0]), 'utf-8'))
					read = self.discretize()
				except:
					pass
				try:
					reward = self.get_reward(read[3]/30,read[4]/10)
					actual_reward+=reward
					new_state = read[:3]
				except:
					reward = 0
				if (current_state[1]<=3 or current_state[1]>=12):
					done=True
				else:
					try:
						self.Q_table[tuple([current_state[0],current_state[1],current_state[2],action[0]])] += alpha * (reward + self.gamma * np.max(self.Q_table[tuple(new_state)]) - self.Q_table[tuple([current_state[0],current_state[1],current_state[2],action[0]])])
						current_state = new_state
					except:
						pass
				if stop:
					return "Finish by user"
			# Guarda los rewards
			self.iteration=e
			self.act_alpha=alpha
			self.act_epsilon=epsilon
			self.total_reward.append(actual_reward)
			self.total_alpha.append(alpha)
			self.total_epsilon.append(epsilon)
		return "Complete"