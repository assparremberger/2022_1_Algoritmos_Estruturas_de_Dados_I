from abc import ABCMeta, abstractmethod


class Veiculo( metaclass=ABCMeta ):

	def __init__(self, modelo, ano = None):
		self.__modelo = modelo
		self.__ano = ano

	@property
	def modelo(self):
		pass

	@modelo.setter
	@abstractmethod
	def modelo( self, valor):
		pass

	@property
	def ano(self):
		pass

	@ano.setter
	@abstractmethod
	def ano( self, valor):
		pass

	def imprimir(self):
		print("Modelo: ", self.__modelo)
		print("Ano: ", self.__ano)

	@abstractmethod
	def imprimirEspecifico(self):
		pass