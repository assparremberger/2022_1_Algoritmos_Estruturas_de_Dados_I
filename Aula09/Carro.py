from Veiculo import Veiculo

class Carro( Veiculo ):

	def __init__(self, modelo, ano = None, portas = 2):
		super().__init__(modelo, ano)
		self.portas = portas

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
		print("Portas: " , str(self.portas))

	
	

	