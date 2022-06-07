from No import No

class Fila:
	def __init__(self):
		self.inicio = None
		self.fim = None
		self.tamanho = 0

	def adicionar(self, valor):
		no = No( valor )
		# if self.inicio == None
		if self.tamanho == 0:
			self.inicio = no
			self.fim = no
		else:
			self.fim.proximo = no
			self.fim = no
		self.tamanho += 1
		self.imprimir()


	def imprimir(self) :
		if self.inicio == None:
			print("A fila está vazia!")
		else:
			print("\n---------------------\n")
			aux = self.inicio
			texto = ""
			while( aux  ) :
				texto += str(aux.dado)  +  "  -  "
				aux = aux.proximo
			print( texto )
			print("\nTamanho da Fila: ", self.tamanho)

	def remover(self):
		# if self.tamanho == 0
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