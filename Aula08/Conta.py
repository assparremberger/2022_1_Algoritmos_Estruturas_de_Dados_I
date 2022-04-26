class Conta:

	tarifa = 1.99

	def __init__(self):
		self.__saldo = 0
	
	def imprimirSaldo(self):
		print("Saldo: ", self.__saldo)

	def __descontarTarifa(self):
		self.__saldo -= self.tarifa

	def depositar(self, valor):
		if self.__saldo + valor >= self.tarifa:
			self.__saldo += valor
			self.__descontarTarifa()

	def sacar(self, valor):
		if( self.__saldo - self.tarifa >= valor ):
			self.__saldo -= valor
			self.__descontarTarifa()
		else:
			print( "Saldo Insuficiente!")

	# Método acessor
	def getSaldo( self ):
		logado = True
		if logado: 
			return self.__saldo
	
	# Método Modificador
	def setSaldo( self, valor ):
		admin = False
		if admin:
			self.__saldo = valor
		else:
			print("Alteração não permitida")


	@property
	def saldo(self):
		logado = True
		if logado: 
			return self.__saldo
		else:
			return 0.0

	@saldo.setter
	def saldo(self, valor):
		admin = True
		if admin and valor >= 0:
			self.__saldo = valor
		else:
			print("Alteração não permitida")

		