from Cliente import Cliente
class FilaCliente:
	def __init__(self):
		self.inicio = None
		self.fim = None
		self.tamanho = 0
	def adicionar(self, cliente):
		# if self.inicio == None
		if self.tamanho == 0:
			self.inicio = cliente
		else:
			self.fim.proximo = cliente
		self.fim = cliente
		self.tamanho += 1
		self.imprimir()
	def imprimir(self) :
		print("\n---------------------\n")
		if self.inicio == None:
			print("A fila está vazia!")
		else:
			aux = self.inicio
			while( aux  ) :
				print( aux ) 
				aux = aux.proximo
				print(" ")
			print("\nTamanho da Fila: ", self.tamanho)
	def remover(self):
		if self.inicio == None:
			print("Fila Vazia!") 
		else: 
			if self.tamanho == 1:
				self.inicio = None
				self.fim = None
				self.tamanho = 0 
			else: 
				self.inicio = self.inicio.proximo
				self.tamanho -= 1
			self.imprimir()