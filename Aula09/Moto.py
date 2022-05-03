from Veiculo import Veiculo

class Moto( Veiculo ):

	def __init__(self, modelo, ano = None, cilindradas = 150):
		super().__init__(modelo, ano)
		self.cilindradas = cilindradas

	@property
	def modelo(self):
		return self.__modelo

	@modelo.setter 
	def modelo(self, valor):
		self.__modelo = valor

	@property
	def ano(self):
		return self.__ano

	@ano.setter 
	def ano(self, valor):
		self.__ano = valor

	def imprimirEspecifico(self):
		super().imprimir()
		print("Cilindradas: " , str(self.cilindradas))